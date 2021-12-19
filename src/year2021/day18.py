from utils.utils import read_csv
import pandas as pd
import json
import numpy as np
import re


def add(l1, l2):
    #print(f' adding to {[l1, l2]}')
    return [l1, l2]


def explode(l:list)->float:
    lstr = str(l)
    lstr_new = lstr
    while True:
        ##print(lstr)
        # find first depth 4 element
        count_open = 0
        for i, c in enumerate(lstr):
            if c == '[':
                count_open +=1
            elif c == ']':
                count_open-=1
            if count_open==5:
                d4_start_idx = i
                break
        # if we found no elements of depth 4:
        if i == len(lstr)-1:
            break
        
        d4_str = '[' + lstr[d4_start_idx+1:].split(']')[0] + ']'
        d4_list = json.loads(d4_str)
        d4_end_idx = int(d4_start_idx + len(d4_str))
        # add to nearest element to the right
        lstr_right = lstr[d4_end_idx:]
        all_digits_right = re.findall(r'\d+',lstr_right)
        if len(all_digits_right)>0:
            first_right = all_digits_right[0]
            lstr_right = lstr_right.replace(first_right, str(int(first_right)+d4_list[1]),1)
        # add to nearest element to the left
        lstr_left = lstr[:d4_start_idx]
        all_digits_left = re.findall(r'\d+',lstr_left)
        if len(all_digits_left)>0:
            last_left = all_digits_left[-1]
            lstr_left = lstr_left[::-1]
            lstr_left = lstr_left.replace(last_left[::-1], str(int(last_left)+d4_list[0])[::-1], 1)    
            lstr_left = lstr_left[::-1]

        lstr_new = lstr_left + '0' + lstr_right

        #update
        lstr = lstr_new
        #print(f' exploding to {json.loads(lstr)}')
        
    return json.loads(lstr)


def split(l):
    lstr = str(l)
    digits_to_split = [a for a in re.findall(r'\d+',lstr) if int(a) >9]
    if len(digits_to_split)==0: 
        return json.loads(lstr)
    d = digits_to_split[0]
    new_val = str([int(np.floor(int(d)/2)), int(np.ceil(int(d)/2))])
    lstr = lstr.replace(d,new_val,1)
    #print(f' splitting to {json.loads(lstr)}')

    return json.loads(lstr)


def reduce(l):
    while True:
        lnew1 = explode(l)
        lnew2 = split(lnew1)
        if lnew2 == l: 
            break
        l = lnew2
    return l


def get_magnitude(l):
    if type(l) == int: 
        return l
    else:
        return 3*get_magnitude(l[0]) + 2*get_magnitude(l[1])


def get_answer1(dl):
    lreduced = json.loads(dl[0])
    for ll in dl[1:]:
        l = json.loads(ll)
        print(f'{lreduced} + {l}')
        lreduced = add(lreduced, l)
        lreduced = reduce(lreduced)
        print(lreduced)
        print(' ')

    # get magnitude
    score = get_magnitude(lreduced)
    return score


def get_answer2(dl):
    score = 0
    #loop over all combinations
    for ix in range(len(dl)):
        lx = json.loads(dl[ix])
        for iy in range(len(dl)):
            if ix == iy:
                continue
            ly = json.loads(dl[iy])
            lreduced = add(lx, ly)
            lreduced = reduce(lreduced)
            # get magnitude
            scorei = get_magnitude(lreduced)
            score = max(score, scorei)
    return score


if __name__ == "__main__":
    dl = open('data/2021/day18.csv').read().splitlines()

    answer1 = get_answer1(dl)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(dl)
    print(f'Todays second answer is: {answer2}')    
