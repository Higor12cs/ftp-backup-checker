from dotenv import load_dotenv
import os
import argparse
from ftp_handler import FTPHandler
from excel_handler import ExcelHandler

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description='FTP to Excel script')
    parser.add_argument('path', help='Path to the directory on the FTP server')
    parser.add_argument('--extension', help='File extension to filter by, e.g., .zip', default=None)
    args = parser.parse_args()

    ftp_host = os.getenv("FTP_HOST")
    ftp_user = os.getenv("FTP_USER")
    ftp_pass = os.getenv("FTP_PASS")

    ftp = FTPHandler(ftp_host, ftp_user, ftp_pass)
    try:
        files = ftp.list_files(args.path)
    except Exception as e:
        print(f"Erro ao acessar o diretório: {e}")
        return
    finally:
        ftp.disconnect()

    if not files:
        print(f"Nenhum arquivo encontrado no diretório: {args.path}")
        return

    if args.extension:
        files = [f for f in files if f.endswith(args.extension)]

    processed_files = [(f.split()[-1], " ".join(f.split()[5:8])) for f in files]

    excel = ExcelHandler()
    directory_name = os.path.basename(args.path.strip('/'))
    excel_file_name = f"{directory_name}.xlsx"
    excel.create_excel(processed_files, excel_file_name)

if __name__ == "__main__":
    main()
