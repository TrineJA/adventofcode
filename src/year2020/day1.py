from utils.utils import read_csv
import pandas as pd


def get_answer1(df_expenses: pd.DataFrame)->float:
    value_list = df_expenses['amount'].tolist()
    # brute force
    result = None
    for val1 in value_list:
        val2 = 2020 - val1
        if val2 in value_list:
            result = val1 * val2
            break
    return result


def get_answer2(df_expenses: pd.DataFrame)->float:
    value_list = df_expenses['amount'].tolist()
    # brute force
    result = None
    for val1 in value_list:
        for val2 in value_list:
            val3 = 2020 - (val1+val2)
            if val3 in value_list:
                result = val1 * val2 * val3
                break
    return result
        

if __name__ == "__main__":
    df_expenses = read_csv('data/day1.csv', col_names=['amount'])
    answer1 = get_answer1(df_expenses)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df_expenses)
    print(f'Todays second answer is: {answer2}')
    
