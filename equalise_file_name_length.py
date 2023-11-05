import sys
from rename_lib import *

def equalise_date(date_str: str, digits: int) -> str:
    while date_str.__len__() < digits:
        date_str += "0"
    while date_str.__len__() > digits:
        date_str = date_str[:-1]
    return date_str

def create_new_path(path: Path, default_prefix: str, default_digits: int) -> Path:
    stem_list = path.stem.split("_")
    new_date = equalise_date(stem_list[stem_list.__len__() - 1], default_digits)
    index: int = 0
    for entry in stem_list:
        if index == stem_list.__len__() - 1:
            break
        default_prefix += f"{entry}_"
        index += 1
    default_prefix += new_date
    return create_path(path, default_prefix)

def equalise_file_name_length(path_list: list[Path], default_prefix: str, default_digits: int):
    for path in path_list:
        rename_file(path, create_new_path(path, default_prefix, default_digits))

if __name__ == "__main__":
    args = sys.argv[1:]
    default_digits = 6
    default_prefix = ""
    if len(args) > 0:
        default_digits = int(args[0])
    if len(args) > 1:
        default_prefix = args[1]
    equalise_file_name_length(get_files_from_directory(), default_prefix, default_digits)
