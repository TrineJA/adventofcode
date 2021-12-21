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
    wins = [0,0]
    game_state = [tuple([0] + scores + spaces + [0] + [1])] # neg_maxscore, score0, score1, space0, space1, player, ngames
    # get list of all possible dice throws (27)
    all_possible_3_rolls = list(product([1,2,3], [1,2,3], [1,2,3]))
    #these are not unique in sum fo 3 throws (49 unique sum combinations)
    sum_of_rolls = [sum(x) for x in all_possible_3_rolls]
    sum_of_rolls_unique= list(Counter(sum_of_rolls).keys())
    sum_of_rolls_n = list(Counter(sum_of_rolls).values())
    sum_of_rolls_combs_and_n = []
    for i, ss in enumerate(sum_of_rolls_unique):
        sum_of_rolls_combs_and_n.append((ss, sum_of_rolls_n[i]))

    while game_state:
        neg_maxscore, score0, score1, space0, space1, player, ngames = heapq.heappop(game_state)
        #print(f'gamestate: {(neg_maxscore, score0, score1, space0, space1, ngames)}')
        #heap pops according to lowest value of first entry. 
        #ensures we play the game closest to finishing. keeping the heap small

        # in each loop both players will play.
        for roll_comb in sum_of_rolls_combs_and_n:
            new_ngames = ngames * roll_comb[1]
            #print(f' looking at {roll_comb}')
            if player == 0:
                new_space0 = move(space0, roll_comb[0])
                if new_space0<1 or new_space0>10:
                    raise ValueError(f'New space 0 not valid: {new_space0} ({space0} - {roll_comb[0]})')
                new_score0 = score0 + new_space0
                if new_score0 >= 21:
                    wins[0] = wins[0]+new_ngames
                else:
                    # add game back to heap
                    new_player = 1
                    new_neg_maxscore = -max(new_score0, score1)
                    assert new_neg_maxscore>-21
                    heapq.heappush(game_state, (new_neg_maxscore, new_score0, score1, new_space0, space1, new_player, new_ngames))
            elif player == 1:
                new_space1 = move(space1, roll_comb[0])
                if new_space1<1 or new_space1>10:
                    raise ValueError(f'New space 0 not valid: {new_space1} ({space1} - {roll_comb[1]})')
                new_score1 = score1 + new_space1
                if new_score1 >= 21:
                    wins[1] = wins[1]+new_ngames
                else: 
                    # add game back to heap
                    new_player = 0
                    new_neg_maxscore = -max(score0, new_score1)
                    assert new_neg_maxscore>-21
                    heapq.heappush(game_state, (new_neg_maxscore, score0, new_score1, space0, new_space1, new_player, new_ngames))
            else:
                raise ValueError(f'Player is not valid: {player}')
            #print(f' new gamestate" {(new_neg_maxscore, new_score0, new_score1, new_space0, new_space1, new_ngames)}')

    print(f'wins: {wins}')
    print(f'length of heap (unfinished game states): {len(game_state)}')
        
    elapsed_sec = time.time() - t
    print(f'time spent[sec]: {round(elapsed_sec)}')

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

    answer1 = get_answer1(dl)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(dl)
    print(f'Todays second answer is: {answer2}')    
