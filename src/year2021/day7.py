import csv
import pandas as pd
import numpy as np


def get_answer1(pos_list: list)->int:
    # init guess
    optimal_position = np.floor(np.mean(pos_list))
    fuel_needed = sum([abs(x-optimal_position) for x in pos_list])
    maxitt = 1000
    for i in range(maxitt):
        #Fixme: make larger steps
        position_candidate = optimal_position + 1
        fuel_needed_candidate = sum([abs(x-position_candidate) for x in pos_list])
        position_candidate2 = optimal_position - 1
        fuel_needed_candidate2 = sum([abs(x-position_candidate2) for x in pos_list])
        #check above
        if fuel_needed_candidate <= fuel_needed:
            fuel_needed = fuel_needed_candidate
            optimal_position = position_candidate
            continue
        #check below
        elif fuel_needed_candidate2 <= fuel_needed:
            fuel_needed = fuel_needed_candidate2
            optimal_position = position_candidate2
            continue
        else:
            break
    return int(fuel_needed)

def get_answer2(pos_list: list)->float:
    # init guess
    optimal_position = int(np.floor(np.mean(pos_list)))
    fuel_needed = sum([sum(range(0,abs(x-optimal_position)+1)) for x in pos_list])
    maxitt = 1000
    for i in range(maxitt):
        #Fixme: make larger steps
        position_candidate = optimal_position + 1
        fuel_needed_candidate = sum([sum(range(0,abs(x-position_candidate)+1)) for x in pos_list])
        position_candidate2 = optimal_position - 1
        fuel_needed_candidate2 = sum([sum(range(0,abs(x-position_candidate2)+1)) for x in pos_list])
        #check above
        if fuel_needed_candidate <= fuel_needed:
            fuel_needed = fuel_needed_candidate
            optimal_position = position_candidate
            continue
        #check below
        elif fuel_needed_candidate2 <= fuel_needed:
            fuel_needed = fuel_needed_candidate2
            optimal_position = position_candidate2
            continue
        else:
            break
    return int(fuel_needed)


if __name__ == "__main__":
    with open('data/2021/day7.csv') as f:
        reader = csv.reader(f)
        pos_list = list(reader)[0]
    pos_list = list(map(int, pos_list))

    answer1 = get_answer1(pos_list)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(pos_list)
    print(f'Todays second answer is: {answer2}')    
