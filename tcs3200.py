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
from machine import Pin, Timer
import time


class TCS3200:
    
    # Frequency Array
    data_array = []
    
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
    
    # Color calibrations
    RED_BLACK = 225 #197 #16
    RED_WHITE = 1800 #1651 #154
    
    BLUE_BLACK = 420 #196 #18
    BLUE_WHITE = 2180 #1683 #173
    
    GREEN_BLACK = 260 #178 #14
    GREEN_WHITE = 1720 #1605 #146
    
    
    def __init__(self, s0=23, s1=5, s2=26, s3=18, out=22, led=19): # First function to run when the class is called
        self.s0 = Pin(s0, Pin.OUT)
        self.s1 = Pin(s1, Pin.OUT)
        self.s2 = Pin(s2, Pin.OUT)
        self.s3 = Pin(s3, Pin.OUT)
        self.out = Pin(out, Pin.IN)
        self.led = Pin(led, Pin.OUT)
        self.debug = False
        self.led.value(0) # To set the LEDs off
        # For frequency checking
        self.stop_flag = False
    
    def test(self):
        print(BLUE_BLACK)
        
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
        self.s0.value(value[0])
        self.s1.value(value[1])
        
    # Get current selected frequency
    def getFrequency(self):
        return self.s0.value(), self.s1.value()
    
    # Function to select the photodiode
    def selectPhotodiode(self, value: tuple):
        if type(value) is not tuple:
            raise TypeError("value should be a tuple")
        # Set photodiode type    
        self.s2.value(value[0])
        self.s3.value(value[1])
    
    # Get current selected photodiode configuration
    def getPhotodiode(self):
        return self.s2.value(), self.s3.value()
        
    # Function to read the frequency from the OUT pin
    def readFreq(self):
        return self.out.value()
    
    # Change stop flag to True
    def setStop(self):
        self.stop_flag = True
#         print("Done")
        
    # Display flag
    def showStopFlag(self):
        return self.stop_flag
    
    def _getFreq(self, array):
        count = 0
        pulseOn = False
        for i in array:
            if i == 1 and not pulseOn:
                count+=1
                pulseOn = True
            if i == 0:
                pulseOn = False
        return count
    
    # Test frequency output
    def _testFreq(self, frequency, color_comp):
        self.selectFrequency(frequency)
        self.selectPhotodiode(color_comp)
        data_array = []
        tim0 = Timer(0)
        tim0.init(period=1200, mode=Timer.ONE_SHOT, callback=lambda t:self.setStop())
        # Storing the data in the data array
        while self.showStopFlag() == False:
            data_array.append(self.readFreq())
        self.stop_flag = False
#             print(self.readFreq())

        # Show frequency
        frequency = self._getFreq(data_array)
        return frequency

    def _mapColor(self, red, green, blue):
        mapped_red = mapped_blue = mapped_black = 0
        
        mapped_red = (red - self.RED_BLACK) * 255 / (self.RED_WHITE - self.RED_BLACK)
        mapped_green = (green - self.GREEN_BLACK) * 255 / (self.GREEN_WHITE - self.GREEN_BLACK)
        mapped_blue = (blue - self.BLUE_BLACK) * 255 / (self.BLUE_WHITE - self.BLUE_BLACK)
        
        return mapped_red, mapped_green, mapped_blue
    

    def readColor(self, percentage):
        red_raw = self._testFreq(percentage, self.RED)
        green_raw = self._testFreq(percentage, self.GREEN)
        blue_raw = self._testFreq(percentage, self.BLUE)
        print(red_raw, green_raw, blue_raw)
        red, green, blue = self._mapColor(red_raw, green_raw, blue_raw)
#         print(green)
        return (red, green, blue)
        



