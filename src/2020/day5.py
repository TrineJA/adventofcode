from utils.utils import read_csv
import pandas as pd
from typing import List
import itertools


def split_list_in_half(ll: List, half_to_keep:str):
    midpoint = len(ll)//2
    if half_to_keep in ['F','L']:
        selected_list = ll[:midpoint]
    elif half_to_keep in ['B','R']:
        selected_list = ll[midpoint:]
    else:
        raise ValueError('half_to_keep svan take F,L,B,R')
    return selected_list


def get_all_seat_ids(boardingpass_list: List)->List:
    seat_ids = []
    for bp in boardingpass_list:
        # initalize list of column and rows
        row_id = list(range(0,128))
        col_id = list(range(0,8))
        # get row number
        for selected_half in bp[:7]:
            row_id = split_list_in_half(row_id, selected_half)
        # get col number
        for selected_half in bp[7:]:
            col_id = split_list_in_half(col_id, selected_half)
        # calculate seat id
        current_seat_id = 8 * row_id[0] + col_id[0]
        seat_ids.append(current_seat_id)
    return seat_ids


def get_answer1(boardingpass_list: List)->float:
    # get all seat-ids
    seat_ids = get_all_seat_ids(boardingpass_list)
    #get highest seat-id
    max_seat_id = max(seat_ids)
    return max_seat_id


def get_answer2(df: pd.DataFrame)->float:
    # get all possible seat ids
    possible_seats = []
    all_row_and_col_id_combos = list(itertools.product(list(range(0,128)), list(range(0,8))))
    for row_col_id in all_row_and_col_id_combos:
        possible_seats.append(8 * row_col_id[0] + row_col_id[1])
    # okay this is of course range(0,128*8)

    # get existing seat ids
    filled_seats = get_all_seat_ids(boardingpass_list)

    # find empty seats
    empty_seats = list(set(possible_seats) - set(filled_seats))

    # find my seat
    for seat in empty_seats:
        # if seat before and after are not empty. then this is my seat
        if (seat-1 not in empty_seats) and (seat+1 not in empty_seats):
            my_seat = seat
    return my_seat


if __name__ == "__main__":
    df = read_csv('data/day5.csv', col_names=['boardingpass'])
    boardingpass_list = df.boardingpass.tolist()

    answer1 = get_answer1(boardingpass_list)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(boardingpass_list)
    print(f'Todays second answer is: {answer2}')    
