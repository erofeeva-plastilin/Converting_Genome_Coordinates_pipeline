import subprocess
import pandas as pd

def convert_coordinates(bed_file, chain_file, output_data, output_tsv_file):
    crossmap_output = f"{output_tsv_file}_temp"
    result = subprocess.run(["CrossMap", "bed", chain_file, bed_file], stdout=open(crossmap_output, 'w'))
    if result.returncode != 0:
        raise RuntimeError("CrossMap did not complete successfully. Please check the chain file and BED file paths.")
    parsed_data = parse_crossmap_output(crossmap_output)
    output_data['chr'] = pd.NA
    output_data['pos_start'] = pd.NA
    output_data['pos_end'] = pd.NA
    output_data[['chr', 'pos_start', 'pos_end']] = output_data.apply(
        lambda row: find_mapped_coordinates(row, parsed_data), axis=1, result_type="expand"
    )
    output_data.to_csv(output_tsv_file, sep='\t', index=False)

def parse_crossmap_output(crossmap_output_file):
    data = []
    with open(crossmap_output_file, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if "Unmap" in parts:
                continue
            data.append({
                "chr_original": parts[0],
                "pos_start_original": int(parts[1]),
                "pos_end_original": int(parts[2]),
                "chr": parts[4],
                "pos_start": int(parts[5]),
                "pos_end": int(parts[6])
            })
    return pd.DataFrame(data)

def find_mapped_coordinates(row, parsed_data):
    match = parsed_data[
        (parsed_data['chr_original'] == row['chr_original']) &
        (parsed_data['pos_start_original'] == row['pos_start_original']) &
        (parsed_data['pos_end_original'] == row['pos_end_original'])
    ]

    if not match.empty:
        return match.iloc[0]['chr'], match.iloc[0]['pos_start'], match.iloc[0]['pos_end']
    return pd.NA, pd.NA, pd.NA
