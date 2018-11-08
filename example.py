
from Servo import Servo
import sys
import RPi.GPIO as GPIO
import time


def main(argv):

    GPIO.setmode(GPIO.BOARD)
    angle = int(argv[0])
    my_servo = Servo(11, "Sg90")
    my_servo.write_angle(angle)
    print("Moving: ", angle)
    time.sleep(1)


if __name__ == "__main__":

    main(sys.argv[1:])
