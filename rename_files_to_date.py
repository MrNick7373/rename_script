import os, sys, time
from rename_lib import *

def to_str(number: int) -> str:
    if number < 10:
        return f"0{number}"
    else:
        return f"{number}"

def create_name_from_modification_date(path: Path) -> str:
    date = time.gmtime(os.path.getmtime(path))
    date_str = f"{date.tm_year}{to_str(date.tm_mon)}{to_str(date.tm_mday)}"
    time_str = f"{to_str(date.tm_hour)}{to_str(date.tm_min)}{to_str(date.tm_sec)}"
    return f"{date_str}_{time_str}"

def rename_files_to_date(path_list: list[Path], name_prefix: str):
    for path in path_list:
        rename_file(path, create_path(path, create_name_from_modification_date(path), name_prefix))

if __name__ == "__main__":
    args = sys.argv[1:]
    default_prefix = ""
    if len(args) > 0:
        default_prefix = args[0]
    rename_files_to_date(get_files_from_directory(), default_prefix)
