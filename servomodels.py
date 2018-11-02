
class ServoModel:

    @staticmethod
    def get_model(servo_model=''):

        dict_of_models = {'mg955': Mg955(), 'sg90': Sg90(), '': Sg90()}

        return dict_of_models[servo_model.lower()]


class ServoConstants:

    def __init__(self):

        self.frequency = 0
        self.m_pulse = 0
        self.n_pulse = 0


class Mg955(ServoConstants):

    def __init__(self):

        ServoConstants.__init__(self)

        self.frequency = 50
        self.m_pulse = 1 / 120
        self.n_pulse = 1


class Sg90(ServoConstants):

    def __init__(self):

        ServoConstants.__init__(self)

        self.frequency = 50
        self.m_pulse = 1 / 180
        self.n_pulse = 1
