import os
from pathlib import Path
import argparse

def sort(folder_path: str):
    folder = Path(folder_path)
    for file_name in os.listdir(folder):
        file_path = folder / file_name
        if file_path.is_file():
            extension = file_path.suffix
            if extension:
                extension = extension[1:].lower()
            else:
                extension = "no_ext"
            
            target_dir = folder / extension
            if not target_dir.exists():
                target_dir.mkdir()
            try:
                new_path = target_dir / file_name
                file_path.rename(new_path)
            except OSError as e:
                print(f"Ошибка перемещения {file_name}: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Путь до папки для сортировки')
    args = parser.parse_args()
    folder_path = args.path
    sort(folder_path=folder_path)
