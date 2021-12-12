from utils.utils import read_csv
import pandas as pd


def public_key_to_loop_size(pub_key:int)->int:
    subject_number = 7
    val = 1
    maxItt = 10000000
    for ii in range(maxItt):
        val *= subject_number
        val = val % 20201227
        if val == pub_key:
            loop_size = ii + 1
            break
    if ii == maxItt-1:
        raise ValueError(f'loop size cannot be derived from public key: {pub_key}')
    
    return loop_size


def get_encryption_key(subject_number: int, loop_size:int) -> int:
    val = 1
    for ii in range(loop_size):
        val *= subject_number
        val = val % 20201227
    return val


def get_answer1(df: pd.DataFrame)->float:
    door_pub_key = df.iloc[0].values[0]
    card_pub_key = df.iloc[1].values[0]

    door_loop_size = public_key_to_loop_size(door_pub_key)
    card_loop_size = public_key_to_loop_size(card_pub_key)

    encryption_key1 = get_encryption_key(card_pub_key, door_loop_size)
    encryption_key2 = get_encryption_key(door_pub_key, card_loop_size)

    if encryption_key1 != encryption_key2:
        raise ValueError('encryption keys does not match. something went wrong')

    return encryption_key1


def get_answer2(df: pd.DataFrame)->float:
    pass


if __name__ == "__main__":
    df = read_csv('data/day25.csv', col_names=['pub_key'], sep=',')
    answer1 = get_answer1(df)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df)
    print(f'Todays second answer is: {answer2}')    
