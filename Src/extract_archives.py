from time import time
from uuid import uuid4
from pathlib import Path
from zipfile import ZipFile
from rarfile import RarFile
from py7zr import SevenZipFile
from tarfile import open as TarFile
from concurrent.futures import ThreadPoolExecutor


def extract_archive(archive_path, extract_path):
    try:
        if archive_path.suffix == ".zip":
            with ZipFile(archive_path, "r") as archive:
                archive.extractall(extract_path)
        elif archive_path.suffix == ".rar":
            with RarFile(archive_path, "r") as archive:
                archive.extractall(extract_path)
        elif archive_path.suffix == ".7z":
            with SevenZipFile(archive_path, "r") as archive:
                archive.extractall(extract_path)
        elif archive_path.suffix == ".tar":
            with TarFile(archive_path, "r") as archive:
                archive.extractall(extract_path)
    except Exception as e:
        print(f"Failed to extract {archive_path}: {e}")


def process_archive(archive, leftover_path):
    unique_name = uuid4().hex
    extract_path = archive.parent / unique_name
    extract_path.mkdir(exist_ok=True)
    extract_archive(archive, extract_path)
    archive.rename(leftover_path / archive.name)


def main():
    start_time = time()
    archive_extensions = {".zip", ".rar", ".7z", ".tar"}
    current_directory = Path.cwd()
    leftover_path = current_directory / "Leftover"
    leftover_path.mkdir(exist_ok=True)

    archives = [
        file
        for file in current_directory.iterdir()
        if file.suffix in archive_extensions
        and file.name not in [f.name for f in leftover_path.iterdir()]
    ]

    with ThreadPoolExecutor() as executor:
        executor.map(lambda archive: process_archive(archive, leftover_path), archives)

    end_time = time()
    print(f"Processed {len(archives)} archives in {end_time - start_time:.2f} seconds.")


if __name__ == "__main__":
    main()
