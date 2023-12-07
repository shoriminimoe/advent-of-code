from collections import Counter


def get_counter(counts):
    counter = Counter(red=0, green=0, blue=0)
    for count in counts:
        val, key = count.split()
        counter[key] = int(val)
    return counter


def parse_games(line):
    game_idx, game_str = line.split(":", maxsplit=1)
    game_idx = int(game_idx.split()[-1])
    game_rounds = [round_ for round_ in game_str.split(";")]
    games = []
    for round_ in game_rounds:
        counts = round_.split(",")
        games.append(get_counter(counts))
    return game_idx, games


def game_is_possible(game):
    return all(round_is_possible(round_counter) for round_counter in game)


def round_is_possible(round_counter):
    bag = Counter(red=12, green=13, blue=14)
    bag.subtract(round_counter)
    return all(val >= 0 for val in bag.values())


def process_games(input):
    sum = 0
    with open(input) as fd:
        for line in fd:
            idx, games = parse_games(line)
            if game_is_possible(games):
                sum += idx
            print(idx, games)
    print(sum)


if __name__ == "__main__":
    process_games("./input")
    minimum_set("./example")
