# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 12:50:11 2026
CourseName : ESVT
@author: FARIHA NAZIA NOOR(2613172) , MINHAZUL ISLAM (2613507), Shifat Jahan Shama (2667724)
"""

from labjack import ljm
import time

# Connect to LabJack
handle = ljm.openS("ANY", "ANY", "ANY")

# Set FIO0 HIGH
ljm.eWriteName(handle, "FIO0", 1)
time.sleep(1)

# Read FIO3
result = ljm.eReadName(handle, "FIO3")
print("FIO0 HIGH, FIO3 =", result)

# Set FIO0 LOW
ljm.eWriteName(handle, "FIO0", 0)
time.sleep(1)

# Read FIO3 again
result = ljm.eReadName(handle, "FIO3")
print("FIO0 LOW, FIO3 =", result)

# Disconnect
ljm.close(handle)