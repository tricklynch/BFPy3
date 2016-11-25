import sys

DEFAULT_TAPE_SIZE = 30000
DEFAULT_CELL_SIZE = 256

class BrainFuckMachine:
    def __init__(
            self,
            code=None,
            tape_size=DEFAULT_TAPE_SIZE,
            cell_size=DEFAULT_CELL_SIZE,
            cell_wrap=True,
            tape_wrap=True,
            extend_tape=False
        ):
        self._code = code
        if self._code == None:
            self._code = sys.stdin.read()

        self._tape_ptr = 0

        self._tape_size = tape_size
        self._tape = [0] * self._tape_size

        self._code_ptr = 0
        self._code = code

        self._cell_size = cell_size
        self._cell_wrap = cell_wrap
        self._tape_wrap = tape_wrap
        self._extend_tape = extend_tape

    def run(self):
        while self._code_ptr in range(len(self._code)):
            instruction = self._code[self._code_ptr]
            if instruction == '+':
                self._plus()
            elif instruction == '-':
                self._minus()
            elif instruction == '>':
                self._point_right()
            elif instruction == '<':
                self._point_left()
            elif instruction == '[':
                self._start_loop()
            elif instruction == ']':
                self._end_loop()
            elif instruction == '.':
                self._output()
            elif instruction == ',':
                self._input()
            self._code_ptr += 1

    def _plus(self):
        self._tape[self._tape_ptr] += 1
        if self._cell_wrap:
            self._tape[self._tape_ptr] %= self._cell_size

    def _minus(self):
        self._tape[self._tape_ptr] -= 1
        if self._cell_wrap:
            self._tape[self._tape_ptr] %= self._cell_size

    def _point_right(self):
        self._tape_ptr += 1
        if self._tape_ptr == len(self._tape):
            if self._extend_tape:
                self._tape.append(0)
            elif self._tape_wrap:
                self._tape_ptr = 0
            else:
                # TODO: throw an error
                NotImplemented

    def _point_left(self):
        self._tape_ptr -= 1
        if self._tape_ptr == -1:
            if self._extend_tape:
                self._tape = [0] + self._tape
                self._tape_ptr = 0
            elif self._tape_wrap:
                self._tape_ptr += len(self._tape)
            else:
                # TODO: throw an error
                NotImplemented

    def _start_loop(self):
        pass

    def _end_loop(self):
        if self._tape[self._tape_ptr] == 0:
            return
        cnt = 1
        while cnt != 0:
            self._code_ptr -= 1
            if self._code[self._code_ptr] == ']':
                cnt += 1
            elif self._code[self._code_ptr] == '[':
                cnt -= 1

    def _output(self):
        sys.stdout.write(chr(self._tape[self._tape_ptr]))

    def _input(self):
        self._tape[self._tape_ptr] = ord(sys.stdin.read(1))

def main():
    with open("test.bf", "r") as code:
        bf_tape = BrainFuckMachine(code=code.read())
        bf_tape.run()

if __name__ == "__main__":
    main()
