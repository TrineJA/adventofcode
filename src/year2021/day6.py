import csv
import pandas as pd
import numpy as np

def get_answer1(init_state_list: list)->float:
    period_restart = 6
    period_restart_first = 8
    Ndays = 80
    fish_timer_list = init_state_list

    for ii in range(Ndays):
        # subtract 1 day from timer
        fish_timer_list = [x - 1 for x in fish_timer_list]
        # did fish reproduce
        if min(fish_timer_list) < 0:
            # add new fish
            Nnew = fish_timer_list.count(-1)            
            fish_timer_list = fish_timer_list + Nnew*[period_restart_first]
            # reset timer for fish that reproduced
            fish_timer_list = [period_restart if x==-1 else x for x in fish_timer_list]

    Nfish = len(fish_timer_list)
    return Nfish


def get_answer2(init_state_list: list)->float:
    period_restart = 6
    period_restart_first = 8
    Ndays = 256
    fish_timer_df = pd.DataFrame(0,index=np.arange(-1,period_restart_first+1),columns=['Nfish'])
    for idx in range(0,period_restart_first):
        fish_timer_df.iloc[idx+1] = init_state_list.count(idx)

    for ii in range(Ndays):
        # subtract 1 day from timer
        fish_timer_df = fish_timer_df.shift(-1).fillna(0)
        # did fish reproduce
        if fish_timer_df.loc[-1,'Nfish'] > 0:
            # add new fish
            fish_timer_df.loc[period_restart_first,'Nfish'] = fish_timer_df.loc[-1,'Nfish']
            # reset timer for fish that reproduced
            fish_timer_df.loc[period_restart,'Nfish'] += fish_timer_df.loc[-1,'Nfish'] 
            fish_timer_df.loc[-1,'Nfish'] = 0

    Nfish = int(fish_timer_df.sum().values[0])
    return Nfish


if __name__ == "__main__":
    with open('data/2021/day6.csv') as f:
        reader = csv.reader(f)
        init_state_list = list(reader)[0]
    init_state_list = list(map(int, init_state_list))

    answer1 = get_answer1(init_state_list)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(init_state_list)
    print(f'Todays second answer is: {answer2}')    
