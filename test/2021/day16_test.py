from utils.utils import read_csv
from year2021.day16 import get_answer


def test_get_answer():
    dl = open('test/2021/data/day16.csv').read().splitlines()

    assert get_answer(['8A004A801A8002F478'])[0] == 16
    assert get_answer(['620080001611562C8802118E34'])[0] == 12
    assert get_answer(['C0015000016115A2E0802F182340'])[0] == 23
    assert get_answer(['A0016C880162017C3686B18A3D4780'])[0] == 31
    assert get_answer(['C200B40A82'])[1] == 3
    assert get_answer(['04005AC33890'])[1] == 54
    assert get_answer(['880086C3E88112'])[1] == 7
    assert get_answer(['CE00C43D881120'])[1] == 9
    assert get_answer(['D8005AC2A8F0'])[1] == 1
    assert get_answer(['F600BC2D8F'])[1] == 0
    assert get_answer(['9C005AC2F8F0'])[1] == 0
    assert get_answer(['9C0141080250320F1802104A08'])[1] == 1