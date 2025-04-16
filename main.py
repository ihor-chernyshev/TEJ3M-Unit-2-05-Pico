"""
Created by Ihor Chernyshev
Created on March 2025
This program moves the servo to 180° and back to 0°
"""

import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A0.
pwm = pwmio.PWMOut(board.A0, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.7
my_servo = servo.Servo(pwm)

while True:
    my_servo.angle = 180 # Goes to 180°
    time.sleep(1) # Waits till servo reach 180°
    my_servo.angle = 0 # Goes to 0°
    time.sleep(1) # Waits till servo reach 0°
