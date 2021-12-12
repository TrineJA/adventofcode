from utils.utils import read_csv, df2grid, get_neighbor_idx
import pandas as pd
import itertools


def get_answer1(df: pd.DataFrame)->float:
    df = df2grid(df)

    #handle that df is not square for final input
    if df.shape[0]!=df.shape[1]:
        df = df.append(pd.DataFrame('.', columns = df.columns, index = [max(df.index)+1]))

    Maxitt = 1000
    for ii in range(Maxitt):
        if round(ii/10) == ii/10:
            print(ii)
        df_next = df.copy()
        for x in itertools.product(list(df.index), list(df.columns)):
            if df.iloc[x] == '.':
                continue
            else:
                xn_list = get_neighbor_idx(x,df)
                nn = ''
                for xn_i in xn_list:
                    nn+=df.iloc[xn_i]
                if df.iloc[x] == 'L' and nn.count('#')==0:
                    df_next.iloc[x] = '#'
                elif df.iloc[x] == '#' and nn.count('#')>=4:
                    df_next.iloc[x] = 'L'
            
        #check for convergence
        if df.equals(df_next):
            break

        # update
        df = df_next.copy()

    print(ii)
    return (df=='#').sum().sum()


def get_answer2(df: pd.DataFrame)->float:
    df = df2grid(df)

    #handle that df is not square for final input
    if df.shape[0]!=df.shape[1]:
        df = df.append(pd.DataFrame('.', columns = df.columns, index = [max(df.index)+1]))

    Maxitt = 1000
    for ii in range(Maxitt):
        if round(ii/10) == ii/10:
            print(ii)
        df_next = df.copy()
        for x in itertools.product(list(df.index), list(df.columns)):
            if df.iloc[x] == '.':
                continue
            else:
                xn_list = get_neighbor_idx(x,df)
                nn = ''
                for xn_i in xn_list:
                    nn+=df.iloc[xn_i]
                if df.iloc[x] == 'L' and nn.count('#')==0:
                    df_next.iloc[x] = '#'
                elif df.iloc[x] == '#' and nn.count('#')>=4:
                    df_next.iloc[x] = 'L'
            
        #check for convergence
        if df.equals(df_next):
            break

        # update
        df = df_next.copy()

    print(ii)
    return (df=='#').sum().sum()


if __name__ == "__main__":
    df = read_csv('data/2020/day11.csv', col_names=['XX'], sep=',')
    df = read_csv('test/2020/data/day11.csv', col_names=['XX'], sep=',')
    answer1 = get_answer1(df)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df)
    print(f'Todays second answer is: {answer2}')    
