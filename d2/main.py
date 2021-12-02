# https://adventofcode.com/2021/day/2

data_in = 'data.txt'  # External data file


def load_data(file_in):
    """Read in data.txt"""
    data = []
    with open(file_in) as cur_file:
        for line in cur_file.readlines():
            row_list = line.split()
            data.append((row_list[0], int(row_list[1].rstrip())))
    return data


def part_one(data):
    """Solution for the first task."""
    pos_x = sum([x[1] for x in data if x[0] == 'forward'])
    pos_y = sum([x[1] for x in data if x[0] == 'up']) - sum([x[1] for x in data if x[0] == 'down'])

    print(f'Answer is {pos_x * -pos_y}')


def part_two(data):
    """Solution for the 2nd task."""
    pos_x, pos_y, angle = 0, 0, 0

    for unit in data:
        if unit[0] == 'up':
            angle -= unit[1]
        elif unit[0] == 'down':
            angle += unit[1]
        else:  # forward
            pos_x += unit[1]
            pos_y += unit[1] * angle

    print(f'Answer is {pos_x * pos_y}')


def main():
    """Main logic."""
    data = load_data(data_in)

    part_one(data)  # 2019945

    part_two(data)  # 1599311480


if __name__ == '__main__':
    main()
