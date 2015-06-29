__author__ = 'Cristobal Ramirez'


class State(object):

    def __init__(self, _id):
        self.id = _id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    def run_state(self):
        """
        Algorithms, Actuations & Measurments need to be performated in this state

        :return: This value will be returned by the FSM. Use any value needed for testing the FSM.
        """
        pass

    def next_state(self):
        """
        Guards for next state

        :return: next state's ID
        """
        pass
