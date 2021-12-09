from utils.load_data import read_csv
import pandas as pd
import csv

def split_boards_in_list(df, board_size):
    #split in boards
    list_of_df = [df.loc[i:i+board_size-1,:] for i in range(0, len(df),board_size)]
    return list_of_df

def check_for_bingo(df_is_called, board_size):
    bingo_board_idx = []

    # split boards and check each
    list_of_df = split_boards_in_list(df_is_called, board_size)
    for idx, df in enumerate(list_of_df):
        max_called_for_col = df.sum(axis=0).max()
        max_called_for_row = df.sum(axis=1).max()
        # bingo
        if (max_called_for_col == board_size) | (max_called_for_row == board_size):
            bingo_board_idx.append(idx)

    return bingo_board_idx
    

def get_answer1(df_boards: pd.DataFrame, call_list: list)->float:
    #init
    board_size = 5
    df_is_called = df_boards < 0

    for val in call_list:
        df_is_called = (df_is_called) | (df_boards == val)
        bingo_board_idx = check_for_bingo(df_is_called, board_size)

        # if we have bingo
        if len(bingo_board_idx)>0:
            # get board with bingo
            list_of_boards = split_boards_in_list(df_boards, board_size)
            list_of_calls = split_boards_in_list(df_is_called, board_size)
            bingo_board = list_of_boards[bingo_board_idx[0]]
            bingo_calls = list_of_calls[bingo_board_idx[0]]

            score = bingo_board[-bingo_calls].sum().sum() * val
            break
        
    return score


def get_answer2(df_boards: pd.DataFrame, call_list: list)->float:
    #init
    board_size = 5
    df_is_called = df_boards < 0
    calc_score = False

    for val in call_list:
        df_is_called = (df_is_called) | (df_boards == val)

        # find bingo boards
        list_of_called = split_boards_in_list(df_is_called, board_size)
        list_of_boards = split_boards_in_list(df_boards, board_size)
        # if we only have 1 board left. then calcualte score when bingo
        if len(list_of_boards)==1:
            calc_score = True

        # check for bingo
        idx_to_pop = []
        for idx, df in enumerate(list_of_called):
            max_called_for_col = df.sum(axis=0).max()
            max_called_for_row = df.sum(axis=1).max()
            # bingo
            if (max_called_for_col == board_size) | (max_called_for_row == board_size):
                idx_to_pop.append(idx)
        
        # if this was the last board then calculate score. otherwise remove bingo boards
        if len(idx_to_pop)>0 and (calc_score):
            score = df_boards[-df_is_called].sum().sum() * val
            break
        elif len(idx_to_pop)>0:
            #remove all bingo boards
            for del_idx in sorted(idx_to_pop, reverse=True):
                del list_of_boards[del_idx]
                del list_of_called[del_idx]

        # make list of dfs to 1 df to re-iterate. Dumb.
        df_boards = pd.concat(list_of_boards).reset_index(drop=True)
        df_is_called = pd.concat(list_of_called).reset_index(drop=True)
        
    return score


if __name__ == "__main__":
    df_boards = pd.read_csv('data/2021/day4.csv', delim_whitespace=True, skiprows=[0],  names=['x1','x2','x3','x4','x5'])
    with open('data/2021/day4.csv') as f:
        reader = csv.reader(f)
        call_list = next(reader)
    call_list = list(map(int, call_list))

    answer1 = get_answer1(df_boards, call_list)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df_boards, call_list)
    print(f'Todays second answer is: {answer2}')    
