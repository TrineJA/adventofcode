from utils.utils import read_csv
from year2021.dayX import get_answer1, get_answer2


def test_get_answer():
    df = read_csv('test/2021/data/dayX.csv', col_names=['XX'], sep=',')
    dl = open('test/2021/data/dayX.csv').read().splitlines()
    answer1 = get_answer1(df)
    answer2 = get_answer2(df)

    assert answer1 == 7
    assert answer2 == 336