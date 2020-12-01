from src.day1 import get_answer1, get_answer2, get_data


def test_day1():
    df_expenses = get_data('test/data/day1.csv')
    answer1 = get_answer1(df_expenses)
    answer2 = get_answer2(df_expenses)

    assert answer1 == 514579
    assert answer2 == 241861950