import RPi.GPIO as GPIO
from Servo import Servo


def main():

    GPIO.setmode(GPIO.BOARD)
    get_out = False
    raspberry_pin = 11
    my_servo = Servo(raspberry_pin)

    while not get_out:

        angle = input("Write an angle: ")
        my_servo.write_angle(int(angle))

        duty_cycke = input("Write duty cyccle: ")
        my_servo.write_duty_cycle(float(duty_cycke))


if __name__ == "__main__":

    main()
