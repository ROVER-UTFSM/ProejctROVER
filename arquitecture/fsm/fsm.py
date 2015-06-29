from state import State

__author__ = 'Cristobal Ramirez'


class FSM:
    END = -1

    def __init__(self, states, init_state_id):
        """
        :param states: list of all State objects
        :param init_state_id: first state to be executed
        """
        self.END = FSM.END

        self._states = {}
        self._init_state = init_state_id
        self._current_state = self._init_state

        for state in states:
            assert isinstance(state, State), 'The second argument must be a list of only the State objects.'

            self._states[state.id] = state

    @property
    def END(self):
        return self.END

    def isEND(self):
        """
        :return: True if it is in the END state
        """
        if self._current_state == self.END:
            return True

        return False

    def run(self, signal=END):
        try:
            if signal == FSM.END:
                stater = self._states[self._current_state].run_state()
                self._current_state = self._states[self._current_state].next_state()
            else:
                self._current_state = signal
                stater = self._states[self._current_state].run_state()
                self._current_state = self._states[self._current_state].next_state()
        except KeyError:
            raise Exception("On state {0}: next_state() have to return a correct state ID.".format(
                str(self._current_state)))

        if self._current_state == self.END:
            self._current_state = self._init_state
            return self.END

        return stater
