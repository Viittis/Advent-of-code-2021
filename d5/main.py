# https://adventofcode.com/2021/day/5
import numpy as np
import itertools

data_in = 'data2.txt'  # External data file


def load_data(file_in):
    """Read in data.txt"""
    data = []
    with open(file_in) as cur_file:
        for line in cur_file.readlines():
            line = line.rstrip().split(' -> ')
            data.append((split_coordinates(line[0]), split_coordinates(line[1])))
    return data


def split_coordinates(coord_in):
    """Split coordinates to indicate start and end, convert value from str to int."""
    coord_list = coord_in.split(',')

    return list(map(int, coord_list))


def part_one(data):
    """Solution for the first task."""
    print('f')


def part_two(numbers, boards):
    """Solution for the 2nd task."""
    print('dfs')


def main():
    """Main logic."""
    data = load_data(data_in)
    filter_data = [x for x in data if x[0][0] == x[1][0] or x[0][1] == x[1][1]]  # Horizontal and vertical lines only

    print(filter_data)

    result = 0

    for line in filter_data:
        exclude_line = [x for x in filter_data if not x == line]
        #for line2 in exclude_line:
            #result += line_intersect(line, line2)

    print(result)


if __name__ == '__main__':
    main()
