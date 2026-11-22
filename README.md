# Embedded Systems Verification & Testing

## Project Overview

This project focuses on embedded systems verification and hardware testing using Python and the **LabJack T7-Pro** data acquisition device.

The main objective is to verify digital circuits, test logic ICs, and automate hardware testing using Python scripts.

This project was completed as part of the Embedded Systems Verification & Testing (ESVT) laboratory.

## Hardware & Technologies

- **Hardware:** LabJack T7-Pro
- **Programming Language:** Python
- **Software:** LabJack Kipling
- **Library:** LabJack LJM Python Library
- **Digital ICs:**
  - 7400 NAND Gate
  - 7448 BCD-to-7-Segment Decoder
  - 74HCT165 8-bit Shift Register
- **Testing Methods:** Digital I/O Testing, Loopback Testing, Logic Verification

## Project Structure

```text
Embedded-Systems-Verification-Testing/
│
├── README.md

├── Lab1/
   └── lab_task_description.pdf
   ├── labjack_test_task0.py
   ├── test_chip_task1.py
   └── lab_task2.py
   └── circuit_setup.jpg


```

## Laboratory Tasks

### Task 0: Digital Loopback Testing

**Objective:** Test digital input and output functionality using the LabJack T7-Pro.

Activities:
- Connected digital output FIO0 to digital input FIO3.
- Generated HIGH and LOW output signals.
- Read the corresponding digital input values.
- Verified digital signal behavior using Python.

**Python File:** `labjack_test_task0.py`

### Task 1: NAND Gate Verification (7400 IC)

**Objective:** Verify the functionality of all four NAND gates in the 7400 IC.

Activities:
- Tested all four NAND gates.
- Applied all four possible input combinations (00, 01, 10, 11).
- Compared actual outputs with the expected NAND truth table.
- Implemented automated PASS/FAIL verification using Python.

**Python File:** `test_chip_task1.py`

### Task 2: BCD Decoder and Shift Register Testing

**Objective:** Test a 7448 BCD-to-7-segment decoder and a 74HCT165 shift register.

Activities:
- Applied decimal BCD inputs from 0 to 9.
- Verified the seven-segment decoder output patterns.
- Loaded parallel data into the 74HCT165 shift register.
- Read serial output signals using the LabJack T7-Pro.
- Checked complementary serial outputs.
- Tested lamp test functionality.
- Tested leading-zero suppression functionality.

**Python File:** `lab_task2.py`

## How to Run the Project

### Requirements

- Python 3
- LabJack T7-Pro device
- LabJack LJM driver
- LabJack Python library
- Required digital circuit connections

### Execution

1. Install the LabJack LJM driver and Python library.
2. Connect the LabJack T7-Pro to the computer.
3. Connect the required digital circuits.
4. Make sure the device is disconnected from Kipling before running Python scripts.
5. Execute the desired Python script.

Example:

```bash
python src/labjack_test_task0.py
```

To run the NAND gate verification:

```bash
python src/test_chip_task1.py
```

To run the BCD decoder and shift register test:

```bash
python src/lab_task2.py
```

**Note:** These programs require physical LabJack hardware and appropriate circuit connections. They are not standalone simulations.

## Learning Outcomes

Through this laboratory project, I gained practical experience in:

- Embedded systems hardware interfacing.
- Python-based hardware control.
- Digital input/output configuration.
- Digital loopback testing.
- NAND gate truth table verification.
- Automated hardware testing.
- BCD-to-7-segment decoding.
- Serial and parallel data communication.
- Shift register testing.
- Hardware verification and debugging.

## Author

Embedded Systems Verification & Testing (ESVT)

**Academic Project**
