from os import walk
from time import time
from uuid import uuid4
from shutil import move
from pathlib import Path
from platform import system
from subprocess import run, CalledProcessError
from concurrent.futures import ThreadPoolExecutor


def get_executable(executable_name):
    os_to_executable = {
        "Windows": f"{executable_name}.exe",
        "Darwin": executable_name,
        "Linux": executable_name,
    }
    executable_path = Path("Bin", system(), os_to_executable[system()])
    if not executable_path.exists():
        executable_path = Path(
            input(
                f"{executable_name} not found.\nProvide the path to {executable_name} executable: "
            ).strip()
        )
        if not executable_path.exists():
            raise FileNotFoundError(f"Executable not found: {executable_path}")
    return str(executable_path)


def extract_gma_bin(
    file_path,
    extracted_addons_path,
    leftover_path,
    gmad_executable,
    seven_zip_executable,
):
    unique_name = uuid4().hex
    renamed_file_path = file_path.with_name(f"{unique_name}{file_path.suffix}")
    move(file_path, renamed_file_path)
    output_path = extracted_addons_path / unique_name
    output_path.mkdir(parents=True, exist_ok=True)

    try:
        if renamed_file_path.suffix == ".gma":
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
                [seven_zip_executable, "x", str(renamed_file_path), f"-o{output_path}"],
                check=True,
            )
            for extracted_file in output_path.iterdir():
                if extracted_file.is_file() and not extracted_file.suffix:
                    new_gma_path = extracted_file.with_suffix(".gma")
                    extracted_file.rename(new_gma_path)
                    extract_gma_bin(
                        new_gma_path,
                        extracted_addons_path,
                        leftover_path,
                        gmad_executable,
                        seven_zip_executable,
                    )
        print(f"Extracted: {renamed_file_path}")
    except CalledProcessError as e:
        print(f"Extraction failed for {renamed_file_path}: {e}")

    move(renamed_file_path, leftover_path / renamed_file_path.name)


def remove_empty_folders(directory):
    for root, directory, _ in walk(directory, topdown=False):
        for directory_name in directory:
            directory_path = Path(root, directory_name)
            if not any(directory_path.iterdir()):
                directory_path.rmdir()


def main():
    start_time = time()
    current_directory = Path.cwd()
    extracted_addons_path = current_directory / "Extracted-Addons"
    leftover_path = current_directory / "Leftover"
    extracted_addons_path.mkdir(exist_ok=True)
    leftover_path.mkdir(exist_ok=True)

    gmad_executable = get_executable("fastgmad")
    seven_zip_executable = get_executable("7za")

    files_to_extract = [
        file
        for file in current_directory.rglob("*")
        if file.suffix in {".gma", ".bin"} and file.parent != leftover_path
    ]

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
    print(
        f"Processed {len(files_to_extract)} files in {time() - start_time:.2f} seconds."
    )


if __name__ == "__main__":
    main()
