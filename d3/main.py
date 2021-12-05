# https://adventofcode.com/2021/day/3
from collections import Counter

data_in = 'data.txt'  # External data file


def load_data(file_in):
    """Read in data.txt"""
    data = []
    with open(file_in) as cur_file:
        for line in cur_file.readlines():
            data.append(line.rstrip())
    return data


def part_one(data):
    """Solution for the first task."""

    gamma_rate = ''
    epsilon_rate = ''

    for index in range(len(data[0])):
        counts = Counter([x[index] for x in data])

        gamma_rate += str(counts.most_common()[0][0])
        epsilon_rate += str(counts.most_common()[-1][0])

    return int(gamma_rate, 2), int(epsilon_rate, 2)


def recursion(data, rating):
    """Loop the list items bit by bit and on every loop advance
    only the values that contain the bit in the specific index."""

    for index in range(len(data[0])):
        if len(data) > 1:
            bits = Counter([x[index] for x in data])

            if rating == 'oxygen':
                if len(set(bits.values())) == 1:
                    val = '1'
                else:
                    val = bits.most_common()[0][0]
            else:  # co2
                if len(set(bits.values())) == 1:
                    val = '0'
                else:
                    val = bits.most_common()[-1][0]

            data = [x for x in data if x[index] == val]
        else:
            return data[0]
    return data[0]


def part_two(data):
    """Solution for the 2nd task."""
    oxygen_rating = recursion(data, 'oxygen')
    co2_rating = recursion(data, 'co2')

    return int(oxygen_rating, 2), int(co2_rating, 2)


def main():
    """Main logic."""
    data = load_data(data_in)

    gamma, epsilon = part_one(data)
    print(f'Answer is {gamma * epsilon}')  # 3813416

    oxygen, co2 = part_two(data)
    print(f'Answer is {oxygen * co2}')  # 2990784


if __name__ == '__main__':
    main()
