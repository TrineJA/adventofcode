from src.utils.load_data import read_csv
from src.day9 import get_answer1, get_answer2


def test_get_answer():
    df = read_csv('test/data/day9.csv', col_names=['xmas'], sep=',')
    answer1 = get_answer1(df, 5)
    answer2 = get_answer2(df, 5)

    assert answer1 == 127
    assert answer2 == 62