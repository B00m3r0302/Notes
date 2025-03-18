# xFreeRDP3
Is by far one of the better RDP clients in the marketspace. It is an open-source RDP client based on the FreeRDP project. It is lightweight, supports modern RDP features, and is commonly used in Linux environments for high-performance remote desktop access.
## Installation
```bash
sudo apt update && sudo apt upgrade -y
```
```bash
sudo apt install -y freerdp3-x11
```
## Usage
- Connecting to an RDP session
```bash
xfreerdp3 /v:target_ip /u:username /p:password
```
- Connect with full-screen mode
```bash
xfreerdp3 /v:target_ip /u:username /p:password /f
```
- Redirecting local drives (useful for file transfers)
```bash
xfreerdp3 /v:target_ip /u:username /p:password /drive:shared,/home/user/shared
```
# Rdesktop
Is one of the older RDP clients for Unix-based systems. While it was once a popular choice, it has been mostly superseded by FreeRDP due to better support for modern Windows versions. However, rdesktop is still useful for compatibility with older RDP servers.
## Installation
```bash
sudo apt update && sudo apt upgrade -y 
```
```bash
sudo apt install -y rdesktop
```
## Usage
- Connect to an RDP session
```bash
rdesktop -u username -p password target_ip
```
- Connect in full-screen mode
```bash
rdesktop -u username -p password -f target_ip
```
- Connect and enable sound support
```bash
rdesktop -u username -p password -r sound:local target_ip
```
# Remmina
Is a GUI-based RDP client that supports RDP, VNC, SSH and other remote protocols. It is widely used in Linux for is ease of use and versatility.
## Installation
```bash
sudo apt update && sudo apt upgrade -y
```
```bash
sudo apt install -y remmina remmina-plugin-rdp
```
## Usage
To use Remmina select the remmina icon from the applications menu. From here you will input the following options under “add connection”

- Protocol: (protocol you want to use to connect)
- Server: target IP address
- Username: username for the session
- Password: password for the session
- Click “save and connect”