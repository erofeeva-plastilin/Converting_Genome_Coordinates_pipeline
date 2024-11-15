def create_bed_file(input_data, output_bed_file):
    with open(output_bed_file, 'w') as bed_file:
        for _, row in input_data.iterrows():
            bed_file.write(f"{row['chr_original']}\t{row['pos_start_original']}\t{row['pos_end_original']}\n")
