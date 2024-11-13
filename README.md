# Converting_Genome_Coordinates_pipeline
# CoordTransfer - основной скрипт для перевода координат и заполнения таблицы
## Установка
Скачивание:
```
git clone https://github.com/erofeeva-plastilin/Converting_Genome_Coordinates_pipeline.git
```
Установка зависимостей:
```
cd CoordTransfer
conda env create -f CoordTransfer_env.yml
conda activate CoordTransfer_env
```
## Описание CoordTransfer
CoordTransfer на вход принимает обычную табличку (в ней должны быть фиксированы названия или номера столбцов) и название исходной сборки из списка (для нее есть chain файл), делает bed файл, переводит координаты и вносит полученные значения в табличку в те специальные колонки

## Пример запуска CoordTransfer

## Сравнение CoordTransfer с SNPLift

# Make_chain - дополнительный скрипт для создания chain-файлов вручную
Установка зависимостей:
```
conda env create -f CGCp_env.yml
conda activate CGCp_env
```
## Описание Make_chain

## Пример запуска Make_chain
```
conda activate CGCp_env
mkdir -p /mnt/users/erofeevan/pyoverchain_workdir
cd /mnt/users/erofeevan/pyoverchain_workdir
cp chr_map.tsv /mnt/users/erofeevan/pyoverchain_workdir/
cp /mnt/reference/genomes/beta_vulgaris/GCF_026745355.1/GCF_026745355.1_EL10.2_genomic.unmasked.fna /mnt/users/erofeevan/pyoverchain_workdir/
cp /mnt/users/erofeevan/Plant_culture/Sunflower/Sugar_beet/GCF_000511025.2_RefBeet-1.2.2_genomic.fna /mnt/users/erofeevan/pyoverchain_workdir/
cd /mnt/users/erofeevan/pyoverchain_workdir
time pyoverchain -n 10 -p 10  GCF_000511025.2_RefBeet-1.2.2_genomic.fna GCF_026745355.1_EL10.2_genomic.unmasked.fna chr_map.tsv
awk '{print $1, $2, $2}' Sugar_beet.bed > Sugar_beet_fixed.bed
conda activate crossmap1_env
CrossMap bed GCF_000511025.2_RefBeet-1.2.2_genomic.fna.to.GCF_026745355.1_EL10.2_genomic.unmasked.fna.over.chain Sugar_beet_fixed.bed > hello
```
tmux attach -t 17
time pyoverchain -n 7 -p 3  Pisum_sativum_v1a.fa GCF_024323335.1_CAAS_Psat_ZW6_1.0_genomic.unmasked.fna chr_map_pea.tsv
```time pyoverchain -n 1 -p 20  Glycine_max_a1.v1.fasta GCF_000004515.6_Glycine_max_v4.0_genomic.unmasked.fna chr_map_Glycine_max_a1v1_to_v4.0.tsv```
Соя: 
real    998m38.447s
user    1661m50.487s
sys     1m4.388s

```time pyoverchain -n 1 -p 23 Glycine_max_a2.v1.fasta GCF_000004515.6_Glycine_max_v4.0_genomic.unmasked.fna chr_map_Glycine_max_a2.v1_to_v4.0.tsv```
