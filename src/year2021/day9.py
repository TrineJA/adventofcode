from utils.utils import read_csv, df2grid
import pandas as pd
import itertools
import numpy as np


def find_lowpoints(df):
    # loop through elements and check for min
    lowpoint_idx = []
    for x in itertools.product(list(df.index), list(df.columns)):
        xval = df.iloc[x]
        # find neighbor values
        neighbors = []
        if x[0]>0:
            neighbors.append(df.iloc[x[0]-1,x[1]])
        if x[1]>0:
            neighbors.append(df.iloc[x[0],x[1]-1])
        if x[0]<df.shape[0]-1:
            neighbors.append(df.iloc[x[0]+1,x[1]])
        if x[1]<df.shape[1]-1:
            neighbors.append(df.iloc[x[0],x[1]+1])
        
        if xval < min(neighbors):
            lowpoint_idx.append(x)

    return lowpoint_idx


def neighbor_bassin_idx(df, bidx):
    bassin_idx = []
    if bidx[0]>0:
        iidx = (bidx[0]-1, bidx[1])
        if df.iloc[iidx] < 9:
            bassin_idx.append(iidx)
    if bidx[1]>0:
        iidx = (bidx[0],bidx[1]-1)
        if df.iloc[iidx] < 9:
            bassin_idx.append(iidx)
    if bidx[0]<df.shape[0]-1:
        iidx = (bidx[0]+1, bidx[1])
        if df.iloc[iidx] < 9:
            bassin_idx.append(iidx)
    if bidx[1]<df.shape[1]-1:
        iidx = (bidx[0],bidx[1]+1)
        if df.iloc[iidx] < 9:
            bassin_idx.append(iidx)

    return bassin_idx


def get_answer1(df: pd.DataFrame)->float:
    # split in 1 column per value
    df = df2grid(df)
    df = df.astype(int)

    # find lowpoints
    lowpoint_idx = find_lowpoints(df)

    # calculate score
    score = 0
    for idx in lowpoint_idx:
        val = df.loc[idx]
        score += (val+1)
 
    return score


def get_answer2(df: pd.DataFrame)->float:
    # split in 1 column per value
    df = df.astype(str)
    df = df['XX'].str.split('', len(df['XX'][0]), expand=True).drop(columns=[0])
    df.columns = df.columns-1
    df = df.astype(int)

    # find lowpoints
    lowpoint_idx = find_lowpoints(df)
    bassin_size = []

    for idx in lowpoint_idx:
        #find basin
        df_bassin = df<0
        df_bassin.loc[idx]=True
        bassin_idx_all = [idx]
        prev_bassin_idx_all = bassin_idx_all.copy()
        # brute force. for each bassin-point check add neighbors that are not 9. 
        # this will check the same point many times...
        maxItts = 1000
        for itts in range(maxItts):
            current_bassin_idx_all = bassin_idx_all.copy()
            for bidx in current_bassin_idx_all:
                nbidx_list = neighbor_bassin_idx(df, bidx)
                bassin_idx_all+=nbidx_list
            bassin_idx_all = list(set(bassin_idx_all))
            # check that we found new (then continue)
            if len(list(set(bassin_idx_all) - set(prev_bassin_idx_all)))==0:
                break
            #update
            prev_bassin_idx_all = bassin_idx_all.copy()

        #print(bassin_idx_all)
        bassin_size.append(len(bassin_idx_all))

    # get score
    bassin_size.sort(reverse=True)
    score = np.prod(bassin_size[0:3])
    return score

if __name__ == "__main__":
    df = read_csv('data/2021/day9.csv', col_names=['XX'], sep=',')
    answer1 = get_answer1(df)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df)
    print(f'Todays second answer is: {answer2}')    
