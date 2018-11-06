
from servomodels import ServoModel
import RPi.GPIO as GPIO


class Servo(object):

    def __init__(self, rasp_pin, servo_model="mg955"):

        self._pulse_width = 0
        self._duty_cycle = 7.5
        self.s_model = ServoModel().get_model(servo_model)
        self.__configure_pin(rasp_pin)
        self.__configure_pwm()

    def move_angle(self, angle):

        self.__get_pulse_width(angle)
        self._duty_cycle = self.__get_duty_cycle()
        self._pwm.ChangeDutyCycle(self._duty_cycle)

        return self._duty_cycle

    def __configure_pwm(self):

        self._pwm = GPIO.PWM(self._pin, self.s_model.frequency)
        self._pwm.start(self._duty_cycle)

    def __configure_pin(self, rasp_pin):

        self._pin = rasp_pin
        GPIO.setup(self._pin, GPIO.OUT)

    def __set_duty_cycle_in_raspi(self):

        self.__get_duty_cycle()

    def __get_pulse_width(self, angle):

        self._pulse_width = self.s_model.m_pulse * angle + self.s_model.n_pulse

    def __get_duty_cycle(self):

        return self._pulse_width * self.s_model.frequency


if __name__ == "__main__":

    newservo = Servo(1)
    print("frequency: ", newservo.s_model.frequency)
    print("m_pulse: ", newservo.s_model.m_pulse)
    print("n_pulse: ", newservo.s_model.n_pulse)
