import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

#from launch_ros.actions import Node
import RPi.GPIO as GPIO     #import library
import time
import rclpy


GPIO.setmode(GPIO.BCM)      #Set pin
AIN1 = 17
AIN2 = 18
BIN1 = 22
BIN2 = 23
GPIO.setWarnings(False)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.output(AIN1, 0)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.outout(AIN2, 0)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.output(BIN1, 0)
GPIO.setup(BIN2, GPIO.OUT)
GPIO.outout(BIN2, 0)

def forward():              #Motor rotation
    GPIO.output(AIN1,1)
    GPIO.output(AIN2,0)
    GPIO.output(BIN1,1)
    GPIO.output(BIN2,0)

def stop():
    GPIO.output(AIN1,0)
    GPIO.output(AIN2,0)
    GPIO.output(BIN1,0)
    GPIO.output(BIN2,0)

forward()
time.sleep(10)
stop()
GPIO.cleanup()

