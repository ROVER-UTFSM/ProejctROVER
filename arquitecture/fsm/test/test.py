import random
import time
from fsm import FSM
from state import State

__author__ = 'catdog'


class BuscarCubo(State):

    def __init__(self, _id):
        State.__init__(self,_id)

    def run_state(self):
        print("Buscando cubo")
        time.sleep(random.random()*3)

    def next_state(self):
        return 2

class DetectartCubo(State):

    def __init__(self, _id):
        State.__init__(self, _id)

    def run_state(self):
        print("Detectando cubo")
        time.sleep(random.random()*3)

    def next_state(self):
        return 3

class AvanzarACubo(State):

    def __init__(self, _id):
        State.__init__(self,_id)

    def run_state(self):
        print("Avanzando a cubo")
        time.sleep(random.random()*3)

    def next_state(self):
        return FSM.END

if __name__ == "__main__":

    bC = BuscarCubo(1)
    dC = DetectartCubo(2)
    aaC = AvanzarACubo(3)

    machine = FSM([bC, dC, aaC, 3], 1)

    while not machine.isEND():
        machine.run()

    print ("This is the END of it")
