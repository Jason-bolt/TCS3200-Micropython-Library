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

# IMPORTING LIBRARIES
from machine import Pin
import time


class TCS3200:
    
    # Constants to control the LEDs on the TCS3200 module    
    ON = True
    OFF = False
    
    # Constants to scale the output frequency
    POWER_DOWN = (0, 0)
    TWO_PERCENT = (0, 1)
    TWENTY_PERCENT = (1, 0)
    HUNDRED_PERCENT = (1, 1)
    
    # Constants for the selecting the color
    RED = (0, 0)
    BLUE = (0, 1)
    CLEAR = (1, 0)
    GREEN = (1, 1)
    
    def __init__(self, s0=23, s1=5, s2=26, s3=18, out=22, led=19): # First function to run when the class is called
        self.s0 = Pin(s0, Pin.OUT)
        self.s1 = Pin(s1, Pin.OUT)
        self.s2 = Pin(s2, Pin.OUT)
        self.s3 = Pin(s3, Pin.OUT)
        self.out = Pin(out, Pin.IN)
        self.led = Pin(led, Pin.OUT)
        self.debug = False
        self.led.value(0) # To set the LEDs off
        
    # Function to turn on or off white LEDs on the module        
    def setLeds(self, state=OFF):
        if state:
            self.led.value(1)
            if self.debug:
                print("Switching LEDs on")
        else:
            self.led.value(0)
            if self.debug:
                print("Switching LEDs off")
        
    # Function to determine the state of the LEDs on the module
    def lightState(self):
        return "On" if self.led.value() == 1 else "Off"
    
    # Show or not show debuging messages
    def setDebug(self, value=None):
        if value == None or value == False:
            self.debug = False
            return "Debug mode is turned off"
        else:
            self.debug = True
            return "Debug mode is turned on"
        
    # Function to select the filter or color to be measured
    def selectFrequency(self, value: tuple):
        if type(value) is not tuple:
            raise TypeError("value should be a tuple")
        # Set frequency    
        self.s0.value(0)
        self.s1.value(1)
        
    # Get current selected frequency
    def getFrequency(self):
        return self.s0.value(), self.s1.value()
    
    # Function to select the photodiode
    def selectPhotodiode(self, value: tuple):
        if type(value) is not tuple:
            raise TypeError("value should be a tuple")
        # Set photodiode type    
        self.s2.value(0)
        self.s3.value(1)
    
    # Get current selected photodiode configuration
    def getPhotodiode(self):
        return self.s2.value(), self.s3.value()
        
    # Function to read the frequency from the OUT pin
    def readFreq(self):
#         for _ in range(1000):
        while True:
            print(self.out.value())



tcs = TCS3200()
# tcs.setDebug(True)
# print(tcs.lightState())
# time.sleep(2)
tcs.setLeds(tcs.ON)
# print(tcs.lightState())
tcs.selectFrequency(tcs.TWO_PERCENT)
tcs.selectPhotodiode(tcs.CLEAR)
tcs.readFreq()

