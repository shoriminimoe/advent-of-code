"""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
import re

NUMBER_RE = re.compile(r"\d+")
SYMBOL_RE = re.compile(r"[^.\d]")

def sum_engine_parts(input):
    numbers = {}
    symbols = {}
    sum = 0
    with open(input) as fd:
        for idx, line in enumerate(fd):
            numbers[idx] = list(NUMBER_RE.finditer(line))
            symbols[idx] = list(SYMBOL_RE.finditer(line))
    for line_idx, line_symbols in symbols.items():
        for match in line_symbols:
            symbol_idx = match.start()
            if line_idx == 0:
                ...
            else:
                for number_match in numbers[line_idx-1]:
                    start, end = number_match.span()
                    if symbol_idx in range(start-1, end+1):
                        sum += int(number_match[0])



if __name__ == "__main__":
    sum_engine_parts("./example")
