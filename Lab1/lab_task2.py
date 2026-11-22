# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:16:54 2026
CourseName : ESVT
@author: FARIHA NAZIA NOOR(2613172) , MINHAZUL ISLAM (2613507), Shifat Jahan Shama (2667724)
  """


from labjack import ljm
import time

# Expected active-HIGH segments for 7448 / 74LS48
# Based on its seven-segment function table
patterns = {
    0: "abcdef",
    1: "bc",
    2: "abdeg",
    3: "abcdg",
    4: "bcfg",
    5: "acdfg",
    6: "cdefg",
    7: "abc",
    8: "abcdefg",
    9: "abcfg"
}

handle = ljm.openS("ANY", "ANY", "ANY")

def write(pin, value):
    ljm.eWriteName(handle, pin, value)

def read(pin):
    return int(ljm.eReadName(handle, pin))

def test_digit(digit, lamp_test=1, rbi=1, expected_segments=None):

    # Send the 4-bit BCD number to 7448
    for bit in range(4):
        write(f"EIO{bit}", (digit >> bit) & 1)

    # Decoder control signals (both active LOW)
    write("EIO4", lamp_test)
    write("EIO5", rbi)

    time.sleep(0.05)

    # Ensure clock is LOW
    write("EIO7", 0)

    # Load the 8 parallel bits into 74HCT165
    write("EIO6", 0)
    time.sleep(0.02)
    write("EIO6", 1)
    time.sleep(0.02)

    serial_bits = []
    inverse_bits = []

    # Read H, G, F, E, D, C, B, A
    for i in range(8):
        serial_bits.append(read("CIO0"))
        inverse_bits.append(read("CIO1"))

        if i < 7:
            write("EIO7", 1)
            time.sleep(0.02)
            write("EIO7", 0)
            time.sleep(0.02)

    if expected_segments is None:
        expected_segments = patterns[digit]

    # Compare the seven display segments G through A.
    # H is BI/RBO and checked separately.
    expected = [
        int(segment in expected_segments)
        for segment in "gfedcba"
    ]
    actual = serial_bits[1:]

    segments_ok = (actual == expected)

    # Both serial outputs must be complementary
    inverse_ok = all(
        a != b for a, b in zip(serial_bits, inverse_bits)
    )

    print(f"\nDecimal digit: {digit}")
    print("Serial HGFEDCBA:",
          "".join(map(str, serial_bits)))
    print("Expected GFEDCBA:",
          "".join(map(str, expected)))
    print("Actual   GFEDCBA:",
          "".join(map(str, actual)))
    print("Segments:",
          "PASS" if segments_ok else "FAIL")
    print("Inverted serial output:",
          "PASS" if inverse_ok else "FAIL")

    return segments_ok and inverse_ok

try:
    # Initialize outputs
    write("EIO4", 1)  # Lamp test OFF
    write("EIO5", 1)  # Leading zero suppression OFF
    write("EIO6", 1)  # Parallel load inactive
    write("EIO7", 0)  # Clock LOW

    results = []

    # Test all decimal digits
    for digit in range(10):
        results.append(test_digit(digit))

    # Additional decoder function checks
    print("\n--- Lamp Test ---")
    results.append(
        test_digit(2, lamp_test=0,
                   expected_segments="abcdefg")
    )

    print("\n--- Leading Zero Suppression ---")
    results.append(
        test_digit(0, rbi=0, expected_segments="")
    )

    print("\n--- FINAL RESULT ---")
    print(f"{sum(results)}/{len(results)} tests passed")

finally:
    ljm.close(handle)
