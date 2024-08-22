```bash
nmap -vv --reason -Pn -T4 -sV -p 22 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp22/tcp_22_ssh_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp22/xml/tcp_22_ssh_nmap.xml" 192.168.196.144
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp22/tcp_22_ssh_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp22/tcp_22_ssh_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:00:44 2024 as: nmap -vv --reason -Pn -T4 -sV -p 22 --script=banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp22/tcp_22_ssh_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp22/xml/tcp_22_ssh_nmap.xml 192.168.196.144
Nmap scan report for 192.168.196.144
Host is up, received user-set (0.14s latency).
Scanned at 2024-08-21 13:00:45 EDT for 13s

PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 61 OpenSSH 8.9p1 Ubuntu 3 (Ubuntu Linux; protocol 2.0)
| ssh2-enum-algos: 
|   kex_algorithms: (10)
|       curve25519-sha256
|       curve25519-sha256@libssh.org
|       ecdh-sha2-nistp256
|       ecdh-sha2-nistp384
|       ecdh-sha2-nistp521
|       sntrup761x25519-sha512@openssh.com
|       diffie-hellman-group-exchange-sha256
|       diffie-hellman-group16-sha512
|       diffie-hellman-group18-sha512
|       diffie-hellman-group14-sha256
|   server_host_key_algorithms: (4)
|       rsa-sha2-512
|       rsa-sha2-256
|       ecdsa-sha2-nistp256
|       ssh-ed25519
|   encryption_algorithms: (6)
|       chacha20-poly1305@openssh.com
|       aes128-ctr
|       aes192-ctr
|       aes256-ctr
|       aes128-gcm@openssh.com
|       aes256-gcm@openssh.com
|   mac_algorithms: (10)
|       umac-64-etm@openssh.com
|       umac-128-etm@openssh.com
|       hmac-sha2-256-etm@openssh.com
|       hmac-sha2-512-etm@openssh.com
|       hmac-sha1-etm@openssh.com
|       umac-64@openssh.com
|       umac-128@openssh.com
|       hmac-sha2-256
|       hmac-sha2-512
|       hmac-sha1
|   compression_algorithms: (2)
|       none
|_      zlib@openssh.com
|_banner: SSH-2.0-OpenSSH_8.9p1 Ubuntu-3
| ssh-hostkey: 
|   256 fb:ea:e1:18:2f:1d:7b:5e:75:96:5a:98:df:3d:17:e4 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKsVbkM4POotpYfh0WatqzVPFWbtiDS0sp2YAxr55TtgpEbeVB8j6CCJjqKJvbgTkIvClq52Jd3XzmYJaK07Ue4=
|   256 66:f4:54:42:1f:25:16:d7:f3:eb:f7:44:9f:5a:1a:0b (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDqyf3tokk0DxqCJOiczEEGgFJsXh09VNspar/n7CtRs
| ssh-auth-methods: 
|   Supported authentication methods: 
|     publickey
|_    password
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:00:59 2024 -- 1 IP address (1 host up) scanned in 14.61 seconds

```
