import sys
from rename_lib import *

def rename_files_ascending(path_list: list[Path], name_prefix: str, index: int):
    length: int = len(path_list);
    for path in path_list:
        rename_file(path, create_path(path, index_to_str(index, length), name_prefix))
        index += 1

if __name__ == "__main__":
    args = sys.argv[1:]
    default_prefix: str = ""
    default_starting_index: int = 0
    if len(args) > 0:
        default_prefix = args[0]
    if len(args) > 1:
        default_starting_index = int(args[1])
    rename_files_ascending(get_files_from_directory(), default_prefix, default_starting_index)
    