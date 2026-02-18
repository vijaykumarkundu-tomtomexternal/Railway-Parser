import ezdxf
import pandas as pd


def extract_blocks(file_path):
    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()

    blocks = []

    for insert in msp.query("INSERT"):
        attrs = {a.dxf.tag: a.dxf.text for a in insert.attribs}
        blocks.append({
            "block_name": insert.dxf.name,
            "layer": insert.dxf.layer,
            "attributes": attrs
        })

    return pd.DataFrame(blocks)