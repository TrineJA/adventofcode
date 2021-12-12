import pandas as pd
from typing import List


def read_csv(input_file_path:str, col_names: List, sep=',', dtype=None, skip_blank_lines=True, engine='c')->pd.DataFrame:
    df = pd.read_csv(input_file_path, names=col_names, sep=sep, dtype=dtype, skip_blank_lines=skip_blank_lines, engine=engine)
    return df


def df2grid(df):
    #split in 1 column per value
    df = df.astype(str)
    df = df['XX'].str.split('', len(df['XX'][0]), expand=True).drop(columns=[0])
    df.columns = df.columns-1
    return df


def get_neighbor_idx(p, df, step = 1):
    p_list = [(p[0],p[1]+step),(p[0],p[1]-step),\
        (p[0]+step,p[1]), (p[0]-step,p[1]),\
        (p[0]+step,p[1]+step), (p[0]-step,p[1]-step),\
        (p[0]+step,p[1]-step), (p[0]-step,p[1]+step)\
        ]
    # check bounds
    p_list_clean =  p_list.copy()
    for pp in p_list:
        if min(pp)<df.index.min() or max(pp)>df.index.max():
            p_list_clean.remove(pp)
    return p_list_clean