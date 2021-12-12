from utils.utils import read_csv
from year2020.day4 import get_answer1, get_answer2


def test_get_answer():
    df = read_csv('test/2020/data/day4.csv', col_names=['passport'], sep=',', skip_blank_lines=False)
    answer1 = get_answer1(df)
    assert answer1 == 2

    df_valid = read_csv('test/2020/data/day4_valid.csv', col_names=['passport'], sep=',', skip_blank_lines=False)
    answer2_valid = get_answer2(df_valid)
    assert answer2_valid == 4

    df_invalid = read_csv('test/2020/data/day4_invalid.csv', col_names=['passport'], sep=',', skip_blank_lines=False)
    answer2_invalid = get_answer2(df_invalid)
    assert answer2_invalid == 0