import argparse
import os
from CoordTransfer.io_utils import read_tsv, write_tsv
from CoordTransfer.bed_converter import create_bed_file
from CoordTransfer.coord_converter import convert_coordinates
from CoordTransfer.chain_files import get_chain_file

def main():
    parser = argparse.ArgumentParser(description="Coordinate Transfer Tool")
    parser.add_argument("-a", "--assembly", required=True, help="The name of the old genomic assembly")
    parser.add_argument("file_name", help="Input TSV file with genomic regions")
    parser.add_argument("output_file", help="Output TSV file with converted coordinates")
    args = parser.parse_args()
    input_data = read_tsv(args.file_name)
    bed_file = args.file_name.replace(".tsv", ".bed")
    create_bed_file(input_data, bed_file)
    chain_file = get_chain_file(args.assembly)
    if not chain_file:
        print(f"Error: Chain file for assembly '{args.assembly}' not found.")
        return
    convert_coordinates(bed_file, chain_file, input_data, args.output_file)
    print(f"Coordinate conversion completed. Output saved to {args.output_file}")

if __name__ == "__main__":
    main()
