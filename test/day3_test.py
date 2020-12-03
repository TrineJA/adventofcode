from src.utils.load_data import read_csv
from src.day3 import get_answer1, get_answer2


def test_get_answer():
    df = read_csv('test/data/day3.csv', col_names=['pattern'], sep=',')
    answer1 = get_answer1(df)
    answer2 = get_answer2(df)

    assert answer1 == 7
    assert answer2 == 336