
class ServoModel:

    def get_model(self, servo_model='', *args):

        return self.factory_models(servo_model, *args)

    @staticmethod
    def factory_models(servo_model, *args):

        dict_of_models = {'mg955': Mg955(), 'sg90': Sg90(), '': Sg90(), 'MyOwn': MyOwn(args)}

        if (servo_model == 'MyOwn') and (len(args) < 3):
            raise IndexError("The size of args has to be 3: frequency, max_angle, min_pulse_in_millisec!")

        return dict_of_models[servo_model.lower()]


class ServoConstants:

    def __init__(self, frequency, max_angle, min_pulse_in_millisec):

        self.frequency = frequency
        self.m_pulse = 1 / max_angle
        self.n_pulse = min_pulse_in_millisec


class Mg955(ServoConstants):

    def __init__(self):

        ServoConstants.__init__(self, 50, 120, 1)


class Sg90(ServoConstants):

    def __init__(self):

        ServoConstants.__init__(self, 50, 180, 1)


class MyOwn(ServoConstants):

    def __init__(self, *args):

        ServoConstants.__init__(args[0], args[1], args[2])

