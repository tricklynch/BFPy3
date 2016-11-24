import sys

DEFAULT_TAPE_SIZE = 30000
DEFAULT_CELL_SIZE = 256

class BrainFuckTape:
    def __init__(self, code=None, tape_size=None, cell_size=None):
        self._pointer = 0

        self._tape_size = tape_size
        if(None == tape_size):
            self._tape_size = DEFAULT_TAPE_SIZE
        self._tape = [0] * self._tape_size

        self._code = code
        if(None == code):
            self._code = sys.stdin.read()

    def run(self):
        NotImplemented

    def _plus(self):
        self._tape[self._pointer] += 1
        self._tape[self._pointer] %= 256

    def _minus(self):
        NotImplemented

    def _point_right(self):
        NotImplemented

    def _point_left(self):
        NotImplemented

    def _start_loop(self):
        NotImplemented

    def _end_loop(self):
        NotImplemented

    def _output(self):
        NotImplemented

    def _input(self):
        NotImplemented

def main():
    with open("test.bf", "r") as code:
        bf_tape = BrainFuckTape(code=code)
        bf_tape.run()

if __name__ == "__main__":
    main()
