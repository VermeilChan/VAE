# Vermeil's Addon Extractor (VAE)

**VAE** is a command-line tool for users of Garry's Mod who need to extract content from addon files. This utility supports both modern `.gma` addons and legacy `.bin` addons, an essential tool for players who download addons from sources such as SteamCMD, third-party programs, websites, or for those using cracked versions of the game.

## Features

- 🖥️ Cross-Platform: Works on Windows, macOS, and Linux.
- 📦 Addon Extraction: Extract both modern `.gma` and legacy `.bin` addon formats.
- 🔄 Archive Extraction: Supports archive formats (`.zip`, `.rar`, `.7z`, `.tar`, `tar.gz` and `tar.xz`).
- ⚡ Multithreading: Utilizes concurrent processing to speed up extraction.
- 🛠️ Easy to Use: A simple command-line interface.
- 🔄 GWTool Replacement: **VAE** is a drop-in replacement for GWTool.

## Requirements

| Operating System | Supported Versions                                       | Architecture |
|------------------|----------------------------------------------------------|--------------|
| Windows          | 11, 10, 8.1, 8                                           | 64-bit       |
| Linux            | Debian 12, Ubuntu 22.04, Fedora 41, Arch Linux, OpenSUSE | 64-bit       |
| macOS            | macOS 15, 14, 13, 12, 11, 10.15                          | Arm64        |

- **RAM Usage:** 20MB
- **Disk Space:** 25MB

## Installation

To install VAE, download the [latest release](https://github.com/VermeilChan/VAE/releases/latest).

- **Windows:** `VAE-2.x.x-Windows-x64.7z`
- **Linux:** `VAE-2.x.x-Linux-x64.tar.xz`
- **macOS:** `VAE-2.x.x-macOS-Arm64.zip`

## Usage

### Step 1: Extract the Downloaded Archive

1. Extract the contents of VAE.
2. Copy the extracted content to the directory where your addons are located. For example:
   - **SteamCMD Path:** `path-to-steamcmd/steamapps/workshop/content/4000`
   - **3rd Party Websites/Programs:** Place VAE in the directory containing your archives or folders. VAE will scan the current directory and any subdirectories.

### Step 2: Run the Program

Upon launching the program, you will be presented with two options:

#### Option 1: Extract Addons

- This option scans the current directory and subdirectories for `.gma` and `.bin` files and extracts them using `fastgmad`.
  - Navigate to the `Extracted-Addons` folder, and copy the folders to your Garry's Mod directory. Enjoy your addons!

#### Option 2: Extract Archives

- This option scans the current directory for archive files (e.g., `.zip`, `.rar`, `.7z`, `.tar`) and extracts them.

- If you want to free up some space, you can remove the `Leftover` folder, which contains the `.gma` and `.bin` and archives.

## Building VAE

Please refer to the [build instructions](BUILD.md) for details on building VAE from source.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).

## Credits

- **[Adamizo](https://github.com/adamizo):** The dumbest person I know. (the main reason why this program exist in first place)
- **[PyInstaller](https://www.pyinstaller.org/):** For creating standalone executables.
- **[Py7zr](https://pypi.org/project/py7zr/):** For 7z file extraction.
- **[RarFile](https://pypi.org/project/rarfile/):** For rar file extraction.
- **[FastGMAD](https://github.com/WilliamVenner/fastgmad):** Fast reimplementation of gmad. (Forked)
- **[7-zip](https://www.7-zip.org/):** For extracting .bin files.
