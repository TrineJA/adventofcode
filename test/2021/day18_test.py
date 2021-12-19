from utils.utils import read_csv
from year2021.day18 import get_answer1, get_answer2


def test_get_answer():
    dl = open('test/2021/data/day18.csv').read().splitlines()
    answer1 = get_answer1(dl)
    answer2 = get_answer2(dl)

    assert answer1 == 4140
    assert answer2 == 3993