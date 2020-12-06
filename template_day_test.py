from src.utils.load_data import read_csv
from src.dayX import get_answer1, get_answer2


def test_get_answer():
    df = read_csv('test/data/dayX.csv', col_names=['XX'], sep=',')
    answer1 = get_answer1(df)
    answer2 = get_answer2(df)

    assert answer1 == 7
    assert answer2 == 336