# Converting_Genome_Coordinates_pipeline
```
mkdir -p /mnt/users/erofeevan/pyoverchain_workdir
cp chr_map.tsv /mnt/users/erofeevan/pyoverchain_workdir/
cp /mnt/reference/genomes/beta_vulgaris/GCF_026745355.1/GCF_026745355.1_EL10.2_genomic.unmasked.fna /mnt/users/erofeevan/pyoverchain_workdir/
cp /mnt/users/erofeevan/Plant_culture/Sunflower/Sugar_beet/GCF_000511025.2_RefBeet-1.2.2_genomic.fna /mnt/users/erofeevan/pyoverchain_workdir/
cd /mnt/users/erofeevan/pyoverchain_workdir
time pyoverchain -n 10 -p 10  GCF_000511025.2_RefBeet-1.2.2_genomic.fna GCF_026745355.1_EL10.2_genomic.unmasked.fna chr_map.tsv
awk '{print $1, $2, $2}' Sugar_beet.bed > Sugar_beet_fixed.bed
CrossMap bed GCF_000511025.2_RefBeet-1.2.2_genomic.fna.to.GCF_026745355.1_EL10.2_genomic.unmasked.fna.over.chain Sugar_beet_fixed.bed > hello
```
