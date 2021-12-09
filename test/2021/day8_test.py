from utils.load_data import read_csv
from year2021.day8 import get_answer1, get_answer2


def test_get_answer():
    df = read_csv('test/2021/data/day8.csv', col_names=['all','shown'], sep='|')
    answer1 = get_answer1(df)
    answer2 = get_answer2(df)

    assert answer1 == 26
    assert answer2 == 61229