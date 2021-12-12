from utils.utils import read_csv
from year2020.day9 import get_answer1, get_answer2


def test_get_answer():
    df = read_csv('test/2020/data/day9.csv', col_names=['xmas'], sep=',')
    answer1 = get_answer1(df, 5)
    answer2 = get_answer2(df, 5)

    assert answer1 == 127
    assert answer2 == 62