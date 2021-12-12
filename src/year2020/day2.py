from utils.utils import read_csv
import pandas as pd


def get_answer1(df_passwords: pd.DataFrame)->float:
    Nvalid = 0
    # loop through each password
    for idx, row in df_passwords.iterrows():
        policy = row['policy'].lower()
        password = row['password'].strip().lower()

        # seperate out rule elements from policy
        min_reps = float(policy.split(' ')[0].split('-')[0])
        max_reps = float(policy.split(' ')[0].split('-')[1])
        letter = policy.split(' ')[1]

        # get number of reps of the given letter in the password
        Nreps = password.count(letter)

        # check validity
        if Nreps >= min_reps and Nreps <= max_reps:
            Nvalid+=1

    return Nvalid


def get_answer2(df_passwords: pd.DataFrame)->float:
    Nvalid = 0
    # loop through each password
    for idx, row in df_passwords.iterrows():
        policy = row['policy'].lower()
        password = row['password'].strip().lower()

        # seperate out rule elements from policy
        loc1 = int(float(policy.split(' ')[0].split('-')[0]))-1
        loc2 = int(float(policy.split(' ')[0].split('-')[1]))-1
        letter = policy.split(' ')[1]

        # how many times are letter at loc1 and loc2
        Nreps = sum([password[loc1]==letter, password[loc2]==letter])

        # check validity
        if Nreps==1:
            Nvalid+=1

    return Nvalid


if __name__ == "__main__":
    df_passwords = read_csv('data/day2.csv', col_names=['policy','password'], sep=':')
    answer1 = get_answer1(df_passwords)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df_passwords)
    print(f'Todays second answer is: {answer2}')    
