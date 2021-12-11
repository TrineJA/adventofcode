from utils.utils import read_csv
import pandas as pd
import numpy as np


def key_from_value(mydict: dict, val: int)->str:
    for ikey, ival in mydict.items():
        if ival == val:
            return ikey


def get_answer1(df: pd.DataFrame)->float:
    lens_to_find = [2,3,4,7]
    found_digits = []
    for idx, row in df.iterrows():
        shown_list = row.shown.strip().split(' ')
        found_digits += [x for x in shown_list if len(x) in lens_to_find]
    return len(found_digits)


def get_answer2(df: pd.DataFrame)->float:
    sum_of_shown_digits = 0
    for idx, row in df.iterrows():
        shown_list = row.shown.strip().split(' ')
        shown_list = [''.join(sorted(x)) for x in shown_list]
        digit_keys = row['all'].strip().split(' ')
        digit_keys = [''.join(sorted(x)) for x in digit_keys]
        digit_dict = dict.fromkeys(digit_keys, np.nan)
        # find 1
        key1 = [x for x in digit_dict.keys() if len(x)==2][0]
        digit_dict[key1]=1
        # find 7
        key7 = [x for x in digit_dict.keys() if len(x)==3][0]
        digit_dict[key7]=7
        # find 4
        key4 = [x for x in digit_dict.keys() if len(x)==4][0]
        digit_dict[key4]=4
        # find 8
        key8 = [x for x in digit_dict.keys() if len(x)==7][0]
        digit_dict[key8]=8
        # find 3 (length 5 and contains 7)
        key_length5 = [x for x in digit_dict.keys() if len(x)==5]
        key3 = [x for x in key_length5 if all(y in x for y in list(key7))][0]
        digit_dict[key3]=3
        # find 5 (length 5 and contains [(in 3 not in 1) + (in 4 not in 3)])
        list_3_not_1 = [x for x in key3 if not x in key1]
        list_4_not_3 = [x for x in key4 if not x in key3]
        key5 = [x for x in key_length5 if all(y in x for y in list_3_not_1 + list_4_not_3)][0]
        digit_dict[key5]=5
        # find 9 (length 6 and contains 4)
        key_length6 = [x for x in digit_dict.keys() if len(x)==6]
        key9 = [x for x in key_length6 if all(y in x for y in list(key4))][0]
        digit_dict[key9]=9
        # find 6 (length 6 and contains 5 and is not 9)
        key6 = [x for x in key_length6 if all(y in x for y in list(key5))]
        key6.remove(key9)
        key6 = key6[0]
        digit_dict[key6]=6
        # remainig keys: len(key)=6->0, len(key)=5->2 
        for ikey, ival in digit_dict.items():
            if np.isnan(ival):
                if len(ikey)==6:
                    digit_dict[ikey] = 0
                elif len(ikey)==5:
                    digit_dict[ikey] = 2
        
        # get value of show digits
        shown_digits = ''.join([str(digit_dict[x]) for x in shown_list])
        # add to running sum
        sum_of_shown_digits += int(shown_digits)

    return sum_of_shown_digits

if __name__ == "__main__":
    df = read_csv('data/2021/day8.csv', col_names=['all','shown'], sep='|')
    answer1 = get_answer1(df)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df)
    print(f'Todays second answer is: {answer2}')    
