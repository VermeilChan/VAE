from uuid import uuid4
from zipfile import ZipFile
from rarfile import RarFile
from py7zr import SevenZipFile
from tarfile import open as TarFile
from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor
from os import path, makedirs, rename, getcwd, listdir

excluded_directories = {"Bin", "Leftover", "_internal"}
archive_handlers = {
    ".zip": ZipFile,
    ".rar": RarFile,
    ".7z": SevenZipFile,
    ".tar": TarFile,
    ".gz": TarFile,
    ".xz": TarFile,
}

def extract_archive(archive_path, extract_path):
    ext = path.splitext(archive_path)[1]
    archive_handler = archive_handlers.get(ext)

    try:
        with archive_handler(archive_path, "r") as archive:
            archive.extractall(extract_path)
    except Exception as e:
        print(f"Failed to extract {archive_path}: {e}")

def process_archive(archive, leftover_path):
    unique_name = uuid4().hex
    extract_path = path.join(path.dirname(archive), unique_name)
    makedirs(extract_path, exist_ok=True)
    extract_archive(archive, extract_path)
    rename(archive, path.join(leftover_path, path.basename(archive)))

def main():
    archive_format = set(archive_handlers.keys())
    current_directory = getcwd()
    leftover_path = path.join(current_directory, "Leftover")
    makedirs(leftover_path, exist_ok=True)

    archives = [
        path.join(current_directory, file)
        for file in listdir(current_directory)
        if path.isfile(path.join(current_directory, file)) and
        any(file.endswith(ext) for ext in archive_format) and
        not any(excluded_directory in path.join(current_directory, file).split(path.sep) for excluded_directory in excluded_directories)
    ]

    workers = max(1, cpu_count())

    with ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(lambda archive: process_archive(archive, leftover_path), archives)

if __name__ == "__main__":
    main()
