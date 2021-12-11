from src.utils.utils import read_csv
from src.day7 import get_answer1, get_answer2


def test_get_answer():
    df = read_csv('test/data/day7.csv', col_names=['outer_bags','inner_bags'], sep='contain', engine='python')
    answer1 = get_answer1(df)
    answer2 = get_answer2(df)

    df2 = read_csv('test/data/day7_2.csv', col_names=['outer_bags','inner_bags'], sep='contain', engine='python')
    answer2_2 = get_answer2(df2)

    assert answer1 == 4
    assert answer2 == 32
    assert answer2_2 == 126