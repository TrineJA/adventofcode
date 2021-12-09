from utils.load_data import read_csv
import pandas as pd


def get_answer1(df: pd.DataFrame)->float:
    hor = 0
    depth = 0
    for idx, row in df.iterrows():
        if row.dir == 'forward':
            hor += row.step
        elif row.dir == 'down':
            depth +=row.step
        elif row.dir == 'up':
            depth -= row.step

    return hor*depth


def get_answer2(df: pd.DataFrame)->float:
    hor = 0
    depth = 0
    aim = 0
    for idx, row in df.iterrows():
        if row.dir == 'forward':
            hor += row.step
            depth += aim * row.step
        elif row.dir == 'down':
            aim +=row.step
        elif row.dir == 'up':
            aim -= row.step

    return hor*depth


if __name__ == "__main__":
    df = read_csv('data/2021/day2.csv', col_names=['dir','step'], sep=' ')
    answer1 = get_answer1(df)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df)
    print(f'Todays second answer is: {answer2}')    
