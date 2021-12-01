# https://adventofcode.com/2021/day/1

data_in = 'data.txt'  # External data file


def load_data(file_in):
    """Read in data.txt"""
    data = []
    with open(file_in) as cur_file:
        for line in cur_file.readlines():
            data.append(int(line.rstrip()))
    return data


def part_one(data):
    """Solution for the first task."""
    increase_count = 0

    for index, measurement in enumerate(data[:-1]):
        if data[index+1] > measurement:
            increase_count += 1

    print('Answer is', increase_count)


def part_two(data):
    """Solution for the 2nd task."""
    increase_count = 0
    window_size = 3

    for index, measurement in enumerate(data[:-window_size]):
        current_window = sum(data[index:index+window_size])
        next_window = sum(data[index+1:index+1+window_size])

        if next_window > current_window:
            increase_count += 1

    print('Answer is', increase_count)


def main():
    """Main logic."""
    data = load_data(data_in)

    part_one(data)  # 1602

    part_two(data)  # 1633


if __name__ == '__main__':
    main()
