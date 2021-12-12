from utils.utils import read_csv
from year2021.day12 import get_answer1, get_answer2


def test_get_answer():
    df = read_csv('test/2021/data/day12.csv', col_names=['f','t'], sep='-')
    answer1 = get_answer1(df)
    answer2 = get_answer2(df)

    assert answer1 == 10
    assert answer2 == 36
