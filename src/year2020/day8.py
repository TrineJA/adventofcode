from utils.utils import read_csv
import pandas as pd


def play_instructions(df):
    # init
    row_idx = 0
    accumulator = 0
    maxitt = df.shape[0]
    for ii in range(maxitt):
        # have I been here before, then Im done
        if df.loc[row_idx,'instruction_executed']:
            exit_reason='infinite loop'
            break
        # read operation and act accordingly
        if df.loc[row_idx,'operation'] == 'nop':
            df.loc[row_idx,'instruction_executed']=1
            row_idx+=1
        elif df.loc[row_idx,'operation'] == 'acc':
            accumulator += df.loc[row_idx,'argument']
            df.loc[row_idx,'instruction_executed']=1
            row_idx+=1
        elif df.loc[row_idx,'operation'] == 'jmp':
            df.loc[row_idx,'instruction_executed']=1
            row_idx+=df.loc[row_idx,'argument']
        # check if you have exited correctly
        if row_idx == df.shape[0]:
            exit_reason='success'
            break
    return exit_reason, accumulator


def get_answer1(df: pd.DataFrame)->float:
    # keep track of where you have already been
    df['instruction_executed'] = 0
    # play instructions
    exit_reason, accumulator = play_instructions(df)
    #print(exit_reason)
    return accumulator


def get_answer2(df: pd.DataFrame)->float:

    # where I have already been
    df['instruction_executed'] = 0

    # init
    idx_to_flip = df.query("operation in ['nop','jmp']").index

    # flip one nop/jmp one by one
    for idx in idx_to_flip:
        _df = df.copy()

        # flip
        if _df.loc[idx,'operation']=='jmp':
            _df.loc[idx,'operation'] = 'nop'
        elif _df.loc[idx,'operation']=='nop':
            _df.loc[idx,'operation'] = 'jmp'

        # play instructions
        exit_reason, accumulator = play_instructions(_df)

        # check if exit was correct
        if exit_reason == 'success':
            return accumulator
    
    

if __name__ == "__main__":
    df = read_csv('data/day8.csv', col_names=['operation','argument'], sep=' ')
    answer1 = get_answer1(df)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df)
    print(f'Todays second answer is: {answer2}')    
