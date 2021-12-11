from utils.utils import read_csv, df2grid

import pandas as pd

def get_answer1(df: pd.DataFrame)->float:
    Nstep = 10
    df = df2grid(df)
    df = df.astype(int)




def get_answer2(df: pd.DataFrame)->float:
    pass


if __name__ == "__main__":
    #df = read_csv('data/2021/dayX.csv', col_names=['XX'], sep=',')
    df = read_csv('test/2021/data/day11.csv', col_names=['XX'], sep=',')
    answer1 = get_answer1(dl)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df)
    print(f'Todays second answer is: {answer2}')    
