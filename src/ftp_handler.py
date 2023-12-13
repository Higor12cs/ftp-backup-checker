from ftplib import error_perm
from ftplib import FTP
import os

class FTPHandler:
    def __init__(self, host, username, password):
        self.ftp = FTP(host)
        self.ftp.login(user=username, passwd=password)

    def list_files(self, path):
        self.ftp.cwd(path)
        files = []
        self.ftp.retrlines('LIST', files.append)

        filtered_files = [f for f in files if not f.endswith(' .') and not f.endswith(' ..')]
        return filtered_files

    def disconnect(self):
        self.ftp.quit()
