from utils.utils import read_csv
from year2020.day10 import get_answer1, get_answer2


def test_get_answer():
    dl = open('test/2020/data/day10.csv').read().splitlines()
    answer1 = get_answer1(dl)
    answer2 = get_answer2(dl)

    assert answer1 == 220
    assert answer2 == 19208