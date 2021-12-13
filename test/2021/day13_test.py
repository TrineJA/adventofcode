from utils.utils import read_csv
from year2021.day13 import get_answer


def test_get_answer():
    df = read_csv('test/2021/data/day13.csv', col_names=['X','Y'], sep=',')
    answer1 = get_answer(df,1)

    assert answer1 == 17