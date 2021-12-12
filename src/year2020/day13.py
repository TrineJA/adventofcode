from utils.utils import read_csv
import pandas as pd
import numpy as np
from operator import itemgetter


def get_answer1(dl)->float:
    start = int(dl[0])
    busses = sorted([float(b) for b in dl[1].split(',') if b!='x'])
    first_valid = []
    for bus in busses:
        fact = np.ceil(start/bus)
        first_valid.append(fact*bus)
    min_idx = np.argmin(first_valid)
    return int((first_valid[min_idx] - start) * busses[min_idx])


def get_answer2(dl)->float:
    busses = [float(b) for b in dl[1].split(',') if b!='x']
    waittimes = []
    delta = 0
    for v in dl[1].split(','):
        if v != 'x':
            waittimes.append(delta)
        delta+=1

    initstep = int(busses[0])
    tmax = int(np.prod(busses))

    # find offset and stepsize (based on first busses)
    alignment_time = []
    for tt in range(0,tmax, initstep):
        beta = []
        for idx, bus in enumerate(busses[0:min(4,len(busses))]):
            beta.append((tt+waittimes[idx])/bus)

        if [round(x) for x in beta] == beta:
            alignment_time.append(tt)
            offset = tt
            
        if len(alignment_time)==2:
            offset = alignment_time[0]
            stepsize = alignment_time[1] - alignment_time[0]
            break
    
    print(f'using: offset={offset}, stepsize={stepsize}')
    # use larger step-size to find result
    for t in range(offset, tmax, stepsize):
        if t<0:
            continue
        beta = []
        for idx, bus in enumerate(busses):
            beta.append((t+waittimes[idx])/bus)
        # all needs to heltal
        if [round(x) for x in beta] == beta:
            break

    return t


if __name__ == "__main__":
    dl = open('data/2020/day13.csv').read().splitlines()
    #dl = open('test/2020/data/day13.csv').read().splitlines()
    answer1 = get_answer1(dl)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(dl)
    print(f'Todays second answer is: {answer2}')    
