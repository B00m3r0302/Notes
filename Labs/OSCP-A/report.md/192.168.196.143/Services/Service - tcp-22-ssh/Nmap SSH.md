```bash
nmap -vv --reason -Pn -T4 -sV -p 22 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp22/tcp_22_ssh_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp22/xml/tcp_22_ssh_nmap.xml" 192.168.196.143
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp22/tcp_22_ssh_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp22/tcp_22_ssh_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:09:28 2024 as: nmap -vv --reason -Pn -T4 -sV -p 22 --script=banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp22/tcp_22_ssh_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp22/xml/tcp_22_ssh_nmap.xml 192.168.196.143
Nmap scan report for 192.168.196.143
Host is up, received user-set (0.14s latency).
Scanned at 2024-08-21 13:09:30 EDT for 5s

PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 61 OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
|_banner: SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.4
| ssh-auth-methods: 
|   Supported authentication methods: 
|     publickey
|_    password
| ssh-hostkey: 
|   3072 23:4c:6f:ff:b8:52:29:65:3d:d1:4e:38:eb:fe:01:c1 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCi/7Md8C4Np6BJgxvw5Jb8jJ+RYx+s7Wc7jWxTHhTMURFOTc6HH2XC0rvbZukvws+KficflBsI/B7RVgY454RK1NOGOqVd5FSIY3qol4MGH2/Sq03mfjcc8aMgni5OZd2DNZY7e8auGa3fDOci6PXOZaYxwwjn52Vt/iNZu8sAv3rf1sRLAikvk5fGlEbxLu1+zXDCySqP0IgeR+i7JcWUp8+xiwp2ZmURcAsFkM0TBm07MJKD+T+zPru2YxvsICXMMG37rV22KFqmk2p/8PF18WUqJpDPnPYEKZwGjbxa71STgQfUcFXeXU9QX3ofz/g0ZpxEg8wk2O9fNvYdZ454isgPWtxhHe9wii18eq4DBizwfHao1OI8iKpPbkQlrKmOrPqU55LXJR84n68cCPp8yH8Pd8Mv+AzV+9h0/u72XB/0AaFcgT5u7SnGoiTrx5e2eMzI+lFkm5xY+KJw5ZvTaC3MnD3LJugV6axmAH+9L6LDrLV8dkLq6kV8KpS9Ej0=
|   256 0d:fd:36:d8:05:69:83:ef:ae:a0:fe:4b:82:03:32:ed (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLKaSNQY+Y3BFhxGXMm8uTdQnXJ1VbZEwFMoa1MUkYgu0vSwafvy6ffXVglWIlroS4axopq6HkpSA+2wnjp2E8s=
|   256 cc:76:17:1e:8e:c5:57:b2:1f:45:28:09:05:5a:eb:39 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIC3D5QMyrcUNcOicavOsnzna2L1/Fg2N7w7okmegpssB
| ssh2-enum-algos: 
|   kex_algorithms: (9)
|       curve25519-sha256
|       curve25519-sha256@libssh.org
|       ecdh-sha2-nistp256
|       ecdh-sha2-nistp384
|       ecdh-sha2-nistp521
|       diffie-hellman-group-exchange-sha256
|       diffie-hellman-group16-sha512
|       diffie-hellman-group18-sha512
|       diffie-hellman-group14-sha256
|   server_host_key_algorithms: (5)
|       rsa-sha2-512
|       rsa-sha2-256
|       ssh-rsa
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
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:09:35 2024 -- 1 IP address (1 host up) scanned in 6.99 seconds

```