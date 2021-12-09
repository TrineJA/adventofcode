from utils.load_data import read_csv
import pandas as pd


def get_answer1(df: pd.DataFrame)->float:
    Nbits = len(df.loc[0,'XX'])
    df2 = df['XX'].str.split('', Nbits, expand=True).drop(columns=[0])

    gamma_binary = df2.mode().apply(''.join, axis=1).values[0]
    epsilon_binary = gamma_binary.replace('1','z').replace('0','1').replace('z','0')
    gamma_decimal = int(gamma_binary, 2)
    epsilon_decimal = int(epsilon_binary, 2)

    return gamma_decimal * epsilon_decimal


def get_answer2(df: pd.DataFrame)->float:
    Nbits = len(df.loc[0,'XX'])
    df2 = df['XX'].str.split('', Nbits, expand=True).drop(columns=[0])

    #get oxy rating
    df_oxy = df2.copy()
    for ii in range(1,Nbits+1):
        oxy_crit = df_oxy[ii].mode().max()
        df_oxy = df_oxy[df_oxy[ii]==oxy_crit]
        if df_oxy.shape[0]==1:
            break
    oxy_rating_binary = df_oxy.apply(''.join, axis=1).values[0]

    #get co2 rating
    df_co2 = df2.copy()
    for ii in range(1,Nbits+1):
        not_co2_crit = df_co2[ii].mode().max()
        df_co2 = df_co2[df_co2[ii]!=not_co2_crit]
        if df_co2.shape[0]==1:
            break
    co2_rating_binary = df_co2.apply(''.join, axis=1).values[0]
    
    return int(oxy_rating_binary,2) * int(co2_rating_binary,2)


if __name__ == "__main__":
    df = read_csv('data/2021/day3.csv', col_names=['XX'], sep=',', dtype=str)
    answer1 = get_answer1(df)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df)
    print(f'Todays second answer is: {answer2}')    
