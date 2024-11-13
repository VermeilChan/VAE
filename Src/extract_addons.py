from time import time
from uuid import uuid4
from shutil import move
from platform import system
from subprocess import run, CalledProcessError
from concurrent.futures import ThreadPoolExecutor
from os import path, rename, listdir, makedirs, walk, getcwd, rmdir

def get_executable(executable_name):
    os_to_executable = {
        "Windows": f"{executable_name}.exe",
        "Darwin": executable_name,
        "Linux": executable_name,
    }
    executable_path = path.join("Bin", system(), os_to_executable[system()])
    
    if not path.exists(executable_path):
        executable_path = input(
            f"{executable_name} not found.\nProvide the path to {executable_name} executable: "
        ).strip()
        
        if not path.exists(executable_path):
            raise FileNotFoundError(f"Executable not found: {executable_path}")
    
    return executable_path

def extract_gma_bin(
    file_path,
    extracted_addons_path,
    leftover_path,
    gmad_executable,
    seven_zip_executable,
):
    unique_name = uuid4().hex
    renamed_file_path = path.join(path.dirname(file_path), f"{unique_name}{path.splitext(file_path)[1]}")
    move(file_path, renamed_file_path)
    output_path = path.join(extracted_addons_path, unique_name)
    makedirs(output_path, exist_ok=True)

    try:
        if path.splitext(renamed_file_path)[1] == ".gma":
            run(
                [
                    gmad_executable,
                    "extract",
                    "-file",
                    renamed_file_path,
                    "-out",
                    output_path,
                ],
                check=True,
            )
        else:
            run(
                [seven_zip_executable, "x", renamed_file_path, f"-o{output_path}"],
                check=True,
            )
            for extracted_file in listdir(output_path):
                extracted_file_path = path.join(output_path, extracted_file)
                if path.isfile(extracted_file_path) and not path.splitext(extracted_file_path)[1]:
                    new_gma_path = f"{extracted_file_path}.gma"
                    rename(extracted_file_path, new_gma_path)
                    extract_gma_bin(
                        new_gma_path,
                        extracted_addons_path,
                        leftover_path,
                        gmad_executable,
                        seven_zip_executable,
                    )
    except CalledProcessError as e:
        print(f"Extraction failed for {renamed_file_path}: {e}")

    move(renamed_file_path, path.join(leftover_path, path.basename(renamed_file_path)))

def remove_empty_folders(directory):
    for root, dirs, _ in walk(directory, topdown=False):
        for directory_name in dirs:
            directory_path = path.join(root, directory_name)
            if not listdir(directory_path):
                rmdir(directory_path)

def main():
    start_time = time()
    current_directory = getcwd()
    extracted_addons_path = path.join(current_directory, "Extracted-Addons")
    leftover_path = path.join(current_directory, "Leftover")
    makedirs(extracted_addons_path, exist_ok=True)
    makedirs(leftover_path, exist_ok=True)

    gmad_executable = get_executable("fastgmad")
    seven_zip_executable = get_executable("7zz")

    files_to_extract = [
        path.join(root, file)
        for root, _, files in walk(current_directory)
        for file in files
        if path.splitext(file)[1] in {".gma", ".bin"}
    ]

    if not files_to_extract:
        return

    with ThreadPoolExecutor() as executor:
        executor.map(
            lambda file_path: extract_gma_bin(
                file_path,
                extracted_addons_path,
                leftover_path,
                gmad_executable,
                seven_zip_executable,
            ),
            files_to_extract,
        )

    remove_empty_folders(current_directory)
    print(f"Processed {len(files_to_extract)} files in {time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()
