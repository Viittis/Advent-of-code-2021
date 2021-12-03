# https://adventofcode.com/2021/day/3
from collections import Counter

data_in = 'data2.txt'  # External data file


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


def exhaustive_loop(data, val):
    result = ''

    if val == 'ogr':
        idx = 0
    else:
        idx = -1

    for index in range(len(data[0])):
        counts = Counter([x[index] for x in data])
        print(list(counts.values()))

        if all(x == list(counts.values())[0] for x in list(counts.values())):
            result += str(idx+1)
        else:
            result += str(counts.most_common()[idx][0])

    print(result)
    return int(result, 2)


def part_two(data):
    """Solution for the 2nd task."""
    first_bits = Counter([x[0] for x in data])

    ogr_val = first_bits.most_common()[0][0]
    csr_val = first_bits.most_common()[-1][0]

    ogr_data = [x for x in data if x[0] == ogr_val]
    csr_data = [x for x in data if x[0] == csr_val]

    ogr_value = exhaustive_loop(ogr_data, 'ogr')
    csr_value = exhaustive_loop(csr_data, 'csr')

    print(ogr_value, csr_value)


def main():
    """Main logic."""
    data = load_data(data_in)

    gamma, epsilon = part_one(data)
    #print(f'Answer is {gamma * epsilon}')  # 3813416

    part_two(data)


if __name__ == '__main__':
    main()
