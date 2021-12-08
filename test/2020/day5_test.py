from src.utils.load_data import read_csv
from src.day5 import get_answer1, get_answer2


def test_get_answer():
    df = read_csv('test/data/day5.csv', col_names=['boardingpass'])
    boardingpass_list = df.boardingpass.tolist()

    answer = get_answer1([boardingpass_list[0]])
    assert answer == 567

    answer = get_answer1([boardingpass_list[1]])
    assert answer == 119

    answer = get_answer1([boardingpass_list[2]])
    assert answer == 820

    answer = get_answer1(boardingpass_list)
    assert answer == 820