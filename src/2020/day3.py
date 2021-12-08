from utils.load_data import read_csv
import pandas as pd


def toboggan_slide(df, step_right, step_down):
   # initialize
    row_idx = 0
    col_idx = 0
    Ntrees = 0
    last_col_idx_in_base_pattern = len(df.pattern[0])-1
    last_row_idx_in_base_pattern = df.shape[0]-1
    max_steps = last_row_idx_in_base_pattern+1 # if we only step 1 down

    # start sliding :)
    for step in range(1,max_steps+1):
        # step to next location
        row_idx = row_idx + step_down
        col_idx = col_idx + step_right

        # If I stepped out of the current pattern (below). Then I have arrived
        if row_idx > last_row_idx_in_base_pattern:
            print('Hooray, I have arrived')
            break

        # If I stepped out of the current pattern (right). Then update col_idx to mimic append of base-pattern
        if col_idx > last_col_idx_in_base_pattern:
            col_idx = (col_idx - last_col_idx_in_base_pattern) - 1

        # get value at current_location
        location_value = df.pattern[row_idx][col_idx]

        # Am I at a tree?
        if location_value == '#':
            Ntrees+=1

    return Ntrees 


def get_answer1(df: pd.DataFrame)->float:
    # start sliding
    Ntrees = toboggan_slide(df, step_right=3, step_down=1)
    return Ntrees


def get_answer2(df: pd.DataFrame)->float:
    slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

    Ntrees = 1
    for slope in slopes:
        # start sliding
        Ntrees_this_slope = toboggan_slide(df, step_right=slope[0], step_down=slope[1])
        print(f'slope{slope}: Ntrees:{Ntrees_this_slope}')
        Ntrees=Ntrees*Ntrees_this_slope

    return Ntrees



if __name__ == "__main__":
    df = read_csv('data/day3.csv', col_names=['pattern'], sep=',')
    answer1 = get_answer1(df)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df)
    print(f'Todays second answer is: {answer2}')    
