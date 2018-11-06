
from Servo import Servo
import sys
import RPi.GPIO as GPIO

def main(argv):

    GPIO.setmode(GPIO.BOARD)

    angle = int(argv[0])
    my_servo = Servo(11, "Sg90")
    my_servo.move_angle(angle)
    print("Moving: ", angle)


if __name__ == "__main__":

    main(sys.argv[1:])
