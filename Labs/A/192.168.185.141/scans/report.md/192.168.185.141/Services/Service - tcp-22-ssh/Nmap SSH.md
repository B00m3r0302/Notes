```bash
nmap -vv --reason -Pn -T4 -sV -p 22 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp22/tcp_22_ssh_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp22/xml/tcp_22_ssh_nmap.xml" 192.168.185.141
```

[/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp22/tcp_22_ssh_nmap.txt](file:///home/kali/Notes/Labs/A/192.168.185.141/scans/tcp22/tcp_22_ssh_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Aug  5 22:09:32 2024 as: nmap -vv --reason -Pn -T4 -sV -p 22 --script=banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods -oN /home/kali/Notes/Labs/A/192.168.185.141/scans/tcp22/tcp_22_ssh_nmap.txt -oX /home/kali/Notes/Labs/A/192.168.185.141/scans/tcp22/xml/tcp_22_ssh_nmap.xml 192.168.185.141
Nmap scan report for 192.168.185.141
Host is up, received user-set (0.068s latency).
Scanned at 2024-08-05 22:09:33 EDT for 3s

PORT   STATE SERVICE REASON          VERSION
22/tcp open  ssh     syn-ack ttl 125 OpenSSH for_Windows_8.1 (protocol 2.0)
| ssh-auth-methods: 
|   Supported authentication methods: 
|     publickey
|     password
|_    keyboard-interactive
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
| ssh-hostkey: 
|   3072 e0:3a:63:4a:07:83:4d:0b:6f:4e:8a:4d:79:3d:6e:4c (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDHi6qqQGQteAgLLakGf2MPORvtZSeF1gAL03sfUo/E/jsObuAOjzHPfw1OIfAyctU/gv17d0sz17kGDXbg4In4vxlnavXxnB/L2ipQLhAkFLo1YZLLwyUs0j1jiSW65Ax12A20nH0F3hbuqKsuWIPywR9XXc0cwhyY3ET06ZCbVVvP8ChGMd97uZTDeZtrnskYMXmqnfQpOGPL6e022+K5ud3MboyYXTlD0rGyVHyLCCXeg9QdxsVR5mZ8hSVCrwdX8Q4tb4kLYi+wpPx1KCirHEk/8O8I7YuA5KR4AeaMVSlqUhlm9MXaNw+5WZD2xOue0ZPCx2gxgKgndoUDfAagZrHr3dzgMUDgUnKTbtL/EIZdyzKh5C1TrN+yplSpqYjK975Q1qas7SUmzanN9S/PnhFFer/0j6hTtGlRalbxX12i2ifC0314ifnHY3Zz+2VD49RARArwvZR+7KcGKP+5tpCl9IyVf1xSKFFnJ0cQdhuAgJnkCfQXaQLHTzqSbys=
|   256 3f:16:ca:33:25:fd:a2:e6:bb:f6:b0:04:32:21:21:0b (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOpOTM37eUD8SUKAqFVSNV8ECDl5yUqV7a41c39cXyPE6EMeNbKxWvQDoTw+WEYArHFAEj3SZbFupIZoZmvjFuA=
|   256 fe:b0:7a:14:bf:77:84:9a:b3:26:59:8d:ff:7e:92:84 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICyZUVdHOqTpEFyvELlmc7sCN1XFXQo7RdZdTRTPO2uJ
|_banner: SSH-2.0-OpenSSH_for_Windows_8.1

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Aug  5 22:09:36 2024 -- 1 IP address (1 host up) scanned in 4.00 seconds

```
