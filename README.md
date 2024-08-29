# Vermeil's Addon Extractor (VAE)

**Vermeil's Addon Extractor (VAE)** is a user-friendly utility designed to simplify the extraction of Garry's Mod addons and various archive formats. Whether you're using SteamCMD, downloading addons from third-party websites, or managing addons without owning the game, VAE streamlines the extraction process, making it fast and hassle-free.

## Features

- 🖥️ Cross-Platform Compatibility: Works on Windows, macOS, and Linux.
- 📦 Support for Multiple Archive Formats: Easily extracts `.zip`, `.rar`, `.7z`, and `.tar` files.
- 🔄 Automatic Handling: Effortlessly processes `.gma` files and archives.
- ⚡ Fast and Efficient: Utilizes multi-threading for quicker extraction.
- 🛠️ Easy to Use: Simple command-line interface for straightforward operation.

## Requirements

| Operating System | Supported Versions                                       | Architecture    |
|------------------|----------------------------------------------------------|-----------------|
| Windows          | 11, 10, 8.1, 8                                           | 64-bit (x86-64) |
| Linux            | Debian 12, Ubuntu 20.04, Fedora 38, Arch Linux, OpenSUSE | 64-bit (x86-64) |
| macOS            | macOS 14, 13, 12, 11, 10.15                              | 64-bit (x86-64) |

- **RAM Usage:** 20MB
- **Disk Space:** 25MB

## Installation

To install VAE, download the [latest release](https://github.com/VermeilChan/VAE/releases/latest).

- **Windows:** `VAE-2.x.x-Windows-x64.7z`
- **Linux:** `VAE-2.x.x-Linux-x64.tar.xz`
- **macOS:** `VAE-2.x.x-macOS-x64.zip`

## Usage

### Step 1: Extract the Downloaded Archive

1. Extract the contents of VAE.
2. Copy the extracted content to the directory where your addons are located. For example:
   - **SteamCMD Path:** `path-to-steamcmd/steamapps/workshop/content/4000`
   - **3rd Party Websites/Programs:** Place VAE in the directory containing your archives or folders. VAE will scan the current directory and any subdirectories.

### Step 2: Run the Program

Upon launching the program, you will be presented with three options:

1. **Extract Addons (GMA)**
2. **Extract Archives (ZIP, RAR, 7Z, TAR)**
3. **Exit**

#### Option 1: Extract Addons (GMA)

- This option scans the current directory and subdirectories for `.gma` files and extracts them using `fastgmad`.
  - Navigate to the `Extracted-Addons` folder, and copy the folders to your Garry's Mod directory. Enjoy your addons!
  - If you want to free up some space, you can remove the `Leftover` folder, which contains the `.gma` and archives.

#### Option 2: Extract Archives (ZIP, RAR, 7Z, TAR)

- This option scans the current directory for archive files (e.g., `.zip`, `.rar`, `.7z`, `.tar`) and extracts them.
- The original archive files are moved to the `Leftover` directory after extraction.

## Building VAE

Please refer to the [build instructions](BUILD.md) for details on building VAE from source.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).

## Credits

- **[Adamizo](https://github.com/adamizo):** The dumbest person I know.
- **[PyInstaller](https://www.pyinstaller.org/):** Used for creating standalone executables.
- **[Py7zr](https://pypi.org/project/py7zr/):** For 7z file extraction.
- **[RarFile](https://pypi.org/project/rarfile/):** For rar file extraction.
- **[FastGMAD](https://github.com/WilliamVenner/fastgmad):** Fast reimplementation of gmad.

## TODO

- Add support for legacy (.bin) addons.
