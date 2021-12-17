from utils.utils import read_csv
from year2021.day17 import get_answer


def test_get_answer():
    dl = open('test/2021/data/day17.csv').read().splitlines()
    answer = get_answer(dl)

    assert answer[0] == 45
    assert answer[1] == 112