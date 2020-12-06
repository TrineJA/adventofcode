from src.utils.load_data import read_csv
from src.day6 import get_answer1, get_answer2


def test_get_answer():
    df = read_csv('test/data/day6.csv', col_names=['response'], sep=',', skip_blank_lines=False)
    answer1 = get_answer1(df)
    answer2 = get_answer2(df)

    assert answer1 == 11
    assert answer2 == 6