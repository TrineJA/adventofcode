from utils.utils import read_csv
import pandas as pd
from random import choices
import heapq
from itertools import product
import time
from collections import Counter


def throw_die1(Nrolls, Nthrow):
    res0 = range(Nrolls, Nrolls+Nthrow)
    res = []
    for r in res0:
        r = r%100
        if r==0:
            r=100
        res.append(r)
    if min(res)<1 or max(res)>100:
        raise ValueError(f'thrown dices not valid: {res} ({res0} - {Nrolls})')
    print(f' rolls: {res}')
    return sum(res)


def move(space, Nstep):
    new_space = space + Nstep
    new_space = new_space%10
    if new_space == 0:
        new_space=10
    return new_space


def get_answer2(dl: list)->float:
    t = time.time()
    spaces = []
    for l in dl:
        spaces.append(int(l.split(' ')[-1]))
    scores = len(spaces)*[0]
    wins = [0,0,0]
    game_state = [tuple([0] + scores + spaces + [1])]
    # get list of all possible dice throws for both players
    all_possible_3_rolls = list(product([1,2,3], [1,2,3], [1,2,3]))
    all_poosible_3_rolls_2_players = list(product(all_possible_3_rolls, all_possible_3_rolls))
    #these are not unique in sum fo 3 throws (49 unique sum combinations)
    sum_of_rolls = []
    for rolls in all_poosible_3_rolls_2_players:
        sum_of_rolls.append((sum(rolls[0]), sum(rolls[1])))
    sum_of_3rolls_all_combs= list(Counter(sum_of_rolls).keys())
    sum_of_3rolls_n = list(Counter(sum_of_rolls).values())
    sum_of_3rolls_combs_and_n = []
    for i, ss in enumerate(sum_of_3rolls_all_combs):
        sum_of_3rolls_combs_and_n.append(ss + (sum_of_3rolls_n[i],))

    while game_state:
        neg_maxscore, score0, score1, space0, space1, ngames = heapq.heappop(game_state)
        #heap pops according to lowest value of first entry. 
        #ensures we play the game closest to finishing. keeping the heap small-ish

        # in each loop both players will play.
        for roll_comb in sum_of_3rolls_combs_and_n:
        #for roll in all_poosible_3_rolls_2_players:
            #roll_comb = (sum(roll[0]), sum(roll[1]))
            new_space0 = move(space0, roll_comb[0])
            new_space1 = move(space1, roll_comb[1])
            new_score0 = score0 + new_space0
            new_score1 = score1 + new_space1
            new_neg_maxscore = -max(new_score0, new_score1)
            new_ngames = ngames * roll_comb[2]
            #new_ngames = 1

            # if both players are above 21. then player 1 (here index0) wins
            if new_score0 >= 21:
                wins[0] = wins[0]+new_ngames
            elif new_score1 >= 21:
                wins[1] = wins[1]+new_ngames
            else: 
                # add game bag to heap
                heapq.heappush(game_state, (new_neg_maxscore, new_score0, new_score1, new_space0, new_space1, new_ngames))

    elapsed_sec = time.time() - t
    print(f'time spent[sec]: {round(elapsed_sec)}')
    print(f'wins: {wins}')
    print(f'length of heap (unfinished games): {len(game_state)}')
    return max(wins)



def get_answer1(dl: list)->float:
    spaces = []
    for l in dl:
        spaces.append(int(l.split(' ')[-1]))
    scores = len(spaces)*[0]
    Nrolls = 1
    while True:
        for player, space in enumerate(spaces):
            print(f'player: {player+1}')
            print(f' Nrolls: {Nrolls}')
            Nsteps = throw_die1(Nrolls, 3)
            Nrolls += 3
            new_space = move(space, Nsteps)
            spaces[player] = new_space
            scores[player] += new_space
            print(f' moves to: {spaces[player]}')
            print(f' total score: {scores[player]}')
            if new_space<1 or new_space>10:
                raise ValueError(f'New space not valid: {new_space} ({player} - {space} - {Nrolls})')

            if max(scores)>=1000:
                print(Nrolls)
                return min(scores)*(Nrolls-1)

if __name__ == "__main__":
    dl = open('data/2021/day21.csv').read().splitlines()
    dl = open('test/2021/data/day21.csv').read().splitlines()

    #answer1 = get_answer1(dl)
    #print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(dl)
    print(f'Todays second answer is: {answer2}')    
