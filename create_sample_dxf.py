import ezdxf

doc = ezdxf.new()
msp = doc.modelspace()

# Track lines
msp.add_line((0, 0), (100, 0), dxfattribs={"layer": "TRACK"})
msp.add_line((100, 0), (200, 0), dxfattribs={"layer": "TRACK"})

# Signals
msp.add_point((50, 0), dxfattribs={"layer": "SIGNALS"})
msp.add_point((150, 0), dxfattribs={"layer": "SIGNALS"})

doc.saveas("data/sample1.dxf")

print("DXF created!")
