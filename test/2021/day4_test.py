import pandas as pd
import csv
from year2021.day4 import get_answer1, get_answer2


def test_get_answer():
    df_boards = pd.read_csv('test/2021/data/day4.csv', delim_whitespace=True, skiprows=[0],  names=['x1','x2','x3','x4','x5'])
    with open('test/2021/data/day4.csv') as f:
        reader = csv.reader(f)
        call_list = next(reader)
    call_list = list(map(int, call_list))

    answer1 = get_answer1(df_boards, call_list)
    answer2 = get_answer2(df_boards, call_list)

    assert answer1 == 4512
    assert answer2 == 1924