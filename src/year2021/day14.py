from utils.utils import read_csv
import pandas as pd
from collections import Counter


def get_answer1(dl:list, Nstep:int)->float:
    p = dl[0]
    pnew = p[0]
    ins_list = dl[2:]
    
    # make insertion dict
    ins_dict = dict()
    for kv in ins_list:
        foo = kv.split(' -> ')
        ins_dict.update({foo[0]:foo[1]})
    
    for n in range(Nstep):
        for idx in range(len(p)-1):
            ppair = p[idx:idx+2]

            if ppair in ins_dict:
                insertion = ins_dict[ppair]
            else:
                insertion = '' 
            pnew += (insertion + ppair[1])
        
        #udpate
        p = pnew
        pnew = p[0]

    #get score
    freq_count = Counter(p).most_common()
    return freq_count[0][1] - freq_count[-1][1]


def get_answer2(dl:list, Nstep:int)->float:
    p = dl[0]
    ins_list = dl[2:]
    
    # make insertion dict
    ins_dict = dict()
    for kv in ins_list:
        foo = kv.split(' -> ')
        ins_dict.update({foo[0]:foo[1]})

    #make polymer dict
    p_dict = dict()
    for idx in range(len(p)-1):
        ppair = p[idx:idx+2]
        if ppair in p_dict:
            p_dict[ppair] +=1
        else:
            p_dict.update({ppair: 1})
    
    for n in range(Nstep):
        p_dict_new = p_dict.copy()
        for ppair,v in p_dict.items():
            #insert
            if ppair in ins_dict:
                insertion = ins_dict[ppair]
                ppair_new = [ppair[0]+insertion, insertion+ppair[1]]
                for pn in ppair_new:
                    if pn in p_dict_new:
                        p_dict_new[pn]+=v
                    else :
                        p_dict_new.update({pn: v})
                #remove ppair
                p_dict_new[ppair]-=v

        #udpate
        p_dict = {key: p_dict_new[key] for key in p_dict_new if p_dict_new[key] > 0}

    #get score
    score_dict = dict()
    for k, v in p_dict.items():
            for letter in k:
                if letter in score_dict:
                    score_dict[letter] += v
                else:
                    score_dict.update({letter: v})
    # add first and last
    score_dict[p[0]]+=1
    score_dict[p[-1]]+=1
    count_max = score_dict[max(score_dict, key=score_dict.get)]/2
    count_min = score_dict[min(score_dict, key=score_dict.get)]/2

    return int(count_max - count_min)

if __name__ == "__main__":
    dl = open('data/2021/day14.csv').read().splitlines()

    answer1 = get_answer1(dl,10)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(dl,40)
    print(f'Todays second answer is: {answer2}')    
