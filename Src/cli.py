import sys
from platform import system, architecture, release
from extract_addons import main as extract_addons
from extract_archives import main as extract_archives

version = f"v2.3.1 (ef4fe69)"
build_date = "2024-11-26 (Tuesday, November 26, 2024)"
rarfile_version = "4.2"
py7zr_version = "0.22.0"
pyinstaller_version = "6.11.1"
seven_zip_version = "24.08"

def display_info():
    system_info = get_os_info()
    print(
        f"{'=' * 75}\n"
        f"Vermeil's Addon Extractor {version}, {system_info} ({architecture()[0]}).\n"
        f"Build Date: {build_date}.\n"
        f"Build Info: Pyinstaller {pyinstaller_version}, Py7zr {py7zr_version}, "
        f"RarFile {rarfile_version}, 7-zip {seven_zip_version}.\n"
        f"{'=' * 75}\n"
    )

def display_menu():
    print(
        "Select an option:\n"
        "1. Extract addons (GMA, BIN)\n"
        "2. Extract archives (ZIP, RAR, 7Z, TAR, TAR.XZ, TAR.GZ)\n"
        "3. Help\n"
        "4. Exit\n"
    )

def display_help():
    print(
        "\nHelp:\n"
        "1. Extract addons - For GMA and BIN files.\n"
        "2. Extract archives - Extracts archive formats (ZIP, RAR, 7Z, TAR, TAR.XZ, TAR.GZ). Mainly for 3rd party.\n"
        "3. Help - Displays this info.\n"
        "4. Exit - Closes the program.\n"
    )

def handle_choice(choice):
    options = {
        "1": extract_addons,
        "2": extract_archives,
        "3": display_help,
        "4": sys.exit
    }

    if choice in options:
        options[choice]()
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")

def get_linux_info():
    with open("/etc/os-release") as f:
        os_info = dict(line.strip().split('=') for line in f)
    return os_info.get("PRETTY_NAME", "").strip('"')

def get_os_info():
    os_name = system()
    if os_name != "Linux":
        return f"{os_name} {release()}"
    return get_linux_info() or os_name

def main():
    try:
        display_info()
        while True:
            display_menu()
            choice = input("Enter your choice (1-4): ").strip()
            handle_choice(choice)
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()
