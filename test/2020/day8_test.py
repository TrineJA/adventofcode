from src.utils.utils import read_csv
from src.day8 import get_answer1, get_answer2


def test_get_answer():
    df = read_csv('test/data/day8.csv', col_names=['operation','argument'], sep=' ')
    answer1 = get_answer1(df)
    answer2 = get_answer2(df)

    assert answer1 == 5
    assert answer2 == 8