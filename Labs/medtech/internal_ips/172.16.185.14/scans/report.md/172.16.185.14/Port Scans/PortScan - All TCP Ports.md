```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.14/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.14/scans/xml/_full_tcp_nmap.xml" 172.16.185.14
```

[/home/kali/Notes/Labs/medtech/internal_ips/172.16.185.14/scans/_full_tcp_nmap.txt](file:///home/kali/Notes/Labs/medtech/internal_ips/172.16.185.14/scans/_full_tcp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Jul 31 12:30:46 2024 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/kali/Notes/Labs/medtech/internal_ips/172.16.185.14/scans/_full_tcp_nmap.txt -oX /home/kali/Notes/Labs/medtech/internal_ips/172.16.185.14/scans/xml/_full_tcp_nmap.xml 172.16.185.14
Nmap scan report for 172.16.185.14
Host is up, received user-set (0.099s latency).
Scanned at 2024-07-31 12:30:46 EDT for 817s
Not shown: 65534 filtered tcp ports (no-response)
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 64 OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 eb:0e:77:7c:69:f2:4a:a5:65:2a:1c:ec:ec:6e:79:19 (RSA)
|_ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCqxAUvVy22GziZwvvvS6nASJ20EXFRbsSkEyr1J+9Fvu2OL5QwOdydPaPXWS3wZzuPw3EgrvrZX8KsSg2e2sUMbCgJl/dPRDALtOXix1PgP7gb8fxuejC+fmLEcdEQt8axhMuenMfi7u1WcztYbzUrKY46iRnd92hvOxabNWdFdflnnwNotOh8SWY7v4OFZzozr9kb3RwlEZClS4E5/7k8M5Ng96wDtjP5V4D7+yipOOkY+PRGd0HK6ZM8Itqj3Ym7XBHYQ0Q3vVJ5hSdlwyrppv8nVA14i9yiHvuomt0R6DGgMftZ9rOHQ6HwAk6rmTierdht6QkHENnnjbv8uzVX7rFeuy7wolVKxyBrXDHevSF/fzFJ6oihCetIHw0C4eBpteRcytRFgU2Ezpkg9VnPTbiXgkVgKiG2vm/ziJK3OVOpUCaEcHbIoIX6egXdQt+6kzJt440YuWfOw9hOBqm1AC2d0lVl752A4WqL5PLdclg89S4rnNRKqhCPHihz4g8=
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
No OS matches for host
TCP/IP fingerprint:
SCAN(V=7.94SVN%E=4%D=7/31%OT=22%CT=%CU=%PV=Y%G=N%TM=66AA69E7%P=x86_64-pc-linux-gnu)
SEQ(SP=109%GCD=1%ISR=107%TI=I%CI=I%II=RI%TS=A)
SEQ(SP=109%GCD=1%ISR=107%TI=I%CI=I%II=RI%TS=B)
OPS(O1=M5B4NNT11NW7%O2=M5B4NNT11NW7%O3=M5B4NNT11NW7%O4=M5B4NNT11NW7%O5=M5B4NNT11NW7%O6=M5B4NNT11)
WIN(W1=7200%W2=7200%W3=7200%W4=7200%W5=7200%W6=7200)
ECN(R=Y%DF=N%TG=40%W=7200%O=M5B4NW7%CC=N%Q=)
T1(R=Y%DF=N%TG=40%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=Y%DF=N%TG=40%W=0%S=Z%A=S%F=AR%O=%RD=0%Q=)
T3(R=Y%DF=N%TG=40%W=7200%S=O%A=S+%F=AS%O=M5B4NNT11NW7%RD=0%Q=)
T4(R=Y%DF=N%TG=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T6(R=Y%DF=N%TG=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T7(R=Y%DF=N%TG=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=N)
IE(R=Y%DFI=S%TG=40%CD=S)

Uptime guess: 15.002 days (since Tue Jul 16 12:41:57 2024)
TCP Sequence Prediction: Difficulty=265 (Good luck!)
IP ID Sequence Generation: Incrementing by 2
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT      ADDRESS
1   98.68 ms 172.16.185.14

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jul 31 12:44:23 2024 -- 1 IP address (1 host up) scanned in 817.77 seconds

```
