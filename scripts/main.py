#!/usr/bin/env python3
import numpy as np
import rospy
import sys
import os
import time
import cv2
# Path selection webots controller
sys.path.insert(0, "/usr/local/webots/lib/controller/python36")
from controller import *

# Set robot Name
os.environ['WEBOTS_ROBOT_NAME'] = 'Matrice 600 Pro'


def config_robot(robot):
    # Function to init the system
    front_right = robot.getMotor('rotational motor1')
    rear_right = robot.getMotor('rotational motor5')
    front_left = robot.getMotor('rotational motor3')
    rear_left = robot.getMotor('rotational motor2')
    # Function to complete rotation
    front_right.setPosition(float('inf'))
    front_left.setPosition(float('inf'))
    rear_right.setPosition(float('inf'))
    rear_left.setPosition(float('inf'))
    return front_right, front_left, rear_right, rear_left


def send_robot(motor, set_point):
    motor.setVelocity(set_point)
    return None


def main(robot):
    time_step = int(robot.getBasicTimeStep())

    # Robot configuration
    front_right, front_left, rear_right, rear_left = config_robot(robot)
    send_robot(front_right, 0)
    send_robot(front_left, 0)
    send_robot(rear_right, 0)
    send_robot(rear_left, 0)

    # loop time
    loop_rate = rospy.Rate(100)

    # motor velocity
    speed = 50

    # Simulation
    while robot.step(time_step) != -1:
        # Fligth controller
        send_robot(front_right, speed)
        send_robot(front_left, -speed)
        send_robot(rear_right, -speed)
        send_robot(rear_left, speed)
        loop_rate.sleep()
    return None


if __name__ == '__main__':
    try:
        rospy.init_node('Drone_DJI_MAVIC_Pro_Webots', anonymous=False)
        # Robot declaration
        robot1 = Robot()
        main(robot1)

    except KeyboardInterrupt:
        print("Pres Ctrl-c to end the statement")
