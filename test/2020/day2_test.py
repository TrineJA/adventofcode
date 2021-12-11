from src.utils.utils import read_csv
from src.day2 import get_answer1, get_answer2


def test_get_answer():
    df_passwords = read_csv('test/data/day2.csv', col_names=['policy','password'], sep=':')
    answer1 = get_answer1(df_passwords)
    answer2 = get_answer2(df_passwords)

    assert answer1 == 2
    assert answer2 == 1