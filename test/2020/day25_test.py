from src.utils.utils import read_csv
from src.day25 import get_answer1, get_answer2


def test_get_answer():
    df = read_csv('test/data/day25.csv', col_names=['pub_key'], sep=',')
    answer1 = get_answer1(df)
    answer2 = get_answer2(df)

    assert answer1 == 14897079
    #assert answer2 == 336