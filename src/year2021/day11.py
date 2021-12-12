from utils.utils import read_csv, df2grid, get_neighbor_idx
import pandas as pd
import itertools


def get_answer1(df: pd.DataFrame)->float:
    Nstep = 100
    df = df2grid(df)
    df = df.astype(int)
    Nflashes = 0
    for itt in range(0,Nstep):
        #step 1
        df+=1

        #step 2
        df_has_flashed = pd.DataFrame(False, index=df.index, columns= df.columns)
        max_val_not_flashed = df.max().max()
        while max_val_not_flashed > 9:
            df_flash = df>9
            for x in itertools.product(list(df.index), list(df.columns)):
                if df_flash.iloc[x] and not df_has_flashed.iloc[x]:
                    #add to all neighbors
                    xn_list = get_neighbor_idx(x,df)
                    for xn in xn_list:
                        df.iloc[xn]+=1
            # update
            df_has_flashed = df_has_flashed | df_flash
            max_val_not_flashed = df[-df_has_flashed].max().max()

        #step 3
        df[df_has_flashed] = 0
        Nflashes+= df_has_flashed.sum().sum()
    
    return Nflashes


def get_answer2(df: pd.DataFrame)->float:
    Nstep = 1000
    df = df2grid(df)
    df = df.astype(int)
    for itt in range(0,Nstep):
        #step 1
        df+=1

        #step 2
        df_has_flashed = pd.DataFrame(False, index=df.index, columns= df.columns)
        max_val_not_flashed = df.max().max()
        while max_val_not_flashed > 9:
            df_flash = df>9
            for x in itertools.product(list(df.index), list(df.columns)):
                if df_flash.iloc[x] and not df_has_flashed.iloc[x]:
                    #add to all neighbors
                    xn_list = get_neighbor_idx(x,df)
                    for xn in xn_list:
                        df.iloc[xn]+=1
            # update
            df_has_flashed = df_has_flashed | df_flash
            max_val_not_flashed = df[-df_has_flashed].max().max()

        #step 3
        df[df_has_flashed] = 0
        
        # check sync
        if (df==0).sum().sum() == df.size:
            break   
    return itt+1


if __name__ == "__main__":
    df = read_csv('data/2021/day11.csv', col_names=['XX'], sep=',')
    answer1 = get_answer1(df)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df)
    print(f'Todays second answer is: {answer2}')    
