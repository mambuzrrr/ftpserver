# Made by Brejax
# Simple FTP Server – Cleaned & Improved

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

# ========== CONFIG ==========
FTP_USER = "your_username"
FTP_PASSWORD = "your_password"
FTP_DIRECTORY = "/path/to/folder"
FTP_HOST = "0.0.0.0"         # 0.0.0.0 for all interfaces
FTP_PORT = 2121              # Dont use Port 69 (its standard port of TFTP)
# ============================

def start_ftp_server():
    if not os.path.isdir(FTP_DIRECTORY):
        raise FileNotFoundError(f"FTP root directory not found: {FTP_DIRECTORY}")
        
    authorizer = DummyAuthorizer()
    authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer

    print(f"[+] Starting FTP server on {FTP_HOST}:{FTP_PORT}")
    print(f"[+] Serving directory: {FTP_DIRECTORY}")
    print(f"[+] Login with: {FTP_USER} / {FTP_PASSWORD}")

    server = FTPServer((FTP_HOST, FTP_PORT), handler)
    server.serve_forever()
    
if __name__ == "__main__":
    try:
        start_ftp_server()
    except KeyboardInterrupt:
        print("\n[!] Server manually stopped.")
    except Exception as e:
        print(f"[!] Error: {e}")
