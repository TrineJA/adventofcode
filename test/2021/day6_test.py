import csv
from year2021.day6 import get_answer1, get_answer2


def test_get_answer():
    with open('test/2021/data/day6.csv') as f:
        reader = csv.reader(f)
        init_state_list = list(reader)[0]
    init_state_list = list(map(int, init_state_list))

    answer1 = get_answer1(init_state_list)
    answer2 = get_answer2(init_state_list)

    assert answer1 == 5934
    assert answer2 == 26984457539