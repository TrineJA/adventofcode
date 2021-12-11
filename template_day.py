from utils.utils import read_csv
import pandas as pd


def get_answer1(df: pd.DataFrame)->float:
    pass


def get_answer2(df: pd.DataFrame)->float:
    pass


if __name__ == "__main__":
    df = read_csv('data/2021/dayX.csv', col_names=['XX'], sep=',')
    answer1 = get_answer1(df)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df)
    print(f'Todays second answer is: {answer2}')    
