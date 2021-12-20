from utils.utils import read_csv
from year2021.day20 import get_answer


def test_get_answer():
    dl = open('test/2021/data/day20.csv').read().splitlines()
    answer1 = get_answer(dl,2)

    assert answer1 == 35