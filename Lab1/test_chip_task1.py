# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:47:57 2026
CourseName : ESVT
@author: FARIHA NAZIA NOOR(2613172) , MINHAZUL ISLAM (2613507), Shifat Jahan Shama (2667724)
"""


from labjack import ljm
import time

# Connect to LabJack
handle = ljm.openS("ANY", "ANY", "ANY")

try:
    # Test all four input combinations
    for a, b in [(0, 0), (0, 1), (1, 0), (1, 1)]:

        # Send A and B to all four NAND gates
        for gate in range(4):
            ljm.eWriteName(handle, f"EIO{2*gate}", a)
            ljm.eWriteName(handle, f"EIO{2*gate+1}", b)

        time.sleep(0.2)

        expected = int(not (a and b))
        print(f"\nA={a}, B={b}, Expected={expected}")

        # Read all four NAND outputs
        for gate in range(4):
            output = int(ljm.eReadName(handle, f"CIO{gate}"))

            if output == expected:
                print(f"Gate {gate+1}: {output} - PASS")
            else:
                print(f"Gate {gate+1}: {output} - FAIL")

finally:
    ljm.close(handle)
