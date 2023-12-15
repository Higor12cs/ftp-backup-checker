
# ftp-backup-checker

The `ftp-backup-checker` is a Python script developed to facilitate the management of files on FTP servers. It allows you to list files in a specific directory on the server and generate an Excel report with details of the found files.

## Prerequisites

-   Python 3.x
-   Python Libraries: `dotenv`, `argparse`, `os`

## Installation

Clone the repository to your local machine:

`git clone https://github.com/Higor12cs/ftp-backup-checker`

Install the necessary dependencies:

`pip install -r requirements.txt`

## Usage

To use the script, execute the following command:

`python main.py [FTP directory path] [--extension EXTENSION]`

Arguments:

-   `FTP directory path`: The path to the directory on the FTP server you want to check.
-   `--extension`: (Optional) Filter files by a specific extension, for example, `.zip`.

Example:

`python main.py /path/to/directory --extension .zip`

## License

This project is licensed under the MIT License - see the LICENSE file for details.
