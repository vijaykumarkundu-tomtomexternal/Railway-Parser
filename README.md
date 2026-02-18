# Railway DXF Parser

This project extracts railway geometry & signal information from DXF files.

Features:
- Parse DXF geometry
- Extract block attributes
- Compute signal distance along track
- DWG → DXF conversion helper
- Unit tests with pytest

## Run Parser
python -m railway_parser.parser data/sample1.dxf

## Run Tests
pytest