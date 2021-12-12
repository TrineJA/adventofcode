from os import path
from utils.utils import read_csv
import pandas as pd
import numpy as np
import random


def remove_dead_ends(d):
    dout = d.copy()
    for key, val in d.items():
        if len(val)==1 and val==[x.lower() for x in val]:
            dout.pop(key)
            dout[val[0]].remove(key)
    return dout


def cave_dict(df):
    # you cannot leave 'end' or enter 'start'
    all_caves = list(np.unique(list(df['f'].unique()) + list(df['t'].unique())))
    all_caves.remove('end')
    d = dict()
    for from_cave in all_caves:
        to_caves = list(set(list(df[df['f']==from_cave]['t']) + list(df[df['t']==from_cave]['f'])))
        to_caves = [x for x in to_caves if x!='start']
        d[from_cave] = to_caves
    return d


def score_path(p):
    return 1


def is_step_valid(p, nc):
    valid = True
    if nc.islower() and nc in p:
        valid = False
    return valid


def is_step_valid2(p, nc):
    valid = True
    if nc.islower():
        prev_lower = [x for x in p.split(',') if x.islower()]
        #if we alreay has a lowercase that was visited twice, then you cannot go
        has_double_visit = len(prev_lower) != len(set(prev_lower))
        if has_double_visit and nc in p:
            valid = False
    return valid


def get_answer1(df: pd.DataFrame)->float:
    # remove dead-ends
    cave_map = cave_dict(df)
    cave_map = remove_dead_ends(cave_map)

    #initialize
    Nstep = 100
    paths = ['start']
    Nscore = 0
    for ii in range(Nstep):
        paths_next = paths.copy()
        for idx, p in enumerate(paths):
            last_cave = p.split(',')[-1]
            # if at end: evaluate score
            if last_cave == 'end':
                Nscore += score_path(p)
            else:
                nextcave = cave_map[last_cave]
                for nc in nextcave:
                    # is this a valid path?
                    if is_step_valid(p, nc):
                        paths_next.append(p+','+nc)
            paths_next.remove(p)
        #update
        if len(paths_next)==0:
            break
        else:
            paths = paths_next.copy()
    print(ii)
    return Nscore


def get_answer2(df: pd.DataFrame)->float:
    # remove dead-ends
    cave_map = cave_dict(df)

    #initialize
    Nstep = 100
    paths = ['start']
    Nscore = 0
    for ii in range(Nstep):
        paths_next = paths.copy()
        for idx, p in enumerate(paths):
            last_cave = p.split(',')[-1]
            # if at end: evaluate score
            if last_cave == 'end':
                Nscore += score_path(p)
            else:
                nextcave = cave_map[last_cave]
                for nc in nextcave:
                    # is this a valid path?
                    if is_step_valid2(p, nc):
                        paths_next.append(p+','+nc)
            paths_next.remove(p)
        #update
        if len(paths_next)==0:
            break
        else:
            paths = paths_next.copy()
    print(ii)
    return Nscore


if __name__ == "__main__":
    df = read_csv('data/2021/day12.csv', col_names=['f','t'], sep='-')
    #df = read_csv('test/2021/data/day12.csv', col_names=['f','t'], sep='-')
    answer1 = get_answer1(df)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df)
    print(f'Todays second answer is: {answer2}')    
