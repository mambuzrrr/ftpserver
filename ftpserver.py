# Made by Brejax
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def start_ftp_server():
    authorizer = DummyAuthorizer()

    username = "USERHERE" # Add a User with a Username...
    password = "PASSWORDHERE" # Add a User with a Password...
    
    # Insert the path here where the user will later have access...
    remote_directory = "/path/to/folder"

    authorizer.add_user(username, password, remote_directory, perm="elradfmw") # See Github for the meaning of "elradfmw"...

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer(("YOURIP/DOMAINHERE", 69), handler) # Set your IP-Address or Domain and Port "69" (Can be any number)...
    server.serve_forever()

if __name__ == "__main__":
    start_ftp_server() # Yes... starting FTP Server LOL...
