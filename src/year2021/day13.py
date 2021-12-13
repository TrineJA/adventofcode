from utils.utils import read_csv
import pandas as pd


def get_answer(df: pd.DataFrame, q)->float:
    # get fold
    folds = df[df.Y.isnull()].X.tolist()
    if q==1:
        folds = folds[0:1]
    df = df[df.Y.notnull()].astype(int)

    #make board
    board = pd.DataFrame(0, index = range(df.max().Y+1), columns=range(df.max().X+1))
    for idx, row in df.iterrows():
        board.iloc[row.Y,row.X]=1
    
    # fold
    for fold in folds:
        fold_idx = int(fold.split('=')[-1])
        fold_dir = fold.split('=')[0][-1]
        #up
        if fold_dir == 'y':
            #split
            board1 = board[0:fold_idx]
            board2 = board[fold_idx+1:]
            #flip
            board2 = board2[::-1].reset_index(drop=True)
            #overlay
            board = board1+board2
        #left
        elif fold_dir == 'x':
            #split
            board1 = board.iloc[:,0:fold_idx]
            board2 = board.iloc[:,fold_idx+1:]
            #flip
            board2 = board2[board2.columns[::-1]]
            board2.columns = board1.columns
            #overlay
            board = board1+board2
    
    if q==1:
        return (board>0).sum().sum()
    elif q==2:
        for idx in range(8):
            print(board.iloc[:,5*idx:5*idx+5])
            print('---')
        return None


if __name__ == "__main__":
    df = read_csv('data/2021/day13.csv', col_names=['X','Y'], sep=',')
    answer1 = get_answer(df, 1)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer(df, 2)
    print(f'Todays second answer is: {answer2}')    
