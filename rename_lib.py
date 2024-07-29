from pathlib import Path

def index_to_str(index: int, number_of_files: int) -> str:
    index_str: str = f"{index}"
    while len(index_str) < len(f"{number_of_files}"):
        index_str = "0" + index_str
    return index_str

def create_path(path: Path, name: str, name_prefix: str = "") -> Path:
    return Path(f"{path.parent}\\{name_prefix}{name}{path.suffix}")

def is_valid_file(path: Path) -> bool:
    skip_suffix: list[str] = [".py", ".md", ".gitignore"]
    skip_name: list[str] = [".gitignore"]
    if skip_suffix.count(path.suffix) != 0 or skip_name.count(path.name) != 0:
        return False
    else:
        return True

def get_files_from_directory(directory: Path = Path(__file__).parent) -> list[Path]:
    #return [Path(os.path.join(directory, file)) for file in os.listdir(directory) if (os.path.isfile(os.path.join(directory, file)) and is_valid_file(Path(os.path.join(directory, file))))]
    paths: list[Path] = []
    for path in directory.iterdir():
        if path.is_file() and is_valid_file(path):
            paths.append(path)
    return paths
            

def rename_file(old_path: Path, new_path: Path):
    if new_path.exists():
        print(f"skipped >{old_path.stem}{old_path.suffix}<")
    else:
        print(f"renamed >{old_path.stem}{old_path.suffix}< to >{new_path.stem}{new_path.suffix}<")
        old_path.rename(new_path)
