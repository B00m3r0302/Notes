## IP
The “ip” tool in Linux is a powerful utility for managing and configuring network interfaces, routes and addresses. It replaces the older “ifconfig” and “route” commands and is a part of the “iproute2” package which is often installed by default on most Linux operating systems.

## IFMETRIC
“ifmetric” is a tool used in Linux to **set the metric (priority)** of network interfaces which affects how routes are prioritized.

## NMTUI
Common issues related to remote operations have to do with connectivity. Additionally, users do not always have access to a GUI so it’s important to know how to check and manage network interfaces through the command line or with tools such as Network Manager Terminal User Interface (nmtui). Nmtui provides a simple, text-based interface for users to configure networking without needing to edit configuration files manually. It is useful for configuring Wi-Fi, Ethernet, VPN and static IP addresses on headless servers, RADs or Linux workstations. However, the device must be using NetworkManager to manage its connections.
### Installation
- Commands
```bash
sudo apt update && sudo apt install -y network-manager
```
## Networking in the terminal
### How it works:
- Each network interface (e.g., eth0, wlan0, tun0) has a **metric value** assigned.
- Lower metric values indicate **higher priority** in routing decisions.
- If multiple interfaces are available, Linux will prefer the one with the **lowest metric** when determining the default route.
- To effectively set our default route, we will need to do the following:
    1. Identify the default route with “ip.”
    2. Use “ifmetric” to prioritize our external connection in the operating system.
### Commands
- Identify the metric for the default route 
```bash
ip route
```
- Change the metric value with 
```bash
sudo ifmetric <INTERFACE> <NUMBER_LOWER_THAN_TARGET_NIC>
```
- After adjusting the metric, we should view the default route again to ensure our interface has been given a higher priority (lower number) than the default interface the last time we checked the route.
```bash
ip route
```

### NMTUI Interface
- Access with 
```bash
sudo nmtui
```
  
- Main menu options
    
    - Once nmtui is open you’ll see three main options:
        
    - Edit a connection
        
        - Create, edit, or delete network configurations
            
    - Activate a connection
        
        - Enable or disable network interfaces
            
    - Set system hostname
        
        - Change the system’s hostname
            
    - You can navigate using the arrow keys and select options using enter
        
- Editing a network connection
    
    - To modify an existing network connection or set up a new one:
        
    - Select “Edit a connection” and press enter
        
    - Choose an existing connection (or create a new one by selecting “Add”)
        
    - Modify the following settings
        
        - Connection name
            
        - IP address (static or DHCP)
            
        - Gateway
            
        - DNS servers
            
        - MAC address cloning
            
        - Wi-Fi SSID and password
            
    - Use tab to navigate to “OK” and press Enter to save changes
        
- Activating or deactivating a connection
    
    - To enable or disable a network connection
        
    - Select “Activate a connection” from the main menu
        
    - Choose the interface you want to activate or deactivate
        
    - Press enter to toggle the connection
        
    - To check if the connection is active run
```bash
ip -c a
```
- Setting the system hostname
    
    - To change the system hostname
        
    - Select “Set system hostname”
        
    - Enter the desired hostname
        
    - Press OK to save the changes
        
    - Verify the hostname change with
```bash
hostnamectl
```
  
- Restarting NetworkManager to apply changes
    
    - After making changes, restart NetworkManager to apply them
```bash
sudo systemctl restart NetworkManager
```
