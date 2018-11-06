
class ServoModel:

    @staticmethod
    def get_model(servo_model=''):

        dict_of_models = {'mg955': Mg955(), 'sg90': Sg90(), '': Sg90()}

        return dict_of_models[servo_model.lower()]


class ServoConstants:

    def __init__(self, frequency, m_p, n_p):

        self.frequency = frequency
        self.m_pulse = m_p
        self.n_pulse = n_p


class Mg955(ServoConstants):

    def __init__(self):

        ServoConstants.__init__(self, 50, 1 / 120, 1)


class Sg90(ServoConstants):

    def __init__(self):

        ServoConstants.__init__(self, 50, 1 / 180, 1)

