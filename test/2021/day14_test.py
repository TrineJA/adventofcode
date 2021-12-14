from utils.utils import read_csv
from year2021.day14 import get_answer1, get_answer2


def test_get_answer():
    dl = open('test/2021/data/day14.csv').read().splitlines()
    answer1 = get_answer1(dl,10)
    answer2 = get_answer2(dl,40)

    assert answer1 == 1588
    assert answer2 == 2188189693529