#!/usr/bin/python

import time, os, subprocess

snap = 0
while snap < 4:
	gpout = subprocess.check_output("gphoto2 --capture-image-and-download --filename /home/pi/photobooth_images/photobooth%Y%m%d%H%M%S.jpg", stderr=subprocess.STDOUT, shell=True)
	snap += 1
	time.sleep(0.5)
subprocess.call("sudo /home/pi/scripts/photobooth/assemble_and_print", shell=True)
time.sleep(110)
print("ready for next round")
