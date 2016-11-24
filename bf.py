import sys

DEFAULT_TAPE_SIZE = 30000

class BrainFuckTape:
    def __init__(self, code=None, size=None):
        self._pointer = 0

        self._size = size
        if(None == size):
            self._size = DEFAULT_TAPE_SIZE

        self._code = code
        if(None == code):
            self._code = sys.stdin.read()

    def run(self):
        NotImplemented

    def _plus(self):
        NotImplemented

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
