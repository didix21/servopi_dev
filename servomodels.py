
class ServoModel:

    def get_model(self, servo_model='', *args):

        return self.factory_models(servo_model, *args)

    @staticmethod
    def factory_models(servo_model, *args):

        dict_of_models = {'mg955': Mg955(), 'sg90': Sg90(), '': Sg90(), 'myown': MyOwn(*args)}

        if (servo_model == 'MyOwn') and (len(args) < 3):
            raise IndexError("The size of args has to be 3: frequency, max_angle, min_pulse_in_millisec!")

        return dict_of_models[servo_model.lower()]


class ServoConstants:

    def __init__(self, frequency, max_angle, min_pulse_in_millisec):

        self.frequency = frequency
        self.m_pulse = 2 / max_angle
        self.n_pulse = min_pulse_in_millisec


class Mg955(ServoConstants):

    def __init__(self):

        ServoConstants.__init__(self, 50, 120, 1)


class Sg90(ServoConstants):

    def __init__(self):

        ServoConstants.__init__(self, 50, 180, 0.5)


class MyOwn(ServoConstants):

    def __init__(self, *args):

        if len(args) == 3:
            ServoConstants.__init__(self, args[0], args[1], args[2])
        else:
            ServoConstants.__init__(self, 0, 1, 0)

