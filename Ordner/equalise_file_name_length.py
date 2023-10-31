from rename_lib import *

def equalise_date(date_str: str, digits: int = 6) -> str:
    while date_str.__len__() < digits:
        date_str += "0"
    while date_str.__len__() > digits:
        date_str = date_str[:-1]
    return date_str

def create_new_path(path: Path) -> Path:
    stem_list = path.stem.split("_")
    new_date = equalise_date(stem_list[stem_list.__len__() - 1])
    new_name = ""
    index: int = 0
    for entry in stem_list:
        if index == stem_list.__len__() - 1:
            break
        new_name += f"{entry}_"
        index += 1
    new_name += new_date
    return create_path(path, new_name)

def equalise_file_name_length(path_list: list[Path]):
    for path in path_list:
        rename_file(path, create_new_path(path))

if __name__ == "__main__":
    equalise_file_name_length(get_files_from_directory())
