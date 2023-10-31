# Scripts to rename huge amounts of files

---
# General
- the files need to be in the same folder as the script
- the scripts need the rename_lib.py file to run

# Functionality of the scripts
## rename_files_to_date.py
- renames the file to the date when it was last modified
- in the format: YYYYMMDD_HHMMSS
- if called from the terminal, a prefix can be declared:  
-> 'rename_files_to_date.py IMG_' results in files been called 'IMG_YYYYMMDD_HHMMSS'

## rename_files_ascending.py
- renames the file ascendingly
- in the format: NNN
- if called from the terminal, a prefix can be declared:  
-> 'rename_files_ascending.py IMG_' results in files been called 'IMG_NNN'

## equalise_file_name_length.py
- extends or truncates the file name to 6 charakters
- if the name contains any '_', the last section will be modified:  
'ABC_DE_123456789' -> 'ABC_DE_123456'  
'ABC_1234' -> 'ABC_123400'
