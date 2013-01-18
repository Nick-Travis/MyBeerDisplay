#!/usr/bin/env python
from time import sleep
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
#GPIO.setup(24, GPIO.IN)
#GPIO.setup(25, GPIO.IN)
while True:
	if ( GPIO.input(18) == False ):
		os.system('mpg321 Choke_me.mp3 &')
	#if ( GPIO.input(24) == False ):
	#os.system('mpg321 power-converters.mp3 &')
	#if ( GPIO.input(25)== False ):
	#os.system('mpg321 vader.mp3 &')
	sleep(1);
