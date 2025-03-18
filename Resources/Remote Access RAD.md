# Remote connections and IP identification
When the RAD is connected to the Wi-Fi puck or cellular hat it will now be assigned a Network Address Translation (NAT) IP address behind a public IP. NAT is a technique used to map private IP addresses within a local network to a single public IP address when accessing external networks like the internet. This process is performed by a router/firewall (or in our case the Wi-Fi puck or cellular hat) and helps conserve IPv4 addresses while providing a level of security by hiding internal network structures. However, NAT negatively impacts our ability to connect to our RAD because it is assigned a private IP address behind the public IP address and is not directly accessible to our local machines.

RFC 1918 (for IPv4) and RFC 4193 (for IPv6) define private IP address schemes. These addresses are reserved for internal network use and are not routable on the public internet. There are three main private IP ranges:

| IP Range                    | Subnet Mask | CIDR Notation  | Total Ips  | Typical Usage                   |
| --------------------------- | ----------- | -------------- | ---------- | ------------------------------- |
| 10.0.0.0-10.255.255.255     | 255.0.0.0   | 10.0.0.0/8     | 16,777,216 | Large enterprises & ISPs        |
| 172.16.0.0-172.31.255.255   | 255.240.0.0 | 172.16.0.0/12  | 1,048,576  | Medium-sized corporate networks |
| 192.168.0.0-192.168.255.255 | 255.255.0.0 | 192.168.0.0/16 | 65,536     | Home & small business networks  |

To bypass NAT and access our RAD from our local machine we need a way for it to be assigned a unique public/pseudo-public IP address that we can connect to it from. This can be done a variety of ways but the easiest is using Software Defined Networking (SDN) and Virtual Private Networks (VPN) the most common of which are Zero-Tier and WireGuard. Other methods could include port forwarding, proxying, etc. This document will go over Zero-Tier and how to configure a device within a Zero-Tier network.

## ZeroTier
ZeroTier is an open-source, peer-to-peer virtual networking solution that enables secure, encrypted communication between devices across the internet as if they were on the same LAN. It functions like a hybrid between a VPN and SD-WAN offering seamless connectivity without the complexity of traditional VPNs or NAT traversal issues.
### How ZeroTier Works
- Devices install the ZeroTier client and join a virtual network using a unique network ID.
- ZeroTier assigns each device a private virtual IP that remains consistent across different physical networks.
- It automatically handles NAT traversal allowing devices behind firewalls and NATs to connect directly without port forwarding.
### Benefits of ZeroTier For Remote Connections
- Bypassing NAT and Firewall Restrictions
    - ZeroTier eliminates the need for port forwarding or NAT traversal tricks.
    - It works in restrictive network environments where traditional SSH tunnels or VPNs may be blocked.
    - Unlike other VPN providers including WireGuard, ZeroTier finds the best path for connectivity without complex firewall rules.
- Stealth & Low Detection Profile
    - ZeroTier traffic blends into normal traffic because it is UDP-based with dynamic ports which makes detection harder.
    - It can be configured to mimic legitimate remote management traffic.
    - There are no static listener ports which makes it les suspicious to IDS/IPS monitoring.
- Secure Encrypted Communication
    - ZeroTier uses AES-256 encryption which ensures traffic between devices remains confidential.
    - Built-in Access Control Lists (ACLs) allow operators to restrict access per device.
- Facilitates Covert Command & Control (C2) Channels
    - A ZeroTier virtual network can be used as a C2 infrastructure for compromised hosts.
    - Operators can issue commands, exfiltrate data, or pivot without alerting most network security tools.
    - It can be combined with proxychains, reverse shells, or Metasploit for deeper infiltration.
### Installation
After setting up an account on zerotier.com you will be presented with a unique identifier for your virtual network. This in conjunction with the ZeroTier-CLI is how you will connect to the ZeroTier network.
- Install ZeroTier
```bash
curl -s https://install.zerotier.com | sudo bash
```
- Join the network
```bash
sudo zerotier-cli join <NETWORK_ID>
```
- The operator/network owner will then need to approve the device in the administration console of the ZeroTier web UI and the terminal output for the join command should be “200 JOIN OK”
- The operator can then get the assigned virtual IP address with the following command:
```bash
sudo zerotier-cli listnetworks
```
- The output is the address that the operator will be using to connect to the RAD throughout prosecution of the target network.
- This address can also be found with the “ip” command and identifying the ip address that matches what the RAD was assigned in the web UI with:
```bash
ip -c a
```

- Using hostname -I locally
    
- Checking the router’s DHCP lease table
    
- Scanning the network with nmap
    
- Using arp -a to find the device
# VPN & Remote Access
A Virtual Private Network (VPN) server allows secure, encrypted tunnels between a RAD deployed in a target environment and an attacker’s local machine. Most times we utilize ZeroTier SDN, but VPNs can be used in its place to bypass NAT and provide secure communication to the RAD and target network. This setup provides stealthy, persistent access, hides traffic inside encrypted tunnels, and bypasses network security controls.
## Why use a VPN on a RAD instead of other tunneling methods?
- Encrypted and hard to detect
    - VPN traffic is encrypted and resembles normal user VPN traffic.
- Reliable long-term access
    - Unlike SSH tunnels, VPN connections automatically reconnect after network interruptions
- Supports full network access
    - Unlike reverse shells, VPNs provide access to all network services.
- Can route all traffic through the target network.
    - Unlike SOCKS proxies, VPNs support full layer 3 network connectivity.
## Why Use a VPN instead of ZeroTier?
- More control over infrastructure
    - With a VPN you control the entire infrastructure
    - ZeroTier relies on ZeroTier’s central servers for peer discovery, introducing a third-party dependency
- No external dependencies or cloud services
    - VPNs don’t rely on external cloud services, while ZeroTier relies on a centralized coordination server for establishing connections
    - This means a VPN works even in air-gapped environments, while ZeroTier requires internet access
- Better OPSEC for covert operations
    - VPN traffic blends in as normal encrypted VPN traffic (especially WireGuard)
    - ZeroTier’s traffic can be flagged by security tools since it’s less common in enterprise networks
    - Security teams monitoring network traffic may detect and block ZeroTier easier than a generic VPN
- More granular firewall & access controls
    - With VPNs you configure firewall rules and access controls yourself
    - ZeroTier automates network routing and access, wwhich can introduce OPSEC risks if misconfigured
- More reliable for long-term access in segmented networks
    - If ZeroTier’s servers go down, the connection will fail
    - VPNs are self-hosted, meaning they remain operational even if external services are blocked
## When would ZeroTier be a better choice?
- Easier to set up and deploy
    - ZeroTier requires little configuration compared to setting up OpenVPN or WireGuard
    - If you need quick, ad-hoc access without a full VPN setup, ZeroTier is simpler.
- Works through NAT without port forwarding
    - ZeroTier can establish direct connections even if the RAD is behind a firewall or NAT
    - VPNs often require port forwarding on the target network, which may not always be feasible
- Peer-to-peer networking & multiple clients
    - ZeroTier allows multiple devices to connect as if they’re on the same LAN, which is useful for multi-system access.
    - VPNs usually require routing rules to enable similar connectivity.
- Good for quick & disposable access
    - If stealth isn’t a concern, and you just need fast temporary access, ZeroTier is more convenient
## Setting up an OpenVPN server
OpenVPN is a reliable, widely supported, but slightly slower VPN
### Installation & Configuration
- Ensure that your environment and software have been updated
```bash
sudo apt update && sudo apt upgrade -y
```
- Install OpenVPN and dependancies
```bash
sudo apt install -y openvpn easy-rsa
```
- Set up the Public Key Infrastructure (PKI)
```bash
make-cadir ~/openvpn-ca
```
```bash
cd ~/openvpn-ca
```
```bash
source vars
```
```bash
./clean-all
```
```bash
./build-ca
```
- Generate server keys
```bash
./build-key-server server
```
```bash
./build-dh
```
```bash
openvpn --genkey --secret keys/ta.key
```
- Configure the OpenVPN server by creating a new configuration file
```bash
sudo vim /etc/openvpn/server.conv
```
- Add the content below
```ini
port 1194
proto udp
dev tun
ca /etc/openvpn/keys/ca.crt
cert /etc/openvpn/keys/server.crt
key /etc/openvpn/keys/server.key
dh /etc/openvpn/keys/dh2048.pem
tls-auth /etc/openvpn/keys/ta.key 0
server 10.8.0.0 255.255.255.0
keepalive 10 120
cipher AES-256-CBC
persist-key
persist-tun
status /var/log/openvpn-status.log
verb 3
```
- Start the OpenVPN server
```bash
sudo systemctl start openvpn@server
```
- Enable the OpenVPN server to start on boot
```bash
sudo systemctl enable openvpn@server
```
- Generate client certificates
```bash
cd ~/openvpn-ca
```
```bash
source vars
```
```bash
./build-key client1
```
- Execute a file transfer of client1.ovpn to your local machine to establish a connection to the RAD
#### Connecting to the VPN
- Command
```bash
sudo openvpn client1.ovpn
```
Now all the traffic to the client network will be tunneled through the RAD based on the configuration you set in the OpenVPN configuration file
#### Breakdown of the configuration settings
- Port/proto
    - Server listens on port 1194 UDP
- Dev tun
    - Uses a TUN (layer 3) virtual interface for routing IP traffic. If bridging is needed, use “dev tap” for layer 2 ethernet bridging
- Ca
    - Specifies the CA certificate for verifying client certificates  
- Cert
    - The VPN server’s SSL/TLS certificate (issued by the CA)
- Key
    - The VPN server’s private key (must be kept secret)    
- Dh
    - Diffie-Hellman parameters for key exchange  
- Tls-auth
    - Uses a pre-shared TLS authentication key to prevent DoS attacks and unauthorized connections
- Cipher AES-256-CBC
    - Uses AES-256 encryption for all VPN traffic
- Auth SHA256
    - Uses SHA-256 for HMAC authentication to ensure data integrity
- Server 10.8.0.0 255.255.255.0
    - Defines the VPN subnet and netmask. Clients will get an IP from this range
- Push “redirect-gateway def1 bypass-dhcp”
    - Forces clients to route all internet traffic through the VPN, ensuring anonymity
- Push “dhcp-option DNS 1.1.1.1”
    - Pushes Cloudflare DNS to clients to prevent DNS leaks
- IF YOU ONLY WANT ACCESS TO SPECIFIC INTERNAL NETWORKS USE
    - Push “route IP/CIDR_TARGET_NETWORK TARGET_NETWORK_NETMASK”
- Keepalive 10 120
    - Sends a ping every 10 seconds and disconnects clients after 120 seconds of inactivity
- Persist-key
    - Prevents OpenVPN from reloading keys on restart (helps with connection stability)
## Setting up a WireGuard VPN
WireGuard is a modern, faster alternative to OpenVPN with strong security features
### Installation & Configuration
- Make sure your environment and software are updated
```bash
sudo apt update && sudo apt upgrade -y
```
- Install WireGuard
```bash
sudo apt install -y wireguard
```
- Generate server keys
```bash
wg genkey | tee server_private.key | wg pubkey > server_public.key
```
- Configure WireGuard server by creating the configuration file
```bash
sudo vim /etc/wireguard/wg0.conf
```
- Add the content below to the file
```ini
[Interface]
PrivateKey = <server_private.key>
Address = 10.10.0.1/24
ListenPort = 51820
Saveconfig = true
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT

[Peer]
PublicKey = <client_public.key>
AllowedIPs = 10.10.0.2/32
```
- Start the WireGuard server
```bash
sudo systemctl start wg-quick@wg0
```
- Enable the WireGuard server to start on boot
```bash
sudo systemctl enable wg-quick@wg0
```
- Execute a file transfer to send the server public key to your local machine you will be connecting from
- On the connecting or client machine use the steps above to update your environment and download WireGuard
- Generate client keys
```bash
wg genkey | tee privatekey | wg pubkey > publickey
```
- Create the client configuration file
```bash
sudo vim /etc/wireguard/wg-client.conf
```
- Add the content below
```ini
[Interface]
PrivateKey = CLIENT_PRIVATE_KEY
Address = 10.10.0.2/24
DNS = 10.0.0.1

[Peer]
PublicKey = SERVER_PUBLIC_KEY
Endpoint = SERVER_IP:51820
AllowedIPs = 0.0.0.0/0 ::/0
PersistentKeepalive = 25
```
- Execute a file transfer and send the publickey of the client to the server
- Edit the configuration file under PEER publickey to point to the public key of the client that was transferred
- Save and restart WireGuard to apply the changes on  the server
```bash
sudo systemctl restart wg-quick@wg0
```
- Back on the client machine start the VPN
```bash
sudo systemctl start wg-quick@wg-client
```
- Enable the service to start on boot with 
```bash
sudo systemctl enable wg-quick@wg-client
```
- Check the status of the connection with
```bash
sudo wg show
```
#### Breakdown of the SERVER configuration settings
- Interface defines the settings for the server
    - PrivateKey is the private key of the server
    - Address means that the server’s IP is 10.10.0.1/24 and listens on port 51820
- peer define the settings for the other device(s) in the connection
    - PublicKey is the client’s public key
    - AllowedIPs means the client is restricted to the IP of 10.10.0.2/32
#### Breakdown of the CLIENT configuration settings
- Interface section (client settings)
    - PrivateKey is the client’s private key (do not share)
    - Address is the client’s assigned VPN IP (from the same subnet as the server)
    - DNS is the DNS resolver (can be set to the WireGuard server or any preferred DNS server)
- Peer section (server details)
    - PublicKey is the WireGuard server’s public key
    - Endpoint is the server’s public IP and port (51820 by default)
    - AllowedIPs determines what traffic is routed through the VPN
        - 0.0.0.0/0, ::/0 routes all traffic through the VPN
        - 10.0.0.0/24 routes only internal VPN traffic
    - PersistentKeepalive = 25 sends keepalive packets every 25 seconds (important for NAT traversal)
## General
Once a VPN connection is established, all traffic from the attacker’s machine routes through the RAD on the target network allowing full access without directly exposing the attacker’s machine.
Once inside a network, the VPN can be used to:
- Scan the target network with tools like “nmap” and “BloodHound”
- Intercept and relay traffic (e.g. MITM attacks)
- Maintain stealthy remote access to compromised hosts
## Conclusion
Using a VPN on a RAD gives an attacker stealthy, persistent access to a compromised target network. While OpenVPN offers more stability, WireGuard provides speed and simplicity, making it a great choice for low-resource environments.