# CoordTransfer - основной скрипт для перевода координат и заполнения таблицы
## Описание CoordTransfer

CoordTransfer предназначен для перевода координат геномных регионов с одной сборки генома на другую, которая считается эталонной. Он принимает в качестве входных данных файл с исходными координатами и название исходной сборки, для которой существует chain-файл (необходимый для преобразования координат). 
```
CoordTransfer/                 
├── CoordTransfer/                 
│   ├── __init__.py                 
│   ├── coordtransfer.py        # Главный скрипт, отвечающий за обработку аргументов и выполнение функций                 
│   ├── io_utils.py             # Функции для чтения и записи файлов                 
│   ├── bed_converter.py        # Функция для создания BED файла                 
│   ├── coord_converter.py      # Функция для преобразования координат через crossmap                 
│   ├── chain_files.py          # Модуль, где хранится словарь с путями к chain файлам                                  
├── data/
│   ├── soybean.tsv             # Пример входного файла
├────── results/               
│  	 ├── soybean_v4.tsv          # Пример выходного файла
│  	 ├── soybean_v4.tsv_temp     # Пример выходного файла (результат после crossmap)
├── Chain_files/                 
│   ├── Glycine_max_a1.v1.fasta.to.GCF_000004515.6_Glycine_max_v4.0_genomic.unmasked.fna.over.chain                 
│   ├── GCF_000511025.2_RefBeet-1.2.2_genomic.fna.to.GCF_026745355.1_EL10.2_genomic.unmasked.fna.over.chain                 
├── CoordTransfer_env.yml       # Файл для создания окружения Conda                 
├── setup.py                    # Скрипт для установки пакета                 
```

**Шаги работы скрипта:**
1. **Чтение входного файла**:   
    На вход скрипту подается файл в формате <file_name>.tsv (пример файла: /Converting_Genome_Coordinates_pipeline/CoordTransfer/data/soybean.tsv), содержащий координаты геномных регионов. В файле обязательно должны присутствовать столбцы:
    - chr_original — название хромосомы в исходной сборке      
    - pos_original — начальная позиция региона в исходной сборке      
    - pos_original_end — конечная позиция региона в исходной сборке      
2. **Создание BED файла**:         
    Скрипт извлекает данные из столбцов chr_original, pos_original и pos_original_end входного файла и создает на их основе новый файл в формате <file_name>.bed. Этот файл будет содержать:
    - chr_original — название хромосомы в исходной сборке      
    - pos_original — начальная позиция региона в исходной сборке      
    - pos_original_end — конечная позиция региона в исходной сборке      
    Созданный .bed файл именуется аналогично входному файлу (<file_name>.bed).
3. **Преобразование координат с использованием chain-файла**:      
    На основе созданного .bed файла и соответствующего chain файла для заданной сборки скрипт с использованием crossmap выполняет перевод координат с исходной сборки на целевую.       
    Преобразованные координаты записываются в новые столбцы:        
    - chr_id — название хромосомы в целевой сборке      
    - pos_start — начальная позиция региона в целевой сборке     
    - pos_end — конечная позиция региона в целевой сборке     
4. **Сохранение результатов**:        
    После преобразования координат скрипт создает новый .tsv файл под именем <file_name_assembly>.tsv, где assembly — название целевой сборки. В этот файл записываются все исходные данные, а также новые столбцы с преобразованными координатами (chr_id, pos_start, pos_end).

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
pip install .
```
## Использование CoordTransfer
```
coordtransfer [-h] [-a] <file_name>.tsv

arguments:
  -h, --help            Show this help message and exit
  -a, --assembly        The name of the old genomic assembly

  <file_name>.tsv       Input file
```
Пример использования:
```
coordtransfer -a soybean_a1v1 soybean.tsv
```
В результате выйдет файл soybean_Glycine_max_v4.0.tsv

Список геномных сборок, для которых есть chain файл: 
```
# Soybean
  'soybean_a1v1': '/Converting_Genome_Coordinates_pipeline/CoordTransfer/Chain_files/Glycine_max_a1.v1.fasta.to.GCF_000004515.6_Glycine_max_v4.0_genomic.unmasked.fna.over.chain',
  'soybean_a2v1': '/Converting_Genome_Coordinates_pipeline/CoordTransfer/Chain_files/Glycine_max_a2.v1.fasta.to.GCF_000004515.6_Glycine_max_v4.0_genomic.unmasked.fna.over.chain',
# Sugar beet
  'refbeet1.2.2' : '/Converting_Genome_Coordinates_pipeline/CoordTransfer/Chain_files/GCF_000511025.2_RefBeet-1.2.2_genomic.fna.to.GCF_026745355.1_EL10.2_genomic.unmasked.fna.over.chain',
```

Соя переводится на сборку Glycine_max_v4.0, свекла - EL10.2.


```
coordtransfer [-h] -a <assembly_name> <input_file>.tsv <output_file>.tsv
```
Аргументы
```
-h, --help: Показать справку по использованию и выйти.
-a, --assembly: Название исходной геномной сборки. Должно совпадать с одним из доступных chain файлов (см. список ниже).
<input_file>.tsv: Входной файл в формате TSV с координатами геномных регионов. Файл должен содержать столбцы:
chr_original — название хромосомы в исходной сборке,
pos_original — начальная позиция региона в исходной сборке,
pos_original_end — конечная позиция региона в исходной сборке.
<output_file>.tsv: Имя выходного файла, куда будут записаны преобразованные координаты.
```
Пример использования
```
coordtransfer -a soybean_a1v1 soybean.tsv output.tsv
```
В результате создается файл output.tsv, содержащий все исходные данные из soybean.tsv, а также столбцы с преобразованными координатами:        
chr_id — название хромосомы в целевой сборке,        
pos_start — начальная позиция региона в целевой сборке,        
pos_end — конечная позиция региона в целевой сборке.        

Доступные сборки и chain файлы        
На данный момент поддерживаются следующие геномные сборки с их соответствующими chain файлами:      
```
# Soybean:
soybean_a1v1: ./Converting_Genome_Coordinates_pipeline/CoordTransfer/Chain_files/Glycine_max_a1.v1.fasta.to.GCF_000004515.6_Glycine_max_v4.0_genomic.unmasked.fna.over.chain
soybean_a2v1: ./Converting_Genome_Coordinates_pipeline/CoordTransfer/Chain_files/Glycine_max_a2.v1.fasta.to.GCF_000004515.6_Glycine_max_v4.0_genomic.unmasked.fna.over.chain
# Sugar beet:
refbeet1.2.2: ./Converting_Genome_Coordinates_pipeline/CoordTransfer/Chain_files/GCF_000511025.2_RefBeet-1.2.2_genomic.fna.to.GCF_026745355.1_EL10.2_genomic.unmasked.fna.over.chain
```
Целевые сборки
Для сои преобразование выполняется на сборку Glycine_max_v4.0.
Для сахарной свеклы преобразование выполняется на сборку EL10.2.

## Сравнение CoordTransfer с SNPLift
![image](https://github.com/user-attachments/assets/898f89e8-4a5f-4d15-ad0c-672940bf3e5d)


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
