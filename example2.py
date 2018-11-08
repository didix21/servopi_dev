
import RPi.GPIO as GPIO
from Servo import Servo
import time
import sys


class MyTest(object):

    def __init__(self, hello='', *args):

        print(hello)
        print("arg1", args[0])
        print("arg2", args[1])
        print("arg3", args[2])


def main(argv='0'):

    GPIO.setmode(GPIO.BOARD)

    # Servo Parameters

    raspberry_pin = 11
    servo_model = 'MyOwn'

    frequency = 50
    max_angle = 180
    min_pulse_width_in_millis = 1
    args = (frequency, max_angle, min_pulse_width_in_millis)

    my_own_servo = Servo(raspberry_pin, servo_model, *args)

    my_own_servo.write_angle(180)    # Move to position 180 º
    time.sleep(1)
    my_own_servo.write_angle(0)      # Move to position 0 º
    time.sleep(2)

    my_desired_angle = int(argv[0])
    my_own_servo.write_angle(my_desired_angle)


if __name__ == "__main__":

    main(sys.argv[1:])
