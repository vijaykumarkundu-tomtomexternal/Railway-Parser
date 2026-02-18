import ezdxf
import pandas as pd
import sys
from railway_parser_pack.blocks import extract_blocks

def parse_geometry(file_path):
    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()

    rows = []

    for e in msp:
        if e.dxftype() == "LINE":
            rows.append({
                "type": "LINE",
                "layer": e.dxf.layer,
                "x1": e.dxf.start.x,
                "y1": e.dxf.start.y,
                "x2": e.dxf.end.x,
                "y2": e.dxf.end.y,
            })

        elif e.dxftype() == "POINT":
            rows.append({
                "type": "POINT",
                "layer": e.dxf.layer,
                "x": e.dxf.location.x,
                "y": e.dxf.location.y,
            })

    return pd.DataFrame(rows)


if __name__ == "__main__":
    df = parse_geometry(sys.argv[1])
    print(df)
    df.to_csv("output/result.csv", index=False)
    df2=extract_blocks(sys.argv[1])
    print(df2)
