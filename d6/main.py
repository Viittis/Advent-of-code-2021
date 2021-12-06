# https://adventofcode.com/2021/day/6

data_in = 'data.txt'  # External data file


def load_data(file_in):
    """Read in data.txt"""

    with open(file_in) as cur_file:
        first_row = cur_file.readline().rstrip().split(',')

    return list(map(int, first_row))


def calculate_day(list_in):
    """Handle zeros and other numbers separately."""

    zeros = [6 for x in list_in if x == 0]  # Change all 0 -> 6
    zeros += [8] * len(zeros)  # Add equal count of eights to list

    other_nos = [x-1 for x in list_in if x != 0]  # Subtract 1 from all other values

    return zeros + other_nos


def part_one(data, days):
    """Solution for the first task."""
    for x in range(days):
        data = calculate_day(data)

    return data


def main():
    """Main logic."""
    data = load_data(data_in)

    result = part_one(data, 80)  # 346063
    print(len(result))


if __name__ == '__main__':
    main()
