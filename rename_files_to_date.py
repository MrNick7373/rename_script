import os, time, sys
from pathlib import Path

def to_str(number: int) -> str:
    if number < 10:
        return f"0{number}"
    else:
        return f"{number}"
    
def create_name_from_creation_date(path: Path, name_prefix: str) -> str:
    date = time.gmtime(os.path.getctime(path))
    date_str = f"{date.tm_year}{to_str(date.tm_mon)}{to_str(date.tm_mday)}"
    time_str = f"{to_str(date.tm_hour)}{to_str(date.tm_min)}{to_str(date.tm_sec)}"
    return f"{path.parent}\\{name_prefix}{date_str}_{time_str}{path.suffix}"

def rename_files_to_date(directory: Path, name_prefix: str):
    path_list = [Path(os.path.join(directory, file)) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
    for path in path_list:
        if path == Path(__file__):
            continue
        new_path = Path(create_name_from_creation_date(path, name_prefix))
        if new_path.exists():
            print(f"skipped >{path.stem}{path.suffix}<")
        else:
            print(f"renamed >{path.stem}{path.suffix}< to >{new_path.stem}{new_path.suffix}<")
            path.rename(new_path)

if __name__ == "__main__":
    args = sys.argv[1:]
    default_prefix = ""
    if len(args) > 0:
        default_prefix = args[0]
    rename_files_to_date(Path(__file__).parent, default_prefix)
