# ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- #

# Importing libraries
import getopt
import sys

# Dictionary (modified from modomics website)
mod_dict = {'!': ['cmnm5U', 'pcmnm5U'],
 '#': ['Gm', 'pGm'],
 '$': ['cmnm5s2U', 'pcmnm5s2U'],
 '&': ['ncm5U', 'pncm5U'],
 '(': ['G+', 'pG+'],
 ')': ['cmnm5Um', 'pcmnm5Um'],
 '*': ['pms2i6A', 'ms2i6A'],
 '.': ['N'],
 '1': ['mcm5U', 'pmcm5U'],
 '2': ['ps2U', 's2U'],
 '3': ['pmcm5s2U', 'mcm5s2U'],
 '4': ['s4U', 'ps4U'],
 '5': ['mo5U', 'pmo5U'],
 '6': ['t6A', 'pt6A'],
 '7': ['m7G', 'pm7G'],
 '8': ['manQ', 'pmanQ'],
 '9': ['galQ', 'pgalQ'],
 '>': ['f5C', 'pf5C'],
 '?': ['m5C', 'pm5C'],
 'B': ['Cm', 'pCm'],
 'D': ['pD', 'D'],
 'E': ['m6t6A', 'pm6t6A'],
 'F': ['m5s2U', 'pm5s2U'],
 'H': ['xA'],
 'I': ['I', 'pI'],
 'J': ['Um', 'pUm'],
 'K': ['m1G', 'pm1G'],
 'L': ['pm2G', 'm2G'],
 'M': ['pac4C', 'ac4C'],
 'N': ['xU'],
 'O': ['m1I', 'pm1I'],
 'P': ['Y', 'pY'],
 'Q': ['Q', 'pQ'],
 'R': ['m2,2G', 'pm2,2G'],
 'S': ['mnm5s2U', 'pmnm5s2U'],
 'T': ['m5U', 'pm5U'],
 'V': ['pcmo5U', 'cmo5U'],
 'W': ['o2yW', 'po2yW'],
 'X': ['acp3U', 'pacp3U'],
 'Y': ['yW', 'pyW'],
 'Z': ['Ym', 'pYm'],
 '[': ['ms2t6A', 'pms2t6A'],
 ']': ['m1Y', 'pm1Y'],
 'b': ['mchm5Um', 'pmchm5Um'],
 'e': ['ct6A', 'pct6A'],
 'f': ['cmnm5ges2U', 'pcmnm5ges2U'],
 'h': ['mnm5ges2U', 'pmnm5ges2U'],
 'l': ['ncm5s2U', 'pncm5s2U'],
 'm': ['pN'],
 'r': ['nchm5U', 'pnchm5U'],
 'y': ['OHyWy', 'pOHyWy'],
 '{': ['pmnm5U', 'mnm5U'],
 '|': ['m2,2Gm', 'pm2,2Gm'],
 '}': ['k2C', 'pk2C'],
 '~': ['ncm5Um', 'pncm5Um'],
 '¡': ['hm5Cm', 'phm5Cm'],
 '£': ['msms2i6A', 'pmsms2i6A'],
 '¥': ['yW-86', 'pyW-86'],
 '§': ['mpppN'],
 '©': ['m7GpppN'],
 '«': ['ht6A', 'pht6A'],
 '®': ['m2,7GpppN'],
 '°': ['f5Cm', 'pf5Cm'],
 '±': ['m2,8A', 'pm2,8A'],
 '¶': ['m2,2,7GpppN'],
 '¾': ['inm5U', 'pinm5U'],
 '¿': ['C+', 'pC+'],
 'Ç': ['ho5C', 'pho5C'],
 'Ð': ['acp3D', 'pacp3D'],
 'Þ': ['acp3Y', 'pacp3Y'],
 'â': ['m8A', 'pm8A'],
 'æ': ['m2,7Gm', 'pm2,7G'],
 'ÿ': ['ms2ct6A', 'pms2ct6A'],
 'Ħ': ['pm5Um', 'm5Um'],
 'Ĳ': ['AppppN'],
 'œ': ['m1Am', 'pm1Am'],
 'š': ['OHyWx', 'pOHyWx'],
 'Ƈ': ['ppG'],
 'Ƒ': ['m3Y', 'pm3Y'],
 'ƕ': ['tm5s2U', 'ptm5s2U'],
 'Ɲ': ['inm5s2U', 'pinm5s2U'],
 'Ƣ': ['phm5C', 'hm5C'],
 'ƿ': ['pppA'],
 'Ȝ': ['pppG'],
 'Ⱥ': ['pGp'],
 'ɀ': ["5'-OH-N"],
 'Ʉ': ['pG(pN)'],
 'ɮ': ['mchm5U', 'pmchm5U'],
 'ɿ': ['m2A', 'pm2A'],
 'ʆ': ['xG'],
 'ʍ': ['Am', 'pAm'],
 'ʤ': ['s2C', 'ps2C'],
 'ʩ': ['pAr(p)', 'Ar(p)'],
 'ʭ': ['tm5U', 'ptm5U'],
 'Γ': ['ges2U', 'pges2U'],
 'Δ': ['nm5ges2U', 'pnm5ges2U'],
 'Ξ': ['NADpN'],
 'Ω': ['yW-72', 'pyW-72'],
 'α': ['m1acp3Y', 'pm1acp3Y'],
 'β': ['m4,4Cm', 'pm4,4Cm'],
 'γ': ['m2Gm', 'pm2Gm'],
 'δ': ['m3U', 'pm3U'],
 'ε': ['m1Gm', 'pm1Gm'],
 'ζ': ['pm6,6A', 'm6,6A'],
 'η': ['m6,6Am', 'pm6,6Am'],
 'λ': ['pm4Cm', 'm4Cm'],
 'μ': ['pm4,4C', 'm4,4C'],
 'ν': ['pm4C', 'm4C'],
 'ξ': ['m1Im', 'pm1Im'],
 'π': ['nm5se2U', 'pnm5se2U'],
 'ρ': ['m5D', 'pm5D'],
 'ς': ['oQ', 'poQ'],
 'σ': ['m3Um', 'pm3Um'],
 'τ': ['m5Cm', 'pm5Cm'],
 'υ': ['mcmo5U', 'pmcmo5U'],
 'φ': ['preQ0', 'ppreQ0'],
 'χ': ['m6Am', 'pm6Am'],
 'ψ': ['preQ0base'],
 'ω': ['pse2U', 'se2U'],
 'ϑ': ['GpppN'],
 'ϒ': ['ppN'],
 'ϓ': ['pyyW'],
 'ϖ': ['pppN'],
 'Ϙ': ['m6AppppN'],
 'Ϛ': ['m6ApppppN'],
 'Ϟ': ['m7GppppN'],
 'Ϩ': ['ApppN', 'f6A', 'pf6A'],
 'Ϫ': ['hm6A', 'phm6A'],
 'Ϭ': ['ApppppN'],
 'Ϯ': ['m6ApppN'],
 'Ͽ': ['mcmo5Um', 'pmcmo5Um'],
 'Ж': ['m6A', 'pm6A'],
 'Ч': ['pi6A', 'i6A'],
 'Ш': ['Im', 'pIm'],
 'Щ': ['m3C', 'pm3C'],
 'Ю': ['inm5Um', 'pinm5Um'],
 'Ѣ': ['m1A', 'pm1A'],
 'Ѩ': ['Xm'],
 'Ѯ': ['xX'],
 'Ѵ': ['xC'],
 'Ѷ': ['cnm5U', 'pcnm5U'],
 'Ѽ': ['mmpN'],
 'Ѿ': ['mpN'],
 'Ҋ': ["pU2'3'cp"],
 'Ҏ': ["pC2'3'cp"],
 'Ґ': ["pG2'3'cp"],
 'Ғ': ["N2'3'cp"],
 'Ҕ': ["pA2'3'cp"],
 'Ợ': ['pAp'],
 'Ỽ': ['io6A', 'pio6A'],
 '†': ['imG-14', 'pimG-14'],
 '€': ['imG', 'pimG'],
 'ℑ': ['Gr(p)', 'pGr(p)'],
 '℘': ['cm5s2U', 'pcm5s2U'],
 'ℵ': ['pac4Cm', 'ac4Cm'],
 '⇑': ['yW-58', 'pyW-58'],
 '⇓': ['ac6A', 'pac6A'],
 '∇': ['preQ1base'],
 '∉': ['preQ1', 'ppreQ1'],
 '∏': ['s2Um', 'ps2Um'],
 '∑': ['mimG', 'pmimG'],
 '√': ['hn6A', 'phn6A'],
 '∝': ['ho5U', 'pho5U'],
 '∞': ['ms2m6A', 'pms2m6A'],
 '∠': ['m2,2,7G', 'pm2,2,7G'],
 '∨': ['pm2,7Gm', 'm2,7G'],
 '∩': ['mcm5Um', 'pmcm5Um'],
 '∪': ['nm5U', 'pnm5U'],
 '∫': ['nm5s2U', 'pnm5s2U'],
 '∴': ['Qbase'],
 '≅': ['mnm5se2U', 'pmnm5se2U'],
 '≈': ['ms2hn6A', 'pms2hn6A'],
 '≠': ['ms2io6A', 'pms2io6A'],
 '≡': ['g6A', 'pg6A'],
 '≥': ['chm5U', 'pchm5U'],
 '⊄': ['gluQ', 'pgluQ'],
 '⊆': ['OHyW', 'pOHyW'],
 '⊇': ['imG2', 'pimG2'],
 '⊥': ['cmnm5se2U', 'pcmnm5se2U'],
 '◊': ['cm5U', 'pcm5U'],
 '♠': ['CoApN'],
 '♣': ['acCoApN'],
 '♥': ['malonyl-CoApN'],
 '♦': ['succinyl-CoApN']}

# ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- #

# Setting flags for option arguments
argv = sys.argv[1:]
options, args = getopt.getopt(argv, 
                              "i:atlhv", 
                              ["input=", "all", "table", "list", "help", "version"])    
                          
# ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- #

# If user includes a specific flag argument, switch the specific flag variable to "True"

input_flag = False # default off 
all_flag = False
table_flag = False
list_flag = False
help_flag = False
version_flag = False
no_flag = False 

for flag, argument in options: # switch on
    if flag in ['-i', '--input']:
        input_flag = True 
    if flag in ['-a', '--all']:
        all_flag = True
    if flag in ['-t', '--table']:
        table_flag = True
    if flag in ['-l', '--list']:
        list_flag = True
    if flag in ['-h', '--help']:
        help_flag = True
    if flag in ['-v', '--version']:
        version_flag = True

no_flag = not (input_flag or all_flag or table_flag or list_flag or help_flag or version_flag)

# ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- #

# Displaying the help page
if help_flag: 
    print('''
Modomics Sequence Decoder | Version 1.1        
----------------------------------------------------------------------------------------------
Processes any RNA sequence from MODOMICS database (https://genesilico.pl/modomics/sequences/) 
and outputs readable visualization of modifications and nucleotide positions. 
----------------------------------------------------------------------------------------------                               
                                                https://github.com/monimaanam/Modomics_Decoder   
            
USAGE: 
    python Modomics_Decoder.py
    python Modomics_Decoder.py --input <rna_sequence> --all
    python Modomics_Decoder.py -i <rna_sequence> -a > output_filename.txt
          
FLAGS: (optional)
    none             If flags are excluded, the script will prompt for inputs. 
    -h --help:       Displays the help menu (usage, flags, arguments). 
    -i --input:      Input RNA sequence as argument. RNA sequences must be in MODOMICS code. 
    -a --all:        Displays both the modifications table and the sequence positions list. 
    -t --table:      Displays the modifications table.
    -l --list:       Displays the enumerated sequence position list.
    -v --version:    Displays the current version (Version 1.1). 

SAVING OUTPUTS:
    Use '>' to write outputs to files; -i argument will be required along with -a, -t, or -l.
''')
    exit()
    
# ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- #

# Displaying the version information
if version_flag:
    print('\nModomics Sequence Decoder - Version 1.1\n')
    exit()

# ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- #
    
# If the RNA sequence was specified by -i, store the sequence
for flag, argument in options:
    if flag in ['-i', '--input']:
        sequence = argument

if input_flag: 
    print(f'\nUNICODE Sequence: {sequence}')
    print('')

# If no -i flag was provided, prompt for the RNA sequence
if not input_flag:
    sequence = input('\nUNICODE Sequence: ')
    print('')

# ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- #

# If table should be shown, then print lines of the table using the dictionary to decode each modification
if all_flag or table_flag or no_flag or input_flag:
    for symbol, mod in mod_dict.items():
            if sequence.find(symbol) != -1:
                print(f'position: {sequence.find(symbol)} | symbol: {symbol} | short names: {mod}')   

if all_flag or table_flag or no_flag or input_flag:
    print('') # Spacer

if table_flag and not all_flag and not list_flag: # Exit if list should not be displayed
    exit()

# ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- #

# Heading for displaying the list
if all_flag or list_flag:
    print("Displaying all positions:\n")

# Prompt asking to display the list if options not specified 
if not all_flag and not list_flag and not table_flag:
    show_list = input("Display all positions? (Yes / No): ")
    show_list = show_list.lower()
    print('')

# Print the list that enumerates each position
if all_flag or list_flag or show_list == 'yes' or show_list == 'y':
    for position in enumerate(sequence): 
        if position[1] in mod_dict.keys():
            print(position, '* mod') # places * next to modified residues
        else:
            print(position)

if all_flag or list_flag or show_list == 'yes' or show_list == 'y': # Spacer
    print('') 

# ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- #


