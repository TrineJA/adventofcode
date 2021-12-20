from utils.utils import read_csv
import pandas as pd


def print_img(img):
    for l in img:
        print(*l)
    return None

def zeropad_img(img, rep, inf_lights):
    n = len(img[0])
    img_out = rep*[n*inf_lights] + img + rep*[n*inf_lights] 
    img_out = [rep*inf_lights + x + rep*inf_lights for x in img_out]
    return img_out


def enhance_img(img, alg, Nstep):
    boarder_size_to_explore = 2
    inf_lights = '0'
    #print('Input Image')
    #print_img(img)
    for itt in range(Nstep):
        #print(f'inf lights are {inf_lights}')
        #add zeros to outerboarders
        img = zeropad_img(img, boarder_size_to_explore+1, inf_lights)
        img_out = []
        for i, row in enumerate(img[1:-1]):
            irow = i + 1
            new_row = ''
            for ii, x in enumerate(row[1:-1]):
                icol = ii + 1
                bin_no = img[irow-1][icol-1:icol+2] + img[irow][icol-1:icol+2] + img[irow+1][icol-1:icol+2] 
                alg_idx = int(bin_no,2)
                new_row += alg[alg_idx]
            img_out.append(new_row)
        #print('Output Image')
        #print_img(img_out)
        #update
        img = img_out
        if inf_lights == '0':
            inf_lights = alg[0]
        else:
            inf_lights = alg[-1]

        #print(img_out)
    return img_out


def get_answer(dl: list, Nstep: int)->float:
    alg = dl[0]
    alg = alg.replace('.','0').replace('#','1')
    img = dl[2:]
    img = [x.replace('.','0').replace('#','1') for x in img]

    img_out = enhance_img(img,alg, Nstep)

    Nlights = sum([x.count('1') for x in img_out])
    return Nlights




if __name__ == "__main__":
    dl = open('data/2021/day20.csv').read().splitlines()

    answer1 = get_answer(dl,2)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer(dl,50)
    print(f'Todays second answer is: {answer2}')    
