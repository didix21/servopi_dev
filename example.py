
from Servo import Servo


def main(args):

    my_servo = Servo(11, "Sg90")
    my_servo.move_angle(args)
