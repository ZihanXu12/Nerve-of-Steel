"""
This program is used as an example for MGTC28.
timer.py is a simple Python script that will allow user to set timer duration.
Upon timer expiry, user will see the time up meme and sound notification.
timer.py uses the time library to help keep track of time
"""


# This program is timer that randomly count down from 5 secs to 25 secs


import time # The time library has a sleep function that will pause the script for a specifized amount of time
from PIL import Image # the pillow library makes it easy to display images 

im = Image.open("times-up.jpeg")
im2 = Image.open("get-up-stand-591ad7.jpg")
im2.show()


# Set timer 
import random
sleep_time = random.randint(5, 26)


time.sleep(sleep_time)

im.show()

