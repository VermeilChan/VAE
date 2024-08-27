# Table of Contents

- [Platforms](#platforms)
- [Getting the Source Code](#getting-the-source-code)
- [Dependencies](#dependencies)
  - [Windows](#dependencies)
  - [Linux](#linux-dependencies)
  - [macOS](#dependencies)
- [Compiling](#compiling)
  - [Windows](#windows-details)
  - [Linux](#linux-details)
  - [macOS](#macos-details)

# Platforms

VAE supports the following platforms:

| Operating System | Supported Versions                                       | Architecture    |
|------------------|----------------------------------------------------------|-----------------|
| Windows          | 11, 10, 8.1, 8                                           | 64-bit (x86-64) |
| Linux            | Debian 12, Ubuntu 20.04, Fedora 38, Arch Linux, OpenSUSE | 64-bit (x86-64) |
| macOS            | macOS 14, 13, 12, 11, 10.15                              | 64-bit (x86-64) |

# Getting the Source Code

- Download the zip archive from the [latest release](https://github.com/VermeilChan/VAE/releases/latest). `VAE-v2.x.x-Source-x64.zip`

# Dependencies

You need the following to compile VAE:

- [Python](https://www.python.org/) 3.8+
- [PyInstaller](https://www.pyinstaller.org/) 6.6.0+
- [Py7zr](https://pypi.org/project/py7zr/)
- [RarFile](https://pypi.org/project/rarfile/)

## Linux Dependencies

For Ubuntu/Debian:
```sh
sudo apt install -y python3 python3-pip python3-venv
```
For Fedora:
```sh
sudo dnf install -y python3 python3-pip python3-virtualenv
```
For Arch:
```sh
sudo pacman -Syu --noconfirm python-pip python-virtualenv
```
For OpenSUSE:
```sh
sudo zypper install -y python3 python3-pip python3-virtualenv
```

# Compiling

## Windows

In Command Prompt:
```sh
cd VAE
py -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
pyinstaller --noconfirm --onedir --console --icon "Src/Icon/VAE.ico" --name "VAE" --clean --optimize "2" --version-file "version.txt" --add-data "Src/extract_addons.py;." --add-data "Src/extract_archives.py;." --add-data "Src/Bin;Bin/"  "Src/cli.py"
```

## Linux

In Terminal:
```sh
cd VAE
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pyinstaller --noconfirm --onedir --console --name "VAE" --clean --optimize "2" --strip --add-data "Src/extract_addons.py:." --add-data "Src/extract_archives.py:." --add-data "Src/Bin:Bin/"  "Src/cli.py"
```

## macOS

In Terminal:
```sh
cd VAE
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pyinstaller --noconfirm --onedir --console --name "VAE" --clean --optimize "2" --strip --add-data "Src/extract_addons.py:." --add-data "Src/extract_archives.py:." --add-data "Src/Bin:Bin/"  "Src/cli.py"
```