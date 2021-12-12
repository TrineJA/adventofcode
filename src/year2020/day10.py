import pandas as pd
import numpy as np


def make_dict_for_paths(dl):
    d = dict()
    for ii in range(len(dl)+1):
        d[ii+1] = []
    return d

def get_answer1(dl:list)->float:
    dl = list(map(int,dl))
    dl.append(3 + max(dl))
    dl.append(0)
    ol= sorted(dl)
    step = list(np.diff(ol))
    score = step.count(1) * step.count(3)
    return score


def get_answer2(dl: list)->int:
    dl = list(map(int,dl))
    endstate = max(dl)+3
    dl.append(0)
    dl.append(endstate)
    dl = sorted(dl)
    
    #initialize
    state = dict()
    for ii in dl:
        state[ii] = 0
    state[0] = 1

    for val in dl:
        valid_next = [x for x in dl if x<=val+3 and x>val]
        for next_state in valid_next:
            state[next_state] += state[val]
    
    return state[endstate]


if __name__ == "__main__":
    dl = open('data/2020/day10.csv').read().splitlines()
    answer1 = get_answer1(dl)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(dl)
    print(f'Todays second answer is: {answer2}')    
