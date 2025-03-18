An alternative to VNC that is more up-to-date and provides a more stable and effective user experience is Remote Desktop Protocol (RDP). RDP is a proprietary protocol developed by Microsoft that allows users to remotely control a Windows system using a graphical interface like VNC. RDP enables users to access applications, files and network resources on a remote machine as if they were physically present.

Unlike VNC, which simply transmits screen updates and inputs, RDP provides a smoother experience with better compression, support for audio redirection, printer sharing, clipboard syncing and multiple monitor support. Additionally, RDP has been expanded to support both Linux and macOS operating systems. While there are a variety of RDP client and server applications available in the marketspace the primary applications, we will be using are xRDP, RustDesk, and Guacamole on the server-side and xfreerdp3, rdesktop, and remmina on the client-side. The applications are primarily used on Linux operating systems but can be used on other operating systems as well.
# RDP Server Applications
## xRDP
xRDP is an open-source implementation of Microsoft’s RDP for Linux-based systems. It allows users to remotely access a Linux machine from an RDP client, such as Windows Remote Desktop (mstsc.exe), Remmina, xfreerdp3 or other RDP-compatible software. XRDP acts as a middle layer that enables RDP clients to interact with the Linux desktop environment:
### How It Works:
1. Client Connection: An RDP client sends a request to connect via port 3389.
2. Session Authentication: xRDP authenticates the user using local Linux credentials.
3. X11 Backend Handling: xRDP launches an Xorg session or redirects to an existing session, rendering the Linux GUI (we will primarily be using xfce4)
4. Display & Input Handling: The remote desktop is streamed to the client, allowing for keyboard/mouse control
### Installation
- Before installing any new packages ensure your system is up to date
```bash
sudo apt update && sudo apt upgrade -y
```
- Install the xfce4 desktop environment if your system does nto already have xfce4 installed
```bash
sudo apt install -y xfce4 xfce4-goodies
```
- Install the xRDP server package
```bash
sudo apt install -y xrdp
```
- Enable xRDP to start on boot and start the service immediately
```bash
sudo systemctl enable --now xrdp
```
- Create a new user so that you can remote into the RAD with RDP while interacting with it locally.
	- Start with creating a new user named rdp and automatically create a home directory for them 
```bash
sudo adduser rdp
```
- You will be prompted to set a password for the user 
- this will create the user with a home directory at /home/rdp
- To give rdp user sudo privileges, add them to the sudo group
```bash
sudo usermod -aG sudo rdp
```
- To verify the user is in the sudo group run
```bash
groups rdp
```
- you should see output similar to 
```ini
rdp : rdp sudo
```
- By default xRDP only allows users in certain groups.
	- Add the rdp user to the "ssl-cert" group which is required for xRDP authentication
```bash
sudo adduser rdp ssl-cert
```
- xRDP does not use your default linux desktop session automatically
	- You need to configure it to lauynch xfce4 instead of the default (which may be GNOME or another DE).
	- Each RDP user must have an ".xsession" file to define their desktop session in their home directory.
```bash
echo "xfce4-session" | sudo tee /home/rdp/.xsession
```
```bash
sudo chown rdp:rdp /home/rdp/.xsession
```
```bash
sudo chmod +x /home/rdp/.xsession
```
- Restart xRDP to apply the changes
```bash
sudo systemctl restart xrdp
```
- Verify the xRDP package is running looking for "Active" and "Enabled" keywords in the output of the following command
```bash
sudo systemctl status xrdp
```
### Pros & Cons
#### Pros
- Better performance than VNC: RDP is optimized for low-bandwidth environments
- Supports clipboard, file transfer, and audio redirection: Ideal for interactive attacks
- Built-in on Windows: No need to install extra software on Windows targets where RDP is enabled
- Can be Encrypted to be more secure than default VNC
#### Cons
- Runs on a Well-Known port (3389) and can be easily detected and blocked
- More logging and visibility: Windows event logs can track RDP connections, making it easier for defenders to spot unauthorized access
- Only one interactive session at a time: If a user is actively using RDP, switching to another session may alert the target
### Conclusion
RDP is a powerful remote access tool that offers better performance and usability than VNC making it an ideal choice for interacting with compromised Windows systems or interacting with an RDP server. However, its visibility in Windows event logs and reliance on port 3389 makes it easier to detect than other tunneling methods. By tunneling RDP through SSH or a RAD, attackers can evade detection, establish persistent access, and interact with target systems more effectively while reducing forensic traces.
## RustDesk
RustDesk is a free, open-source remote desktop application that provides a self-hosted alternative to commercial solutions like TeamViewer and AnyDesk. It allows users to remotely access and control devices, with end-to-end encryption for secure communication. RustDesk is ideal for scenarios where privacy, control over the infrastructure, and customizability are priorities. In offensive cyber operations, a self-hosted RustDesk server can act as a covert Remote Access Tool (RAT) for persistent access to remote systems without relying on third-party services. It can also serve as an alternative to RDP servers and clients.
### Installation
- Ensure your system is updated and install the necessary dependencies
```bash
sudo apt update && sudo apt upgrade -y
```
```bash
sudo apt install -y wget curl unzip
```
- Download the latest RustDesk server files from the official source
```bash
wget https://github.com/rustdesk/rustdesk/releases/latest/download/rustdesk-server-linux-amd64.zip
```
- Extract the files and move into the RustDesk directory 
```bash
unzip rustdesk-server-linux-amd64.zip -d rustdesk-server
```
```bash
cd rustdesk-server
```
- Make the server binaries executable
```bash
chmod +x hbbs hbbr
```
- Move the binaries to the /usr/bin directory 
```bash
sudo mv hbbs /usr/bin
```
```bash
sudo mv hbbr /usr/bin
```
- Create the hbbs service by creating a file 
```
sudo vim /etc/systemd/system/hbbs.service
```
- Add the content below
```ini
[Unit]
Description=RustDesk Broker Server
After=network.target

[Service]
ExecStart=/usr/bin/hbbs -r <YOUR-SERVER-IP>:21117
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```
- Create a file for the hbbr service
```bash
sudo vim /etc/systemd/system/hbbr.service
```
- Add the content below
```ini
[Unit]
Description=RustDesk Relay Server
After=network.target

[Service]
ExecStart=/usr/bin/hbbr
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```
- Enable the services so that they start on boot
```bash
sudo systemctl enable hbbs hbbr
```
- Start the services
```bash
sudo systemctl start hbbs hbbr
```
- Check to see if the services are running and look for "Active" and "Enabled" keywords in the output
```bash
sudo systemctl status hbbs hbbr
```
### Pros & Cons
#### Pros
- Self-hosted: No reliance on third-party services
- Encrypted communication: Secure data transmission
- Cross-platform works on Linux, Windows, macOS, Android and iOS
- NAT traversal support: Bypasses firewalls easily
- Simple installation: Quick setup compared to traditional RDP/VNC
#### Cons
- Requires open ports (if using a self-hosted server).
- Needs additional security hardening to be secure
- Higher visibility in logs than SSH tunnels
- May not be able to login with an IP, username, and password without additional configuration as RustDesk primarily uses a computer ID and rotating passwords.
### Conclusion
RustDesk is a powerful, open-source remote desktop tool that provides privacy and security advantages over commercial alternatives. By deploying a self-hosted RustDesk server, attackers or teams can maintain stealthy persistence and access to compromised systems without opening additional network ports or relying on third-party services.
## Guacamole
Apache Guacamole is a clientless remote desktop gateway that allows users to access RDP, VNC and SSH sessions through a web browser. Unlike traditional remote access tools that require client applications, Guacamole operates entirely through HTML5, making it platform-independent and highly flexible.
### Why Guacamole?
- Stealthy web-based access: no need for installing RDP or SSH clients; access is done via a browser.
- Centralized multi-protocol access: Control multiple remote systems like Windows RDP and Linux SSH/VNC from a single web interface
- Proxy and tunneling support: can be routed through a RAD to provide a centralized point for accessing target networks
- Credential management: stores login credentials, allowing persistent access to compromised hosts
- End-to-End encryption: Can be secured using SSL/TLS
### Installation
Installation requires two main components
1. Guacamole Server: the backend responsible for handling remote connections.
2. Guacamole Client (web application): The frontend that provides access through a browser
- Before installing Guacamole update your system and install the required dependencies
```bash
sudo apt update && sudo apt upgrade -y
```
```bash
sudo apt install -y build-essential libcairo2-dev libjpeg62-turbo-dev libpng-dev libtool-bin uuid-dev freerdp2-dev libpango1.0-dev libssh2-1-dev libtelnet-dev libvncserver-dev libwebsockets-dev libssl-dev tomcat9 tomcat9-admin tomcat9-common ghostscript libpulse-dev libavcodec-dev libavformat-dev libacutil-dev
```
- Download the latest Guacamole source code
```bash
wget https://archive.apache.org/dist/guacamole/1.5.3/source/guacamole-server-1.5.3.tar.gz
```
- Extract the files and move into the directory
```bash
tar -xzf guacamole-server-1.5.3.tar.gz
```
```bash
cd guacamole-server-1.5.3
```
- Compile and install
```bash
./configure --with-init-dir=/etc/init.d
```
```bash
make -j$(noproc)
```
```bash
sudo make install
```
```bash
sudo ldconfig
```
- Enable the service so that it starts on boot and start the Guacamole service
```bash
sudo systemctl daemon-reload
```
```bash
sudo systemctl enable guacd
```
```bash
sudo systemctl start guacd
```
- Install the Guacamole web application
```bash
wget https://archive.apache.org/dist/guacamole/1.5.3/binary/guacamole-1.5.3.war -O guacamole.war
```
- Move the web application to Tomcat's directory
```bash
sudo mv guacamole.war /var/lib/tomcat9/webapps
```
- Restart Tomcat to deploy Guacamole web application
```bash
sudo systemctl restart tomcat9
```
- After this Guacamole should be accessible via http://yourip:8080 in the browser
### Configuration
Guacamole requires a configuration file at "/etc/guacamole/guacamole.properties"
- Create the necessary directories
```bash
sudo mkdir -p /etc/guacamole/{extensions,lib}
```
- Create the configuration file
```bash
sudo vim /etc/guacamole/guacamole.properties
```
- Add the content below
```ini
guacd-hostname: localhost
guacd-port: 4822
user-mapping: /etc/guacamole/user-mapping.xml
auth-provider: net.sourceforge.guacamole.net.basic.BasicFileAuthenticationProvider
```
- Setup user authenticating by creating the user-mapping file
```bash
sudo vim /etc/guacamole/user-mapping.xml
```
- Add the content below based on what you want
```xml
<user-mapping>
	<authorize username="admin" password="SuperSecurePassword">
		<connection name="Target RDP">
			<protocol>rdp</protocol>
			<param name="hostname">IP_ADDRESS</param>
			<param name="port">3389</param>
			<param name="username">Administrator</param>
			<param name="password">Password123</param>
		</connection>
		<connection name="Target SSH">
			<protocol>ssh</protocol>
			<param name="hostname">IP_ADDRESS</param>
			<param name="port">22</param>
			<param name="username">Administrator</param>
			<param name="password">Password123</param>
		</connection>
		<connection name="Target VNC">
			<protocol>vnc</protocol>
			<param name="hostname">IP_ADDRESS</param>
			<param name="port">5901</param>
			<param name="username">Administrator</param>
			<param name="password">Password123</param>
		</connection>
	</authorize>
</user-mapping>
```
- Restart the services to apply the changes
```bash
sudo systemctl restart guacd tomcat9
```
#### Protecting Guacamole with SSL
If you have multiple users and want to avoid browser SSL warnings, you can set up a Local Certificate Authority (CA) and sign your certificate
- Create the following directory and move into it
```bash
sudo mkdir -p /etc/ssl/guacamole
```
```bash
cd /etc/ssl/guacamole
```
- ensure only root can access the certificates
```bash
sudo chmod 600 /etc/ssl/guacamole/*
```
- Create a local CA (only once!)
```bash
openssl genpkey -algorithm RSA -out localCA.key
```
```
openssl req -x509 -new -nodes -key localCA.key -sha256 -days 1825 -out localCA.pem
```
- Generate a Certificate Signing Request (CSR)
```bash
openssl req -new -key guac-key.pem -out guac.csr
```
- Sign the CSR with your local CA
```bash
openssl x509 -req -in guac.csr -CA localCA.pem -CAkey localCA.key -CAcreateserial -out guac-cert.pem -days 825 -sha256
```
- Import the signed certificate into Java Keystore
```bash
keytool -importkeystore -srckeystore guac.p12 -srcstoretype PKCS12 -destkeystore guac.keystore -deststoretype JKS
```
#### Configure Tomcat to use SSL
- Edit the tomcat configuration file
```bash
sudo vim /etc/tomcat9/server.xml
```
- Look for “Connector” for port 8443 or add the following section if it doesn’t exist (replace Your_keystore_password with the password you set in the previous steps
- Example
```xml
<Connector port="8443" protocol="HTTP/1.1" SSLEnabled="true">
	<SSLHostConfig>
		<Certificate certificateKestoreFile="/etc/ssl/guacamole/guac.keystore" type="JKS" certificateKeystorePassword="your_keystore_password" />
	</SSLHostConfig>
</Connector>
```
- Restart Tomcat
```bash
sudo systemctl restart tomcat9
```
- After this Guacamole should be accessible in your browser via https://<YOUR_SERVER_IP>:8443/guacamole
- If the local CA certificate is installed on your machine, there should be no browser warnings.
- If you still get an “Untrusted Certificate” warning install the “localCA.pem” on your system
```bash
sudo cp /etc/ssl/guacamole/localCA.pem /usr/local/share/ca-certificates/localCA.crt
```
```bash
sudo update-ca-certificates
```
#### Redirecting HTTP to HTTPS (for more security)
Requires modifying the tomcat configuration
```bash
sudo vim /etc/tomcat9/server.xml
```
- find the HTTP "Connector" (usually port 8080) and ad the "redirectPort" attribute like below
```xml
<Connector port="8080" protocol="HTTP/1.1"
		   connectionTimeout="20000"
		   redirectPort="8443" />
```
- Restart Tomcat
```bash
sudo systemctl restart tomcat9
```
- now any connection to http://your_server_ip:8080/guacamole will be redirected to HTTPS
### Pros & Cons
#### Pros
- Clientless: no need to install and RDP/VNC client; access via browser.
- Supports multiple protocols: RDP, SSH, and VNC in a single interface
- Secure (if properly configured) – Uses SSL/TLS and centralized authentication
- Works well with jump hosts/RADs: Provides a single-entry point into a target network
#### Cons
- More complex to set up than direct RDP or SSH
- Potential logging risks: if misconfigured, may store credentials
- Web access visibility: web traffic could be detected by proxy logs, SIEMs, or web filters.
### Conclusion
Apache Guacamole is an extremely powerful web-based remote access solution for operators when used with a self-hosted server. When deployed through a RAD, it enables secure, stealthy, multi-protocol access to compromised environments while minimizing forensic artifacts on target machines.

