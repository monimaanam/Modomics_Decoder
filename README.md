
Installation
----------------------------------------------------------------
```
git clone https://github.com/monimaanam/Modomics_Decoder
```

Modomics_Decoder.py 
----------------------------------------------------------------
This script will take any pasted unicode Modomics RNA sequence (from: https://genesilico.pl/modomics/sequences/) and annotate each modified position for easy viewing. Enter an RNA unicode sequence of interest (e.g., GGGGCUAU...) when prompted or through the command line interface. A second prompt will display all nucleotide positions enumerated, highlighting modified base positions.

Command Line Interface
----------------------------------------------------------------
```
USAGE: 
    python Modomics_Decoder.py
    python Modomics_Decoder.py --input <rna_sequence> --all
    python Modomics_Decoder.py -i <rna_sequence> -a > output_filename.txt
          
FLAGS: (optional)
    none             If flags are excluded, the program will provide input prompts. 
    -h --help:       Displays the help menu (usage, flags, arguments). 
    -i --input:      Input RNA sequence as argument. RNA sequences must be in MODOMICS code. 
    -a --all:        Displays both the modifications table and the sequence positions list. 
    -t --table:      Displays only the modifications table without the sequence positions list
    -l --list:       Displays only the enumerated sequence position list without the modifications table.
    -v --version:    Displays the current version (Version 1.1). 
```

Example Output
----------------------------------------------------------------
```
UNICODE Sequence: GGGGCUAUAGCUCAGCDGGGAGAGCGCCUGCUUVGCACGCAGGAG7UCUGCGGTPCGAUCCCGCAUAGCUCCACCA

position: 45 | symbol: 7 | short names: ['m7G', 'pm7G']
position: 16 | symbol: D | short names: ['pD', 'D']
position: 54 | symbol: P | short names: ['Y', 'pY']
position: 53 | symbol: T | short names: ['m5U', 'pm5U']
position: 33 | symbol: V | short names: ['pcmo5U', 'cmo5U']

View all positions? (Yes / No) Yes

(0, 'G')
(1, 'G')
(2, 'G')
(3, 'G')
(4, 'C')
(5, 'U')
(6, 'A')
(7, 'U')
(8, 'A')
(9, 'G')
(10, 'C')
(11, 'U')
(12, 'C')
(13, 'A')
(14, 'G')
(15, 'C')
(16, 'D') * mod
(17, 'G')
(18, 'G')
(19, 'G')
(20, 'A')
(21, 'G')
(22, 'A')
(23, 'G')
(24, 'C')
(25, 'G')
(26, 'C')
(27, 'C')
(28, 'U')
(29, 'G')
(30, 'C')
(31, 'U')
(32, 'U')
(33, 'V') * mod
(34, 'G')
(35, 'C')
(36, 'A')
(37, 'C')
(38, 'G')
(39, 'C')
(40, 'A')
(41, 'G')
(42, 'G')
(43, 'A')
(44, 'G')
(45, '7') * mod
(46, 'U')
(47, 'C')
(48, 'U')
(49, 'G')
(50, 'C')
(51, 'G')
(52, 'G')
(53, 'T') * mod
(54, 'P') * mod
(55, 'C')
(56, 'G')
(57, 'A')
(58, 'U')
(59, 'C')
(60, 'C')
(61, 'C')
(62, 'G')
(63, 'C')
(64, 'A')
(65, 'U')
(66, 'A')
(67, 'G')
(68, 'C')
(69, 'U')
(70, 'C')
(71, 'C')
(72, 'A')
(73, 'C')
(74, 'C')
(75, 'A')
```
