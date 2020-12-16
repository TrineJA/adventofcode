from utils.load_data import read_csv
import pandas as pd
from itertools import product

def check_if_sum_exists(input_list, sum_val):
    # brute force. just loop through
    for val1 in input_list:
        cal_sum = val1


def find_invalid_number(df: pd.DataFrame, preamble_length: int)->float:
    input_list = df.xmas[0:preamble_length].tolist()
    # step through input
    for find_this_sum in df.xmas[preamble_length:]:
        combos_to_check = list(product(input_list, input_list))
        itt = 0
        # check of this value is the sum of 2 elements in the input list
        for a,b in combos_to_check:
            itt+=1  
            # do this elements sum to what we are looking for? then move to next item in df.xmas
            if a!=b and find_this_sum == a + b:
                # Update input_list
                input_list = input_list[1:] + [find_this_sum]
                break
            if itt == len(combos_to_check):
                # if we get to here. then find_this_sum was not found!
                return find_this_sum
        

def sum_next_elements(df, start_idx, sumval):
    contiguous_sum = df.loc[start_idx,'xmas']
    for end_idx in range(start_idx+1,len(df)):
        contiguous_sum+=df.loc[end_idx,'xmas']
        if contiguous_sum >= sumval:
            break
    return contiguous_sum, end_idx


def find_contiguous_list(df, sumval):
    for start_idx in range(len(df)):
        contiguous_sum, end_idx = sum_next_elements(df, start_idx, sumval)
        if contiguous_sum == sumval:
            # i found the list
            output_list = df.loc[start_idx:end_idx,'xmas'].tolist()
            break
    return output_list


def get_answer1(df: pd.DataFrame, preamble_length: int)->float:
    invalid_number = find_invalid_number(df, preamble_length)
    return invalid_number


def get_answer2(df: pd.DataFrame, preamble_length: int)->float:
    invalid_number = find_invalid_number(df, preamble_length)
    contiguous_list = find_contiguous_list(df, invalid_number)
    answer = min(contiguous_list) + max(contiguous_list)
    return answer



if __name__ == "__main__":
    df = read_csv('data/day9.csv', col_names=['xmas'], sep=',')
    answer1 = get_answer1(df, 25)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df, 25)
    print(f'Todays second answer is: {answer2}')    
