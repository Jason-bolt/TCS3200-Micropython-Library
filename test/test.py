"""
This class reads RGB values from a TCS3200 color sensor.

GND   Ground.
VDD   Supply Voltage (2.7-5.5V)
TCS3200  ESP32 Pin comment
S0, S1   Output frequency scaling selection inputs
S2, S3   Photodiode type selection inputs.


S1 = 5
S0 = 23
LED = 19
S3 = 18
S2 = 26
OUT = 22

    
Author: Jason Kwame Appiatu
Date: 23rd June, 2022
"""

from tcs3200 import TCS3200


# Test Code

tcs = TCS3200()
# tcs.setDebug(True)
# print(tcs.lightState())
# time.sleep(2)
tcs.setLeds(tcs.ON)
# print(tcs.lightState())
# tcs.readFreq()
# tcs._testFreq(tcs.TWO_PERCENT, tcs.GREEN)
# print(tcs._testFreq(tcs.TWO_PERCENT, tcs.RED))
# time.sleep(10)

# print(tcs._testFreq(tcs.TWO_PERCENT, tcs.GREEN))
# print(tcs._testFreq(tcs.TWO_PERCENT, tcs.BLUE))

# print(tcs._mapColor(200, 2, 2))


print(tcs.readColor(tcs.TWO_PERCENT))



