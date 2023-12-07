import re


def sum_digits(input):
    sum = 0
    with open(input) as fd:
        for line in fd:
            numbers = re.findall(r"\d", line)
            value = int(f"{numbers[0]}{numbers[-1]}")
            sum += value
    print(sum)


def sum_words(input):
    words = r"one|two|three|four|five|six|seven|eight|nine"
    word_re = re.compile(rf"(\d|{words})")
    reverse_word_re = re.compile(rf"(\d|{words[-1::-1]})")
    number_map = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    sum = 0
    with open(input) as fd:
        for line in fd:
            numbers = word_re.findall(line)
            reversed_numbers = reverse_word_re.findall(line[-1::-1])
            value = int(
                f"{number_map[numbers[0]]}{number_map[reversed_numbers[0][-1::-1]]}"
            )
            sum += value
    print(sum)


if __name__ == "__main__":
    sum_digits("./input")
    sum_words("./input")
