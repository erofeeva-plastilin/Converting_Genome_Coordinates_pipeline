import pandas as pd

REQUIRED_COLUMNS = ['chr_original', 'pos_original', 'pos_original_end']

def read_tsv(file_path):
    data = pd.read_csv(file_path, sep='\t')
    check_required_columns(data)
    return data

def write_tsv(data, file_path):
    data.to_csv(file_path, sep='\t', index=False)

def check_required_columns(data):
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in data.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")
