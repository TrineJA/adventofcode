import pandas as pd

def get_map():
    # ['Ldir', 'Rdir']
    d = dict.fromkeys(['N','S','E','W'], [])
    d['N'] = ['W','E']
    d['E'] = ['N','S']
    d['S'] = ['E','W']
    d['W'] = ['S','N']
    return d


def get_answer1(dl)->float:
    turn = get_map()  
    facing = 'E'
    dist = dict.fromkeys(['N','S','E','W'], 0)
    for step in dl:
        if step[0] == 'F':
            dist[facing] += int(step[1:])
        elif step[0] in ['N','S','E','W']:
            dist[step[0]] += int(step[1:])
        elif step[0] == 'R':
            deg = int(step[1:])
            for ss in range(int(deg/90)):
                facing = turn[facing][1]
        elif step[0] == 'L':
            deg = int(step[1:])
            for ss in range(int(deg/90)):
                facing = turn[facing][0]
    print(dist)
    score = abs(dist['E']-dist['W']) + abs(dist['N']-dist['S'])
    return score



def get_answer2(dl)->float:
    turn = get_map()  
    waypoint = dict(E=10, N=1)
    facing = 'E'
    dist = dict.fromkeys(['N','S','E','W'], 0)
    for step in dl:
        waypoint_new = dict.fromkeys(['N','S','E','W'], 0)
        if step[0] == 'F':
            waypoint_new = waypoint.copy()
            for k,v in waypoint.items():
                    dist[k] += int(v)*int(step[1:])
        elif step[0] in ['N','E','S','W']:
            for k, v in waypoint.items():
                waypoint_new[k] = v
            waypoint_new[step[0]] = waypoint[step[0]] + int(step[1:])
        elif step[0] == 'R':
            deg = int(step[1:])
            for k, v in waypoint.items():
                newk = k
                for ss in range(int(deg/90)):
                    newk = turn[newk][1]
                waypoint_new[newk] = waypoint[k]
        elif step[0] == 'L':
            deg = int(step[1:])
            for k, v in waypoint.items():
                newk = k
                for ss in range(int(deg/90)):
                    newk = turn[newk][0]
                waypoint_new[newk] = waypoint[k]
        waypoint = waypoint_new.copy()
    score = abs(dist['E']-dist['W']) + abs(dist['N']-dist['S'])
    return score


if __name__ == "__main__":
    dl = open('data/2020/day12.csv').read().splitlines()
    answer1 = get_answer1(dl)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(dl)
    print(f'Todays second answer is: {answer2}')    
