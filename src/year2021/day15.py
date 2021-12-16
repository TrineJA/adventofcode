from utils.utils import read_csv, df2grid
import pandas as pd
import numpy as np
import heapq


def get_neighbor_idx_nodiag(p, df, step = 1):
    p_list = [(p[0],p[1]+step),(p[0],p[1]-step),\
        (p[0]+step,p[1]), (p[0]-step,p[1]),
        ]
    # check bounds
    p_list_clean =  p_list.copy()
    for pp in p_list:
        if min(pp)<df.index.min() or max(pp)>df.index.max():
            p_list_clean.remove(pp)
    return p_list_clean


def find_lowrisk_path(df):
    [nrow, ncol] = df.shape
    df_vis = pd.DataFrame(False, index = df.index, columns=df.columns)

    start = (0,0,0) #risk, row, col
    queue = [start] 
    goal = (nrow-1, ncol-1)

    while queue:
        risk, x, y = heapq.heappop(queue)
        #heap pops according to lowest value of first entry (risk). 
        #  in every loop we take 1 step for path with currently lowest risk
        p = (x,y)
        if df_vis.iloc[p]:
            continue
        elif p == goal:
            return risk
        else:
            #update visit
            df_vis.iloc[(x,y)]=True
            # look at neighbors. rank by risk
            for pn in get_neighbor_idx_nodiag(p,df):
                if df_vis.iloc[pn]:
                    continue
                else:
                    newrisk = risk + df.iloc[pn]
                    heapq.heappush(queue, (newrisk, pn[0], pn[1]))


def get_answer1(df: pd.DataFrame)->float:
    df = df2grid(df)
    df = df.astype(int)
    risk = find_lowrisk_path(df)
    return risk


def get_answer2(df: pd.DataFrame)->float:
    df = df2grid(df)
    df = df.astype(int)
    # make new grid
    Nrep = 5
    df_all_list = []
    for rowrep in range(Nrep):
        dfcol0 = (rowrep) + df.copy()
        dfcol0[dfcol0>9] += -9
        df_rowx_list = [dfcol0]
        for colrep in range(Nrep-1):
            df_newtile = (colrep+1) + dfcol0.copy()
            df_newtile[df_newtile>9] += -9
            df_rowx_list.append(df_newtile)
        df_rowx = pd.concat(df_rowx_list, axis=1)
        df_rowx.columns = range(df_rowx.shape[1])
        df_all_list.append(df_rowx)
    df_all = pd.concat(df_all_list, axis=0).reset_index(drop=True)
    risk = find_lowrisk_path(df_all)
    return risk


if __name__ == "__main__":
    df = read_csv('data/2021/day15.csv', col_names=['XX'], sep=',')

    answer1 = get_answer1(df)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df)
    print(f'Todays second answer is: {answer2}')
