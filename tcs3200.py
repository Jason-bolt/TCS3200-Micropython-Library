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
    def __init__(self, s0, s1, s2, s3, out, led): # First function to run when the class is called
        self.s0 = Pin(s0, Pin.OUT)
        self.s1 = Pin(s1, Pin.OUT)
        self.s2 = Pin(s2, Pin.OUT)
        self.s3 = Pin(s3, Pin.OUT)
        self.out = Pin(out, Pin.IN)
        self.led = Pin(led, Pin.OUT)
        self.debug = False
        self.led.value(0) # To set the LEDs off
        
    # Function to turn on white LEDs on the module        
    def turnLightOn(self):
        self.led.value(1)
    
    # Function to turn on white LEDs on the module
    def turnLightOff(self):
        self.led.value(0)
        
    # Function to determine the state of the LEDs on the module
    def lightValue(self):
        return "On" if self.led.value() == 1 else "Off"
    
    # Show or not show debuging messages
    def setDebug(self, value=None):
        if value == None or value == False:
            self.debug = False
            return "Debug mode is turned off"
        else:
            self.debug = True
            return "Debug mode is turned on"
        