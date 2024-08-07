from os import rmdir
from time import time
from uuid import uuid4
from shutil import move
from pathlib import Path
from platform import system
from subprocess import run, CalledProcessError
from concurrent.futures import ThreadPoolExecutor


def get_gmad_executable():
    os_to_executable = {
        "Windows": "gmad.exe",
        "Darwin": "gmad_osx",
        "Linux": "gmad_linux",
    }
    executable_path = Path("Bin", system(), os_to_executable[system()])

    if not executable_path.exists():
        user_input = input(
            f"{executable_path} not found.\nProvide the path to gmad executable: "
        )
        executable_path = Path(user_input)
        if not executable_path.exists():
            raise FileNotFoundError(f"Executable not found: {executable_path}")

    return executable_path


def extract_gma(gma_path, extracted_addons_path, leftover_path, gmad_executable):
    unique_name = uuid4().hex
    renamed_gma_path = gma_path.with_name(f"{unique_name}.gma")

    move(gma_path, renamed_gma_path)

    output_path = extracted_addons_path / unique_name
    output_path.mkdir(parents=True, exist_ok=True)

    try:
        run(
            [
                gmad_executable,
                "extract",
                "-file",
                renamed_gma_path,
                "-out",
                output_path,
            ],
            check=True,
        )
    except CalledProcessError:
        print(f"Extraction failed for {renamed_gma_path}")

    gma_folder = gma_path.parent
    if gma_folder != Path.cwd():
        target_folder = leftover_path / gma_folder.name
        if not target_folder.exists():
            move(gma_folder, target_folder)

    move(renamed_gma_path, leftover_path / renamed_gma_path.name)


def remove_empty_folders(root_path, ignored_folders):
    for dirpath in root_path.glob("**/"):
        if dirpath.name not in ignored_folders and not any(dirpath.iterdir()):
            try:
                rmdir(dirpath)
            except OSError:
                pass


def main():
    start_time = time()
    current_directory = Path.cwd()

    ignored_folders = {"Extracted-Addons", "Leftover", "_internal", "Bin"}

    extracted_addons_path = current_directory / "Extracted-Addons"
    leftover_path = current_directory / "Leftover"

    extracted_addons_path.mkdir(exist_ok=True)
    leftover_path.mkdir(exist_ok=True)

    gmad_executable = get_gmad_executable()

    gma_files = list(current_directory.rglob("*.gma"))

    with ThreadPoolExecutor() as executor:
        executor.map(
            lambda gma_path: extract_gma(
                gma_path, extracted_addons_path, leftover_path, gmad_executable
            ),
            gma_files,
        )

    remove_empty_folders(current_directory, ignored_folders)

    print(
        f"Processed {len(gma_files)} .gma files in {time() - start_time:.2f} seconds."
    )


if __name__ == "__main__":
    main()
