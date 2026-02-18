from railway_parser_pack.railway_logic import distance


def test_distance():
    assert distance((0,0), (3,4)) == 5