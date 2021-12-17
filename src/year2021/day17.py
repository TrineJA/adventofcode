from utils.utils import read_csv
import pandas as pd
import numpy as np 


def aim_at_target(vel:list, target:list):
    pos = [0,0] # x, y
    inTarget = False
    max_height = 0
    while True:
        pos = [ai + bi for ai, bi in zip(pos,vel)]
        vel[0] = max(vel[0]-1,0)
        vel[1] += -1
        max_height = max(max_height, pos[1])
        if pos[0] in range(target[0][0],target[0][1]+1) and pos[1] in range(target[1][0],target[1][1]+1):
            inTarget = True
            break
        elif pos[0] > max(target[0]) or pos[1]<min(target[1]):
            break
    return inTarget, pos, max_height


def get_answer(dl: list)->float:
    #get target from input
    target_str = dl[0].replace('target area: ','')
    foo = target_str.split(', ')
    target=[]
    for dir in foo:
        target.append([int(a) for a in dir.split('=')[1].split('..')])

    #define velocity range to explore:
    for xmin in range(10):
        xdist = sum(list(range(xmin+1)))  
        if xdist >= target[0][0]: break
    xmax = 1000
    ymin = -150
    ymax = 1000
    #loop over start velocities
    max_height = -np.inf
    vel0_hits_target = []
    for x in range(xmin, xmax):
        for y in range(ymin, ymax):
            inTarget, pos, max_height_i = aim_at_target([x,y], target)
            if inTarget:
                vel0_hits_target.append([x,y])
                if max_height_i > max_height:
                    max_height = max_height_i
    Nhitstarget = len(vel0_hits_target)
    return max_height, Nhitstarget


if __name__ == "__main__":
    dl = open('data/2021/day17.csv').read().splitlines()
    answer = get_answer(dl)
    print(f'Todays first answer is: {answer[0]}')
    print(f'Todays second answer is: {answer[1]}')    
