In the absence of an SSH server on a target or RAD there are graphical alternatives such as Virtual Network Computing (VNC). VNC is a remote desktop sharing system that allows users to control a computer’s graphical desktop environment over a network connection. VNC operates using the Remote Framebuffer (RFB) protocol, which transmits screen updates, keyboard inputs and mouse movements between the client and the remote machine.

VNC is platform-independent meaning it can be used to remotely control Linux, Windows, or macOS machines from various devices, including other computers, tablets, or smartphones. It is commonly used for remote administration, IT support and accessing headless systems (systems without a monitor attached). Two of the most common VNC applications are:

1. TightVNC
2. RealVNC

TightVNC is a lightweight, open-source VNC server optimized for low-bandwidth environments. It features better compression algorithms to reduce lag and improve performance making it ideal for use over slow network connections.

**Key features**
- Efficient bandwidth usage
- Cross-platform support (Windows & Linux)
- Password authentication for basic security.    
- Multiple clients can connect simultaneously to the same session

RealVNC is a commercial VNC solution that offers free and paid versions with additional features such as end-to-end encryption, cloud connectivity, and multi-factor authentication.
## Key Features
- Stronger security with the paid version
- Cloud-based remote access (allows connections without port forwarding)
- File transfer & remote printing capabilities.
- More user-friendly interface compared to TightVNC.
## Pros & Cons
### Pros
- Graphical control: Provides a full desktop environment instead of just a command line
- Persistent access: Allows an attacker to reconnect easily without re-exploiting a system
- Low system requirements: Works on low-power devices like Raspberry Pi
- Supports multiple users: Multiple operators can connect to the same VNC session
### Cons
- Unencrypted by default: Must be tunneled through SSH for security
- High bandwidth usage: Not ideal for low-bandwidth remote access devices
- Easy to detect: Generates network logs and visible processes (Xtightvnc or Xvnc)
- Does not support native clipboard Encryption: Data copied via clipboard can be exposed.
## Installation
- Commands
```bash
sudo apt update && sudo apt install -y tightvncserver
```
```bash
tightvncserver
```
- The first time you run this it will prompt you to set a VNC access password (max 8 characters)
- You can optionally set a view-only password to allow users to watch but not control the session
- Check to see if the VNC server is running
```bash
ps aux | grep Xtightvnc
```
- If the output is not blank the VNC server is running
## Connecting to a VNC server
### Installation
- Command
```bash
sudo apt update && sudo apt install -y tigervnc-viewer
```
- Open "VNC Viewer" and enter the connection details (SERVER/RAD_IP:PORT(default is 5901))
- Login with the password