import argparse
import sys

DEFAULT_TAPE_SIZE = 9999
DEFAULT_CELL_SIZE = 128

class BrainFuckMachine:

    def __init__(
            self,
            code_file=None,
            input_file=None,
            output_file=None,
            tape_size=DEFAULT_TAPE_SIZE,
            cell_size=DEFAULT_CELL_SIZE,
            cell_wrap=False,
            tape_wrap=False,
            extend_tape=False,
            debug_level=0
        ):
        if code_file == None:
            self._code = sys.stdin.read()
        else:
            self._code = code_file.read()

        self._input_file = input_file
        if self._input_file == None:
            self._input_file = sys.stdin

        self._output_file = output_file
        if self._output_file == None:
            self._output_file = sys.stdout

        self._tape_ptr = 0

        self._tape_size = tape_size
        self._tape = [0] * self._tape_size

        self._code_ptr = 0

        self._cell_size = cell_size
        self._cell_wrap = cell_wrap
        self._tape_wrap = tape_wrap
        self._extend_tape = extend_tape

        self._debug_level = debug_level

        self._instruction_function_dict = {
            '+' : self._plus,
            '-' : self._minus,
            '>' : self._point_right,
            '<' : self._point_left,
            '[' : self._start_loop,
            ']' : self._end_loop,
            '.' : self._output,
            ',' : self._input
        }

    def run(self):
        # TODO: throw exception if square brackets are unbalanced
        while self._code_ptr in range(len(self._code)):
            instruction = self._code[self._code_ptr]
            try:
                self._instruction_function_dict[instruction]()
            except:
                pass
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
        self._output_file.write(chr(self._tape[self._tape_ptr]))

    def _input(self):
        self._tape[self._tape_ptr] = ord(self._input_file.read(1))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--code",
        help="The file to read brainfuck code from"
    )
    parser.add_argument(
        "-i", "--input",
        help="The file to read input from with the , operator"
    )
    parser.add_argument(
        "-o", "--output",
        help="The file to write to with the . operator"
    )
    parser.add_argument(
        "-l", "--length",
        type=int,
        default=DEFAULT_TAPE_SIZE,
        help="The number of cells in the tape"
    )
    parser.add_argument(
        "-s", "--size",
        type=int,
        default=DEFAULT_CELL_SIZE,
        help="The size maximum size that can be stored in a cell"
    )
    parser.add_argument(
        "-e", "--extend",
        action="store_true",
        help="Extends the tape if the program attempts to go beyond the edges"
    )
    parser.add_argument(
        "-a", "--arbitrary",
        action="store_true",
        help="Allows cells to grow to arbitrary sizes"
    )
    parser.add_argument(
        "-w", "--cellwrap",
        action="store_true",
        help="If the cell's value overflows, it wraps like integer overflow"
    )
    parser.add_argument(
        "-t", "--tapewrap",
        action="store_true",
        help="If the cell pointer overflows, it wraps to the tape's other side"
    )
    parser.add_argument(
        "-d", "--debuglevel",
        type=int,
        default=0,
        help="The amount of spam to print"
    )
    args = parser.parse_args()

    files_to_close = []

    code_filename = args.code
    code_file = None
    if code_filename != None:
        code_file = open(code_filename, "r")
        files_to_close.append(code_file)

    input_filename = args.input
    input_file = None
    if input_filename != None:
        input_file = open(input_filename, "r")
        files_to_close.append(input_file)

    output_filename = args.output
    output_file = None
    if output_filename != None:
        output_file = open(output_filename, "w")
        files_to_close.append(output_file)

    bf_tape = BrainFuckMachine(
        code_file=code_file,
        input_file=input_file,
        output_file=output_file,
        tape_size=args.length,
        cell_size=args.size,
        cell_wrap=args.cellwrap,
        tape_wrap=args.tapewrap,
        extend_tape=args.extend,
        debug_level=args.debuglevel
    )
    bf_tape.run()

    for f in files_to_close:
        f.close()

if __name__ == "__main__":
    main()
