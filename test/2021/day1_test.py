from utils.load_data import read_csv
from year2021.day1 import get_answer1, get_answer2


def test_get_answer():
    df = read_csv('test/2021/data/day1.csv', col_names=['XX'], sep=',')
    answer1 = get_answer1(df)
    answer2 = get_answer2(df)

    assert answer1 == 7
    assert answer2 == 5