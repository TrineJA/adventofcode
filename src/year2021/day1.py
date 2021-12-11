from utils.utils import read_csv
import pandas as pd


def get_answer1(df: pd.DataFrame)->float:
    df['XX2'] = df.XX.shift(1)
    return (df.XX > df.XX2).sum()


def get_answer2(df: pd.DataFrame)->float:
    df2 = df.XX.rolling(3).sum().to_frame()
    df2['XX2'] = df2.XX.shift(1)
    return (df2.XX > df2.XX2).sum()


if __name__ == "__main__":
    df = read_csv('data/2021/day1.csv', col_names=['XX'], sep=',')
    answer1 = get_answer1(df)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df)
    print(f'Todays second answer is: {answer2}')    
