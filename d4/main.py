# https://adventofcode.com/2021/day/4
import pandas as pd

data_in = 'data.txt'  # External data file


def load_data(file_in):
    """Read in data.txt"""
    data = []
    temp_list = []

    with open(file_in) as cur_file:
        first_row = cur_file.readline().rstrip().split(',')
        drawn_numbers = list(map(int, first_row))

        for line in cur_file.readlines()[1:]:  # Exclude first row
            if line.rstrip() == '':
                if temp_list:
                    data.append(temp_list)
                    temp_list = []
            else:
                temp_list.append(line.rstrip().split())
        data.append(temp_list)

    return drawn_numbers, data


def bingo_in(df):
    """Check if dataframe column or row contains only instances of the same character."""
    for column in df:
        if len(set(df[column].tolist())) == 1:
            return True

    for index, row in df.iterrows():
        if len(set(row.tolist())) == 1:
            return True

    return False


def part_one(numbers, boards):
    """Solution for the first task."""
    df_boards = []
    for board in boards:
        df = pd.DataFrame(board)
        df_boards.append(df)

    for number in numbers:
        for df_board in df_boards:
            df_board.replace(str(number), 'X', inplace=True)
            if bingo_in(df_board):
                board_sum = sum(df_board.apply(pd.to_numeric, errors='coerce').sum())
                return int(board_sum)*int(number)


def part_two(numbers, boards):
    """Solution for the 2nd task."""
    df_boards = []
    for board in boards:
        df = pd.DataFrame(board)
        df_boards.append(df)

    wins = []

    for number in numbers:
        for idx, df_board in enumerate(df_boards):
            df_board.replace(str(number), 'X', inplace=True)
            if bingo_in(df_board) and idx not in [x[0] for x in wins]:
                board_sum = sum(df_board.apply(pd.to_numeric, errors='coerce').sum())
                wins.append((idx, int(board_sum)*int(number)))

    return wins[-1][1]


def main():
    """Main logic."""
    numbers, boards = load_data(data_in)

    result = part_one(numbers, boards)
    print(f'The correct answer is {result}')  # 8442

    result_two = part_two(numbers, boards)
    print(f'The correct answer is {result_two}')  # 8442


if __name__ == '__main__':
    main()
