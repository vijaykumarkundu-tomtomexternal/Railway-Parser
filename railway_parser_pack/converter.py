import subprocess


def convert_dwg_to_dxf(input_folder, output_folder):
    subprocess.run([
        "ODAFileConverter",
        input_folder,
        output_folder,
        "ACAD2018",
        "DXF",
        "0",
        "1"
    ])