from utils.load_data import read_csv
import pandas as pd
import string

def get_answer1(df: pd.DataFrame)->float:
    # initialize
    total_unique_positive_responses = 0 
    responses_within_group = ''
    # ensure dataframe ends on an empty row
    if not df.tail(1).isnull().values:
        df = df.append(pd.Series(dtype='object'), ignore_index=True)

    # loop over rows
    for idx, row in df.iterrows():
        # if this row is a group seperator
        if row.isnull().any():
            # evaluate current group
            unique_responses_within_group = ''.join(set(responses_within_group))
            total_unique_positive_responses += len(unique_responses_within_group)
            # reset
            responses_within_group = ''
        else:
            responses_within_group+=row.response
    return total_unique_positive_responses


def get_answer2(df: pd.DataFrame)->float:
    # initialize
    total_shared_positive_responses = 0 
    responses_within_group = []
    shared_responses = list(string.ascii_lowercase)

    # ensure dataframe ends on an empty row
    if not df.tail(1).isnull().values:
        df = df.append(pd.Series(dtype='object'), ignore_index=True)

    # loop over rows
    for idx, row in df.iterrows():
        # if this row is a group seperator
        if row.isnull().any():
            # evaluate current group
            # loop over each persons responses
            for response in responses_within_group:
                shared_responses =  set(shared_responses).intersection(set(list(response)))

            total_shared_positive_responses += len(shared_responses)
            # reset
            responses_within_group = []
            shared_responses = list(string.ascii_lowercase)
        else:
            responses_within_group.append(row.response)
    return total_shared_positive_responses


if __name__ == "__main__":
    df = read_csv('data/day6.csv', col_names=['response'], sep=',', skip_blank_lines=False)
    answer1 = get_answer1(df)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df)
    print(f'Todays second answer is: {answer2}')    
