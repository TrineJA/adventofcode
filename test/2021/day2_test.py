from utils.utils import read_csv
from year2021.day2 import get_answer1, get_answer2


def test_get_answer():
    df = read_csv('test/2021/data/day2.csv', col_names=['dir','step'], sep=' ')
    answer1 = get_answer1(df)
    answer2 = get_answer2(df)

    assert answer1 == 150
    assert answer2 == 900