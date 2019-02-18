#!/usr/bin/env python3

import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

ConnectedPin = 23
fanOnTemperature = 55
fanOffTemperature = 45

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ConnectedPin, GPIO.OUT)
    GPIO.setwarnings(False)
    return()

def measureCPUTemperature():
    raw_reading = os.popen('vcgencmd measure_temp').readline()
    temperature =(raw_reading.replace('temp=','').replace("\'C\n",""))
    return temperature

def FanControl():
    CPUTemperature = float(measureCPUTemperature())
    if CPUTemperature > fanOnTemperature:
        GPIO.output(ConnectedPin, True)
    elif CPUTemperature < fanOffTemperature:
        GPIO.output(ConnectedPin, False)
    return()

try:
    setup() 
    while True:
        FanControl()
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
