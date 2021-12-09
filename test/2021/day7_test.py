import csv
from year2021.day7 import get_answer1, get_answer2


def test_get_answer():
    with open('test/2021/data/day7.csv') as f:
        reader = csv.reader(f)
        pos_list = list(reader)[0]
    pos_list = list(map(int, pos_list))

    answer1 = get_answer1(pos_list)
    answer2 = get_answer2(pos_list)

    assert answer1 == 37
    assert answer2 == 168