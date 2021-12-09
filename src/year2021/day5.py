from utils.load_data import read_csv
import pandas as pd
import numpy as np
import re

def check_horz_or_vert(p1, p2):
    if (p1[0]==p2[0]) or (p1[1] == p2[1]):
        is_horz_or_vert = True
    else:
        is_horz_or_vert = False
    return is_horz_or_vert

def check_diag(p1,p2):
    if abs(p1[0]-p2[0]) == abs(p1[1]-p2[1]):
        is_diag = True
    else:
        is_diag = False
    return is_diag      


def draw_horz_vert_line(df_diagram, p1, p2):
    # if col is contants (vertical)
    if p1[0]==p2[0]:
        pmin = min(p1[1],p2[1])
        pmax = max(p1[1],p2[1])
        rows = list(range(pmin,pmax+1))
        df_diagram.iloc[rows,p1[0]] += 1
    if p1[1]==p2[1]:
        pmin = min(p1[0],p2[0])
        pmax = max(p1[0],p2[0])
        cols = list(range(pmin,pmax+1))
        df_diagram.iloc[p1[1],cols] += 1
    return df_diagram


def draw_diag_line(df_diagram, p1, p2):
    Nsteps = abs(p2[0]-p1[0]) + 1
    col_sign = np.sign(p2[0]-p1[0])
    row_sign = np.sign(p2[1]-p1[1])
    for step in range(Nsteps):
        col_step = p1[0] + (col_sign*step)
        row_step = p1[1] + (row_sign*step)
        df_diagram.iloc[row_step,col_step] +=1
    return df_diagram


def get_answer1(df: pd.DataFrame)->float:
    # init
    N = df['from'].str.extractall('(\\d+)').astype(int).max().values[0]
    df_diagram = pd.DataFrame(0, index=np.arange(N+1), columns=np.arange(N+1))

    for idx, row in df.iterrows():
        # define points ([col, row])
        p1 = list(map(int, re.findall(r'\d+', row['from'])))
        p2 = list(map(int, re.findall(r'\d+', row['to'])))
        if check_horz_or_vert(p1, p2):
            df_diagram = draw_horz_vert_line(df_diagram, p1, p2)
    score = (df_diagram>=2).sum().sum()
    return score


def get_answer2(df: pd.DataFrame)->float:
    # init
    N = df['from'].str.extractall('(\\d+)').astype(int).max().values[0]
    df_diagram = pd.DataFrame(0, index=np.arange(N+1), columns=np.arange(N+1))

    for idx, row in df.iterrows():
        # define points ([col, row])
        p1 = list(map(int, re.findall(r'\d+', row['from'])))
        p2 = list(map(int, re.findall(r'\d+', row['to'])))
        if check_horz_or_vert(p1, p2):
            df_diagram = draw_horz_vert_line(df_diagram, p1, p2)
        if check_diag(p1,p2):
            df_diagram = draw_diag_line(df_diagram, p1, p2)

    score = (df_diagram>=2).sum().sum()
    return score

if __name__ == "__main__":
    df = read_csv('data/2021/day5.csv', col_names=['from','to'], sep='->', engine='python')
    answer1 = get_answer1(df)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df)
    print(f'Todays second answer is: {answer2}')    
