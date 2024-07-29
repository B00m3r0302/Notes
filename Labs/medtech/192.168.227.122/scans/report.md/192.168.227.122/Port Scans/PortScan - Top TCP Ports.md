```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Notes/Labs/medtech/192.168.227.122/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/192.168.227.122/scans/xml/_quick_tcp_nmap.xml" 192.168.227.122
```

[/home/kali/Notes/Labs/medtech/192.168.227.122/scans/_quick_tcp_nmap.txt](file:///home/kali/Notes/Labs/medtech/192.168.227.122/scans/_quick_tcp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Jul 29 07:55:21 2024 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN /home/kali/Notes/Labs/medtech/192.168.227.122/scans/_quick_tcp_nmap.txt -oX /home/kali/Notes/Labs/medtech/192.168.227.122/scans/xml/_quick_tcp_nmap.xml 192.168.227.122
Increasing send delay for 192.168.227.122 from 0 to 5 due to 262 out of 654 dropped probes since last increase.
Increasing send delay for 192.168.227.122 from 5 to 10 due to 11 out of 23 dropped probes since last increase.
adjust_timeouts2: packet supposedly had rtt of -193618 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -193618 microseconds.  Ignoring time.
Nmap scan report for 192.168.227.122
Host is up, received user-set (0.076s latency).
Scanned at 2024-07-29 07:55:22 EDT for 31s
Not shown: 999 closed tcp ports (reset)
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 61 OpenSSH 8.9p1 Ubuntu 3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 60:f9:e1:44:6a:40:bc:90:e0:3f:1d:d8:86:bc:a9:3d (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJ0/iBLK4jYimQjBeuwnG2ZFeJODcJDLQFBZoX/Gzn/BQc4aaYlaqHfDH/OwHFwffCzK6Ud/boKS1Hxo084jaLI=
|   256 24:97:84:f2:58:53:7b:a3:f7:40:e9:ad:3d:12:1e:c7 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAQKZnihoyWylk5RZg92RJyNHGV/3pGU9wPbfOFhtBQd
Aggressive OS guesses: Linux 2.6.32 (88%), Linux 2.6.32 or 3.10 (88%), Linux 2.6.39 (88%), Linux 3.10 - 3.12 (88%), Linux 3.4 (88%), Linux 3.5 (88%), Linux 4.4 (88%), Synology DiskStation Manager 5.1 (88%), WatchGuard Fireware 11.8 (88%), Linux 2.6.35 (87%)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=7/29%OT=22%CT=1%CU=30123%PV=Y%DS=4%DC=T%G=Y%TM=66A7
OS:8349%P=x86_64-pc-linux-gnu)SEQ(SP=102%GCD=1%ISR=10B%TI=Z%TS=A)SEQ(SP=102
OS:%GCD=1%ISR=10B%TI=Z%TS=C)SEQ(SP=102%GCD=1%ISR=10B%TI=Z%II=I%TS=A)SEQ(SP=
OS:102%GCD=1%ISR=10C%TI=Z%II=I%TS=A)OPS(O1=M551ST11NW7%O2=M551ST11NW7%O3=M5
OS:51NNT11NW7%O4=M551ST11NW7%O5=M551ST11NW7%O6=M551ST11)WIN(W1=FE88%W2=FE88
OS:%W3=FE88%W4=FE88%W5=FE88%W6=FE88)ECN(R=Y%DF=Y%T=40%W=FAF0%O=M551NNSNW7%C
OS:C=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=N)T5(R=
OS:Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=N)T7(R=N)U1(R=Y%DF=N%T=40%
OS:IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=D4DC%RUD=G)IE(R=Y%DFI=N%T=40%CD=S
OS:)

Uptime guess: 43.661 days (since Sat Jun 15 16:03:40 2024)
Network Distance: 4 hops
TCP Sequence Prediction: Difficulty=258 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 111/tcp)
HOP RTT      ADDRESS
1   73.19 ms 192.168.45.1
2   72.54 ms 192.168.45.254
3   73.58 ms 192.168.251.1
4   67.79 ms 192.168.227.122

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jul 29 07:55:53 2024 -- 1 IP address (1 host up) scanned in 32.34 seconds

```
