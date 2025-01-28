```bash
nmap -vv --reason -Pn -T4 -sV -p 22 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/kali/Notes/Labs/htb/reel/scans/tcp22/tcp_22_ssh_nmap.txt" -oX "/home/kali/Notes/Labs/htb/reel/scans/tcp22/xml/tcp_22_ssh_nmap.xml" 10.10.10.77
```

[/home/kali/Notes/Labs/htb/reel/scans/tcp22/tcp_22_ssh_nmap.txt](file:///home/kali/Notes/Labs/htb/reel/scans/tcp22/tcp_22_ssh_nmap.txt):

```
# Nmap 7.95 scan initiated Mon Jan 27 20:52:45 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 22 --script=banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods -oN /home/kali/Notes/Labs/htb/reel/scans/tcp22/tcp_22_ssh_nmap.txt -oX /home/kali/Notes/Labs/htb/reel/scans/tcp22/xml/tcp_22_ssh_nmap.xml 10.10.10.77
Nmap scan report for 10.10.10.77
Host is up, received user-set (0.059s latency).
Scanned at 2025-01-27 20:52:46 EST for 2s

PORT   STATE SERVICE REASON          VERSION
22/tcp open  ssh     syn-ack ttl 127 OpenSSH 7.6 (protocol 2.0)
|_banner: SSH-2.0-OpenSSH_7.6
| ssh-auth-methods: 
|   Supported authentication methods: 
|     publickey
|     password
|_    keyboard-interactive
| ssh-hostkey: 
|   2048 82:20:c3:bd:16:cb:a2:9c:88:87:1d:6c:15:59:ed:ed (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDQkehAZGj87mZluxFiVu+GPAAnC/OQ9QKUF2wlIwvefrD2L4zWyGXlAgSbUq/MqujR/efrTIjPYWK+5Mlxc7gEoZBylGAPbdxFivL8YQs3dQPt6aHNF0v+ABS01L2qZ4ewd1sTi1TlT6LtWHehX2PBJ6S3LWG09v+E/3ue97y9gaOjfA6BCMWgQ7K3yvQeHrRpBSk/vQxfCh4TINwV3EGbGTfbs8VvvR+Et7weB5EOifgXfHbyh04KemONkceFSAnjRRYOgwvtXai9imsDJ8KtS2RMR197VK4MBhsY7+h0nOvUMgm76RcRc6N8GW1mn6gWp98Ds9VeymzAmQvprs97
|   256 23:2b:b8:0a:8c:1c:f4:4d:8d:7e:5e:64:58:80:33:45 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAw2CYanDlTRpGqzVXrfGTcAYVe/vUnnkWicQPzdfix5gFsv4nOGNUM+Fko7QAW0jqCFQKc8anGAwJjFGLTB00k=
|   256 ac:8b:de:25:1d:b7:d8:38:38:9b:9c:16:bf:f6:3f:ed (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICdDfn+n5xueGtHP20/aPkI8pvCfxb2UZA3RQdqnpjBk
| ssh2-enum-algos: 
|   kex_algorithms: (10)
|       curve25519-sha256
|       curve25519-sha256@libssh.org
|       ecdh-sha2-nistp256
|       ecdh-sha2-nistp384
|       ecdh-sha2-nistp521
|       diffie-hellman-group-exchange-sha256
|       diffie-hellman-group16-sha512
|       diffie-hellman-group18-sha512
|       diffie-hellman-group14-sha256
|       diffie-hellman-group14-sha1
|   server_host_key_algorithms: (5)
|       ssh-rsa
|       rsa-sha2-512
|       rsa-sha2-256
|       ecdsa-sha2-nistp256
|       ssh-ed25519
|   encryption_algorithms: (4)
|       chacha20-poly1305@openssh.com
|       aes128-ctr
|       aes192-ctr
|       aes256-ctr
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
|   compression_algorithms: (1)
|_      none

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan 27 20:52:48 2025 -- 1 IP address (1 host up) scanned in 2.60 seconds

```
