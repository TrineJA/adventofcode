from utils.utils import read_csv
from year2020.day1 import get_answer1, get_answer2


def test_get_answer():
    df_expenses = read_csv('test/2020/data/day1.csv', col_names=['amount'])
    answer1 = get_answer1(df_expenses)
    answer2 = get_answer2(df_expenses)

    assert answer1 == 514579
    assert answer2 == 241861950