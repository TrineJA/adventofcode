from src.utils.utils import read_csv
from src.day20 import get_answer1, get_answer2


def test_get_answer():
    df = read_csv('test/data/day20.csv', col_names=['XX'], sep=',')
    answer1 = get_answer1(df)
    answer2 = get_answer2(df)

    assert answer1 == 20899048083289
    #assert answer2 == 336