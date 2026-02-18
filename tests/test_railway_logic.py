from railway_parser_pack.railway_logic import polyline_length


def test_polyline():
    pts = [(0,0), (3,4)]
    assert polyline_length(pts) == 5