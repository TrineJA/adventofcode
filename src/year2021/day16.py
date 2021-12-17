from utils.utils import read_csv
import pandas as pd
import numpy as np

def parsePacket(bin_str, i):
    # start reading string from index i
    # get header
    version = int(bin_str[i:i+3],2)
    version_sum = version
    value = 0
    i+=3
    type = int(bin_str[i:i+3],2)
    i+=3

    #literal
    if type == 4:
        packet = bin_str[i:]
        lit_str = ''
        while True:
            p = bin_str[i:i+5]
            i+=5
            lit_str += p[1:]
            if p[0]=='0':
                value=(int(lit_str,2))
                return i, version_sum, value 
    #operator
    else:
        length_type_id = bin_str[i]
        i+=1
        value_list = []
        if length_type_id=='0':
            L=15
            subpacket_tot_length = int(bin_str[i:i+L],2)
            i+=L
            start_i = i
            while i < start_i + subpacket_tot_length:
                i, version_sum_i, value_i = parsePacket(bin_str, i)
                version_sum += version_sum_i
                value_list.append(value_i)
        elif length_type_id=='1':
            L=11
            n_subpackets = int(bin_str[i:i+L],2)
            i+=L
            for idx in range(n_subpackets):
                i, version_sum_i, value_i = parsePacket(bin_str, i)
                version_sum += version_sum_i
                value_list.append(value_i)
        #evalue value list
        if type==0:
            value=sum(value_list)
        elif type==1:
            value=np.prod(value_list)
        elif type==2:
            value=min(value_list)
        elif type==3:
            value=max(value_list)
        elif type==5:
            value=int(value_list[0]>value_list[1])
        elif type==6:
            value=int(value_list[0]<value_list[1])  
        elif type==7:
            value=int(value_list[0]==value_list[1])          
    return i, version_sum, value


def get_answer(dl: list)->float:
    # prepare binary string
    hex_str = dl[0].rstrip('0')
    bin_str = bin(int(hex_str, 16))[2:]
    # add leading zeros
    nzeros = 4 * len(hex_str) - len(bin_str) #int(np.ceil(len(bin_str)/4)*4 - len(bin_str))
    bin_str = nzeros * '0' + bin_str

    next_i, version_sum, value = parsePacket(bin_str, 0)
    return version_sum, value


if __name__ == "__main__":
    dl = open('data/2021/day16.csv').read().splitlines()
    #dl = open('test/2021/data/day16.csv').read().splitlines()
    answer1 = get_answer(dl)[0]
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer(dl)[1]
    print(f'Todays second answer is: {answer2}')    
