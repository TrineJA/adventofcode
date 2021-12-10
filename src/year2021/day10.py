from utils.load_data import read_csv
import pandas as pd
import re
import numpy as np

def calculate_score(char):
    if char == ')':
        score = 3
    elif char == ']':
        score = 57
    elif char == '}':
        score = 1197
    elif char == '>':
        score = 25137
    else:
        score = 0
    return score


def calculate_score2(missing_closes):
    score = 0
    for char in missing_closes:
        score = score * 5
        if char == ')':
            score += 1
        elif char == ']':
            score += 2
        elif char == '}':
            score += 3
        elif char == '>':
            score += 4
        else:
            score += 0
    return score
    

def get_answer1(df: pd.DataFrame)->float:
    score = 0
    for idx, row in df.iterrows():   
        # order needs to match between open and close
        open_chars = '{<[('
        close_chars = '}>])'
        currently_open = ''
        for char in row.XX:
            if char in open_chars:
                currently_open += char
            elif char in close_chars:
                #find corresponding open char
                char_idx = close_chars.index(char)
                correct_open = open_chars[char_idx]
                # if this closure matches last open. then delete the open from the list and continue
                if currently_open[-1]== correct_open:
                    currently_open = currently_open[:-1]
                else:
                    score += calculate_score(char)
                    break
    return score


def get_answer2(df: pd.DataFrame)->float:
    # order needs to match between open and close
    open_chars = '{<[('
    close_chars = '}>])'
    score_list = []
    for idx, row in df.iterrows():   
        currently_open = ''
        is_corrupted = False
        # check for corruption/incomplete
        for char in row.XX:
            if char in open_chars:
                currently_open += char
            elif char in close_chars:
                #find corresponding open char
                char_idx = close_chars.index(char)
                correct_open = open_chars[char_idx]
                # if this closure matches last open. then delete the open from the list and continue
                if currently_open[-1]== correct_open:
                    currently_open = currently_open[:-1]
                else:
                    is_corrupted = True
                    break
        #if we made it to here without breaking. then the row is not corrupted
        if not is_corrupted:
            missing_closes = ''
            for char in reversed(currently_open):
                char_idx = open_chars.index(char)
                missing_closes += close_chars[char_idx]
            score_list.append(calculate_score2(missing_closes))
    return int(np.median(score_list))


if __name__ == "__main__":
    df = read_csv('data/2021/day10.csv', col_names=['XX'], sep=',')
    answer1 = get_answer1(df)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df)
    print(f'Todays second answer is: {answer2}')    
