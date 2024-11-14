from uuid import uuid4
from shutil import move
from platform import system
from subprocess import run, DEVNULL
from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor
from os import path, scandir, rename, makedirs, rmdir, listdir

current_platform = system()

def get_executable_paths():
    base_path = 'Bin'
    platform_paths = {
        'Windows': {'7zz': '7zz.exe', 'fastgmad': 'fastgmad.exe'},
        'Linux': {'7zz': '7zz', 'fastgmad': 'fastgmad'},
        'Darwin': {'7zz': '7zz', 'fastgmad': 'fastgmad'}
    }

    if current_platform not in platform_paths:
        raise Exception(f"Unsupported platform: {current_platform}.\nSupported platforms are: Windows, Linux, macOS.")

    exec_paths = {
        exe: path.join(base_path, current_platform, exe_name)
        for exe, exe_name in platform_paths[current_platform].items()
    }

    for exe, exe_path in exec_paths.items():
        if not path.exists(exe_path):
            exec_paths[exe] = input(f"Could not find {exe} at {exe_path}.\nProvide the full path to the {exe} executable: ").strip()

    return exec_paths

def generate_unique_name(file_path):
    return path.join(path.dirname(file_path), uuid4().hex + path.splitext(file_path)[-1])

def find_files_with_extension(extension, start_dir):
    files = []
    for entry in scandir(start_dir):
        if entry.is_dir() and entry.name not in ['_internal', 'Bin', 'Leftover', 'Extracted-Addons']:
            files.extend(find_files_with_extension(extension, entry.path))
        elif entry.is_file() and entry.name.endswith(extension):
            files.append(entry.path)
    return files

def add_extension_to_files_without_format(start_dir):
    for entry in scandir(start_dir):
        if entry.is_dir() and entry.name not in ['_internal', 'Bin', 'Leftover', 'Extracted-Addons']:
            add_extension_to_files_without_format(entry.path)
        elif entry.is_file() and '.' not in entry.name:
            new_path = entry.path + '.gma'
            rename(entry.path, new_path)

def extract_bin_file(bin_file, seven_zip_path):
    run([seven_zip_path, 'x', bin_file, '-o' + path.dirname(bin_file)], stdout=DEVNULL, stderr=DEVNULL)

def extract_gma_file(gma_file, fastgmad_path):
    addon_folder = path.join(path.dirname(gma_file), 'Extracted-Addons', uuid4().hex)
    makedirs(addon_folder, exist_ok=True)
    run([fastgmad_path, 'extract', '-file', gma_file, '-out', addon_folder], stdout=DEVNULL, stderr=DEVNULL)

def move_files_to_leftover(files, leftover_dir):
    makedirs(leftover_dir, exist_ok=True)
    for file in files:
        destination = path.join(leftover_dir, path.basename(file))
        if path.exists(destination):
            destination = generate_unique_name(destination)
        move(file, destination)

def remove_empty_directories(start_dir):
    for entry in scandir(start_dir):
        if entry.is_dir() and entry.name not in ['_internal', 'Bin', 'Leftover', 'Extracted-Addons']:
            remove_empty_directories(entry.path)
            if not listdir(entry.path):
                rmdir(entry.path)

def main():
    exec_paths = get_executable_paths()
    seven_zip_path = exec_paths['7zz']
    fastgmad_path = exec_paths['fastgmad']

    bin_files = find_files_with_extension('.bin', '.')
    workers = max(1, cpu_count())

    with ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(lambda bin_file: extract_bin_file(bin_file, seven_zip_path), bin_files)

    add_extension_to_files_without_format('.')

    gma_files = find_files_with_extension('.gma', '.')

    with ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(lambda gma_file: extract_gma_file(gma_file, fastgmad_path), gma_files)

    move_files_to_leftover(bin_files + gma_files, 'Leftover')

    remove_empty_directories('.')

if __name__ == "__main__":
    main()
