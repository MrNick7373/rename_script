import os
from pathlib import Path

def to_str_3digits(number: int) -> str:
    if number < 10:
        return f"00{number}"
    if number < 100 and number >= 10:
        return f"0{number}"
    else:
        return f"{number}"

def to_str(number: int) -> str:
    if number < 10:
        return f"0{number}"
    else:
        return f"{number}"
    
def create_path(path: Path, name: str, name_prefix: str = "") -> Path:
    return Path(f"{path.parent}\\{name_prefix}{name}{path.suffix}")

def get_files_from_directory(directory: Path = Path(__file__).parent) -> list[Path]:
    return [Path(os.path.join(directory, file)) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

def rename_file(old_path: Path, new_path: Path):
    if old_path.suffix == ".py":
        return
    if new_path.exists():
        print(f"skipped >{old_path.stem}{old_path.suffix}<")
    else:
        print(f"renamed >{old_path.stem}{old_path.suffix}< to >{new_path.stem}{new_path.suffix}<")
        old_path.rename(new_path)
