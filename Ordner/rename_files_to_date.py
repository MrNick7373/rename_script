import os, time, sys
from pathlib import Path

def to_str(number: int) -> str:
    if number < 10:
        return f"0{number}"
    else:
        return f"{number}"
    
def create_path(path: Path, name: str, name_prefix: str = "") -> Path:
    return Path(f"{path.parent}\\{name_prefix}{name}{path.suffix}")

def create_name_from_modification_date(path: Path) -> str:
    date = time.gmtime(os.path.getmtime(path))
    date_str = f"{date.tm_year}{to_str(date.tm_mon)}{to_str(date.tm_mday)}"
    time_str = f"{to_str(date.tm_hour)}{to_str(date.tm_min)}{to_str(date.tm_sec)}"
    return f"{date_str}_{time_str}"

def create_new_path(path: Path, name_prefix: str) -> Path:
    return create_path(path, create_name_from_modification_date(path), name_prefix)

def get_files_from_directory(directory: Path = Path(__file__).parent) -> list[Path]:
    return [Path(os.path.join(directory, file)) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

def rename_file(old_path: Path, new_path: Path):
    if old_path == Path(__file__):
        return
    if new_path.exists():
        print(f"skipped >{old_path.stem}{old_path.suffix}<")
    else:
        print(f"renamed >{old_path.stem}{old_path.suffix}< to >{new_path.stem}{new_path.suffix}<")
        old_path.rename(new_path)

def rename_files_to_date(path_list: list[Path], name_prefix: str):
    for path in path_list:
        rename_file(path, create_new_path(path, name_prefix))

if __name__ == "__main__":
    args = sys.argv[1:]
    default_prefix = ""
    if len(args) > 0:
        default_prefix = args[0]
    rename_files_to_date(get_files_from_directory(), default_prefix)
