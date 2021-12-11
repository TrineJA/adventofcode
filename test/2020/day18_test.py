from src.utils.utils import read_csv
from src.day18 import get_answer1, get_answer2


def test_get_answer():
    df = read_csv('test/data/day18.csv', col_names=['expr'], sep=',')
    answer1 = get_answer1(df)
    answer2 = get_answer2(df)

    assert answer1 == 26335
    assert answer2 == 693891