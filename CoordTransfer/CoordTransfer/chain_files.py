CHAIN_FILES = {
    'soybean_a1v1': '/mnt/users/erofeevan/Converting_Genome_Coordinates_pipeline/CoordTransfer/Chain_files/Glycine_max_a1.v1.fasta.to.GCF_000004515.6_Glycine_max_v4.0_genomic.unmasked.fna.over.chain',
    'soybean_a2v1': '/mnt/users/erofeevan/Converting_Genome_Coordinates_pipeline/CoordTransfer/Chain_files/Glycine_max_a2.v1.fasta.to.GCF_000004515.6_Glycine_max_v4.0_genomic.unmasked.fna.over.chain',
    'refbeet1.2.2': '/mnt/users/erofeevan/Converting_Genome_Coordinates_pipeline/CoordTransfer/Chain_files/GCF_000511025.2_RefBeet-1.2.2_genomic.fna.to.GCF_026745355.1_EL10.2_genomic.unmasked.fna.over.chain'
}

def get_chain_file(assembly_name):
    chain_file = CHAIN_FILES.get(assembly_name)
    if chain_file is None:
        print(f"Chain file for assembly '{assembly_name}' not found.")
    return chain_file
