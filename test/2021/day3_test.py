from utils.utils import read_csv
from year2021.day3 import get_answer1, get_answer2


def test_get_answer():
    df = read_csv('test/2021/data/day3.csv', col_names=['XX'], sep=',', dtype=str)
    answer1 = get_answer1(df)
    answer2 = get_answer2(df)

    assert answer1 == 198
    assert answer2 == 230