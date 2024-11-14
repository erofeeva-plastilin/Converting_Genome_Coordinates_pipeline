# CoordTransfer - основной скрипт для перевода координат и заполнения таблицы
## Описание CoordTransfer

CoordTransfer предназначен для перевода координат геномных регионов с одной сборки генома на другую, которая считается эталонной. Он принимает в качестве входных данных файл с исходными координатами и название **исходной** сборки, для которой существует chain-файл (необходимый для преобразования координат). Спасок возможных исходных сборок можно посмотреть в разделе **Доступные сборки и chain файлы**.
```
main
    ├──CoordTransfer/                 
    │   ├── CoordTransfer/                 
    │   │   ├── __init__.py                 
    │   │   ├── coordtransfer.py        # Главный скрипт, отвечающий за обработку аргументов и выполнение функций                 
    │   │   ├── io_utils.py             # Функции для чтения и записи файлов                 
    │   │   ├── bed_converter.py        # Функция для создания BED файла                 
    │   │   ├── coord_converter.py      # Функция для преобразования координат через crossmap                 
    │   │   ├── chain_files.py          # Словарь с путями к chain файлам                                  
    │   ├── data/
    │   │   ├── soybean.tsv             # Пример входного файла
    │   ├────── results/               
    │   │  	 ├── soybean_v4.tsv         # Пример выходного файла
    │   │  	 ├── soybean.bed            # Пример выходного .bed файла
    │   │  	 ├── soybean_v4.tsv_temp    # Пример выходного файла (результат после crossmap)
    │   ├── Chain_files/                 
    │   │   ├── Glycine_max_a1.v1.fasta.to.GCF_000004515.6_Glycine_max_v4.0_genomic.unmasked.fna.over.chain                 
    │   │   ├── GCF_000511025.2_RefBeet-1.2.2_genomic.fna.to.GCF_026745355.1_EL10.2_genomic.unmasked.fna.over.chain                 
    │   ├── CoordTransfer_env.yml       # Файл для создания окружения Conda                 
    │   ├── setup.py                    # Скрипт для установки пакета
    ├──Excel/
    │   ├── Сравнение_с_snplift.xlsx    # Сравнение качества работы CoordTransfer и SNPLift
    ├──READMY.md     
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
    На основе созданного .bed файла и соответствующего chain файла для заданной сборки скрипт с использованием crossmap выполняет перевод координат с исходной сборки на целевую (можно отдельно команду выполнить: ```CrossMap bed GCF_000511025.2_RefBeet-1.2.2_genomic.fna.to.GCF_026745355.1_EL10.2_genomic.unmasked.fna.over.chain Sugar_beet_fixed.bed > new_Sugar_beet```).       
    Преобразованные координаты записываются в новые столбцы:        
    - chr_id — название хромосомы в целевой сборке      
    - pos_start — начальная позиция региона в целевой сборке     
    - pos_end — конечная позиция региона в целевой сборке     
4. **Сохранение результатов**:        
    После преобразования координат скрипт создает новый .tsv файл под именем <file_name_assembly>.tsv, где assembly — название целевой сборки. В этот файл записываются все исходные данные, а также новые столбцы с преобразованными координатами (chr_id, pos_start, pos_end).

## Установка
**Скачивание:**
```
git clone https://github.com/erofeeva-plastilin/Converting_Genome_Coordinates_pipeline.git
```
**Установка зависимостей:**
```
cd Converting_Genome_Coordinates_pipeline/CoordTransfer
conda env create -f CoordTransfer_env.yml
conda activate CoordTransfer_env
pip install .
```
## Использование CoordTransfer

```
coordtransfer [-h] -a <assembly_name> <input_file>.tsv <output_file>.tsv
```
**Аргументы**
```
-h, --help: Показать справку
-a, --assembly: Название исходной геномной сборки. Должно совпадать с одним из доступных chain файлов (см. список ниже)
<input_file>.tsv: Входной файл в формате TSV с координатами геномных регионов. Файл должен содержать столбцы:
    chr_original — название хромосомы в исходной сборке
    pos_original — начальная позиция региона в исходной сборке
    pos_original_end — конечная позиция региона в исходной сборке
<output_file>.tsv: Имя выходного файла, куда будут записаны преобразованные координаты
```
**Доступные сборки и chain файлы**            
```
# Soybean:
soybean_a1v1: /mnt/users/erofeevan/Converting_Genome_Coordinates_pipeline/CoordTransfer/Chain_files/Glycine_max_a1.v1.fasta.to.GCF_000004515.6_Glycine_max_v4.0_genomic.unmasked.fna.over.chain
soybean_a2v1: /mnt/users/erofeevan/Converting_Genome_Coordinates_pipeline/CoordTransfer/Chain_files/Glycine_max_a2.v1.fasta.to.GCF_000004515.6_Glycine_max_v4.0_genomic.unmasked.fna.over.chain
# Sugar beet:
refbeet1.2.2: /mnt/users/erofeevan/Converting_Genome_Coordinates_pipeline/CoordTransfer/Chain_files/GCF_000511025.2_RefBeet-1.2.2_genomic.fna.to.GCF_026745355.1_EL10.2_genomic.unmasked.fna.over.chain
```
**Целевые сборки**          
Для сои преобразование выполняется на сборку Glycine_max_v4.0.
Для сахарной свеклы преобразование выполняется на сборку EL10.2.

**Пример использования**
```
cd data # сюда можно загружать необходимые таблицы  
coordtransfer -a soybean_a1v1 soybean.tsv output.tsv
```
В результате создается файл output.tsv, содержащий все исходные данные из soybean.tsv, а также столбцы с преобразованными координатами:        
chr_id — название хромосомы в целевой сборке,        
pos_start — начальная позиция региона в целевой сборке,        
pos_end — конечная позиция региона в целевой сборке.       
Кроме этого, сохраняются все промежуточные файлы - созданный .bed файл, а также результат работы crossmap.           
Скрипт поддерживает любой порядок столбцов, главное, чтобы названия не менялись и обязательно были следующие столбцы: chr_original, pos_original, pos_original_end, chr_id, pos_start, pos_end.

## Сравнение CoordTransfer с SNPLift
![image](https://github.com/user-attachments/assets/898f89e8-4a5f-4d15-ad0c-672940bf3e5d)
Сравнивая перевод 318 позиций, этот скрипт идентично snplift заполнилнил 311 позиций. Оставшиеся 7 позиций: 3 позиции snplift просто не нашел, а этот скрипт смог переести координаты, для еще 4 позиций отличие было в 1 нуклеотид (см. сравнение с snplift в папке Excel: https://github.com/erofeeva-plastilin/Converting_Genome_Coordinates_pipeline/tree/main/Excel). Скорость выполнения скрипта для этого составила 0m1.657s, что значительно быстрее snplift.

# pyOverChain - дополнительный скрипт для создания chain-файлов вручную

Скрипт не мой, он взят тут: https://github.com/billzt/pyOverChain               
**pyOverChain** — это Python-пайплайн для создания chain файлов, необходимых для перевода координат (LiftOver) между разными сборками генома. Он сопоставляет и выравниванивает последовательности из старой и новой сборки генома, чтобы установить соответствие между их координатами. Хромосомы из старой и новой сборок извлекаются и сопоставляются на основании файла chr_map, который задает, каким образом хромосомы старой сборки соответствуют хромосомам новой сборки.
Судя по коду (лучше я бы не сделала точно, поэтому беру его):                  
- faSplit: разделение новой хромосомы на сегменты для ускорения обработки               
- BLAT/pBLAT: выравнивание сегментов новой хромосомы с последовательностями старой хромосомы для поиска участков сходства                   
- liftUp: преобразование выравниваний в формате PSL для учета хромосомных позиций                    
- axtChain: создание chain файлов, которые отображают соответствия между старыми и новыми координатами               
- chainMergeSort и chainNet: объединение и сортировка цепочек выравниваний для создания финальных chain файлов               
- netChainSubset: окончательное преобразование chain файлов для генерации готового chain файла, пригодного для LiftOver               

Параллельное выполнение: для ускорения пайплайн выполняет параллельную обработку нескольких хромосом, используя заданное количество потоков для выполнения задач на уровне каждой хромосомы                                
Очистка временных файлов: после работы все временные файлы и директории удаляются               

**Аргументы командной строки:** 
```
old_genome — FASTA файл старой сборки генома
new_genome — FASTA файл новой сборки генома
chr_map — TSV файл с соответствием между хромосомами старой и новой сборок
-n, --num-chromosome-tasks — количество параллельных задач для обработки хромосом
-p, --num-threads-pblat — количество потоков для работы pblat
--disable-progress — отключение отображения прогресса 
```
## Установка 
```
git clone https://github.com/billzt/pyOverChain.git
cd pyOverChain
pip install .
mkdir ucsc_tools
cd ucsc_tools
wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/liftUp
wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/axtChain
wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/chainMergeSort
wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/chainSplit
wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/chainNet
wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/netChainSubset
wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/faSplit
chmod +x axtChain chainMergeSort chainNet chainSplit faSplit liftUp netChainSubset
echo 'export PATH=/mnt/users/erofeevan/test/pyOverChain/ucsc_tools:$PATH' >> ~/.bashrc # тут надо написать реальный путь до папки ucsc_tools
source ~/.bashrc
conda activate /mnt/users/erofeevan/miniconda3/envs/CGCp_env
cd ../
cd ../
mkdir pyoverchain_workdir
cd pyoverchain_workdir # сюдя копируем нужные две геномные сборки и файл с соответствием хоромосом этих сборок
# Например
#cp chr_map.tsv /mnt/users/erofeevan/pyoverchain_workdir/
#cp /mnt/reference/genomes/beta_vulgaris/GCF_026745355.1/GCF_026745355.1_EL10.2_genomic.unmasked.fna /mnt/users/erofeevan/pyoverchain_workdir/
#cp /mnt/users/erofeevan/Plant_culture/Sunflower/Sugar_beet/GCF_000511025.2_RefBeet-1.2.2_genomic.fna /mnt/users/erofeevan/pyoverchain_workdir/
```
**chromosome-mapping-file** - файл соответствия хромосом двух сборок
```
#old_genome_chr new_genome_chr
chr1    chr1
chr2    chr2
chr3    chr3
```
## Пример запуска 
```
cd pyoverchain_workdir # Запускать только в этой директории, иначе он выдает ошибки
time pyoverchain -n 10 -p 10  GCF_000511025.2_RefBeet-1.2.2_genomic.fna GCF_026745355.1_EL10.2_genomic.unmasked.fna chr_map.tsv
time pyoverchain -n 1 -p 20  Glycine_max_a1.v1.fasta GCF_000004515.6_Glycine_max_v4.0_genomic.unmasked.fna chr_map_Glycine_max_a1v1_to_v4.0.tsv
time pyoverchain -n 1 -p 23 Glycine_max_a2.v1.fasta GCF_000004515.6_Glycine_max_v4.0_genomic.unmasked.fna chr_map_Glycine_max_a2.v1_to_v4.0.tsv
time pyoverchain -n 7 -p 3  Pisum_sativum_v1a.fa GCF_024323335.1_CAAS_Psat_ZW6_1.0_genomic.unmasked.fna chr_map_pea.tsv
```
**Время работы:**
```
# Соя: 
real    998m38.447s
user    1661m50.487s
sys     1m4.388s
```
