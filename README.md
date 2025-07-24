# FTPServer on Linux

Here, Ive created a basic standalone FTP server in Python thats typically intended for another project. However, since this is quite "basic," I thought of sharing it with all of you.

## Here, Ill tell you what you need to do for this:

1.) Download the file and place the Python file in a directory of your choice.

2.) You need to install the Python packages first to run the file.

- Commands to Install the Packets and Python on Linux:
```
sudo apt update -y
sudo apt install python3.8
sudo apt install python3-pyftpdlib
```

3.) If you have installed everything, open the `ftpserver.py` file and edit the additional details Comment with `#`

4.) Don't Forget: Open the Firewall Port: `sudo ufw allow 2121/tcp`

5.) Now everything should be ready and working. You can start the FTPServer with the command: `python3 ftpserver.py`

Now you can connect using a program like "**WinSCP**" or "**FileZilla**" Please remember to set the settings in the FTP program to "**FTP**" and not "**SFTP**" or something else.

> [!NOTE]
> If there are any problems, please reach out here or on Discord. **(Discord: mambuzrrr)**. The meaning of **"elradfmw"** inside the code indicates that the user has the **permissions**: **execute**, **list**, **read**, **append**, **delete**, **full controll (inside path)**, **modfiy** & **Write**.

> [!TIP]
> If you want to keep your FTPServer running continuously, you can go to the directory where the `ftpserver.py` file is located **(using Putty)**. Then, you can open a new terminal with `screen -S terminalname` and execute the file with `python3 ftpserver.py`. You can exit the terminal with `CTRL+A+D` **(dont worry, it continues running)**. To return to the terminal, use the command `screen -R terminalname`.

> [!IMPORTANT]
> No updates will be provided here. Since this was developed for private projects, updates will only be released for private purposes.
