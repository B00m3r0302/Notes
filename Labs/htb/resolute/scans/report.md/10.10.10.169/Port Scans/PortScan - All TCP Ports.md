```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/htb/resolute/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/htb/resolute/scans/xml/_full_tcp_nmap.xml" 10.10.10.169
```

[/home/kali/Notes/Labs/htb/resolute/scans/_full_tcp_nmap.txt](file:///home/kali/Notes/Labs/htb/resolute/scans/_full_tcp_nmap.txt):

```
# Nmap 7.95 scan initiated Sun Jan 26 20:13:35 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/kali/Notes/Labs/htb/resolute/scans/_full_tcp_nmap.txt -oX /home/kali/Notes/Labs/htb/resolute/scans/xml/_full_tcp_nmap.xml 10.10.10.169
Increasing send delay for 10.10.10.169 from 0 to 5 due to 187 out of 466 dropped probes since last increase.
Increasing send delay for 10.10.10.169 from 5 to 10 due to 11 out of 25 dropped probes since last increase.
Warning: 10.10.10.169 giving up on port because retransmission cap hit (6).
Nmap scan report for 10.10.10.169
Host is up, received user-set (0.083s latency).
Scanned at 2025-01-26 20:13:36 EST for 1494s
Not shown: 65220 closed tcp ports (reset), 290 filtered tcp ports (no-response)
PORT      STATE SERVICE    REASON          VERSION
53/tcp    open  tcpwrapped syn-ack ttl 127
88/tcp    open  tcpwrapped syn-ack ttl 127
135/tcp   open  tcpwrapped syn-ack ttl 127
139/tcp   open  tcpwrapped syn-ack ttl 127
389/tcp   open  tcpwrapped syn-ack ttl 127
445/tcp   open  tcpwrapped syn-ack ttl 127
464/tcp   open  tcpwrapped syn-ack ttl 127
593/tcp   open  tcpwrapped syn-ack ttl 127
636/tcp   open  tcpwrapped syn-ack ttl 127
3268/tcp  open  tcpwrapped syn-ack ttl 127
3269/tcp  open  tcpwrapped syn-ack ttl 127
5985/tcp  open  tcpwrapped syn-ack ttl 127
9389/tcp  open  tcpwrapped syn-ack ttl 127
47001/tcp open  tcpwrapped syn-ack ttl 127
49664/tcp open  tcpwrapped syn-ack ttl 127
49665/tcp open  tcpwrapped syn-ack ttl 127
49666/tcp open  tcpwrapped syn-ack ttl 127
49667/tcp open  tcpwrapped syn-ack ttl 127
49671/tcp open  tcpwrapped syn-ack ttl 127
49676/tcp open  tcpwrapped syn-ack ttl 127
49677/tcp open  tcpwrapped syn-ack ttl 127
49688/tcp open  tcpwrapped syn-ack ttl 127
49919/tcp open  tcpwrapped syn-ack ttl 127
50294/tcp open  tcpwrapped syn-ack ttl 127
50513/tcp open  tcpwrapped syn-ack ttl 127
OS fingerprint not ideal because: Didn't receive UDP response. Please try again with -sSU
No OS matches for host
TCP/IP fingerprint:
SCAN(V=7.95%E=4%D=1/26%OT=50513%CT=1%CU=%PV=Y%G=N%TM=6796E396%P=x86_64-pc-linux-gnu)
SEQ()
ECN(R=N)
T1(R=N)
T2(R=N)
T3(R=N)
T4(R=N)
T5(R=N)
T6(R=N)
T7(R=N)
U1(R=N)
IE(R=N)


Host script results:
| smb2-time: 
|   date: 2025-01-27T01:45:29
|_  start_date: 2025-01-27T01:13:52
|_clock-skew: 6m59s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 52471/tcp): CLEAN (Timeout)
|   Check 2 (port 47337/tcp): CLEAN (Failed to receive data)
|   Check 3 (port 55070/udp): CLEAN (Data received, but checksum was invalid (possibly INFECTED))
|   Check 4 (port 30335/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked

TRACEROUTE (using port 49673/tcp)
HOP RTT    ADDRESS
1   ... 30

Read data files from: /usr/share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Jan 26 20:38:30 2025 -- 1 IP address (1 host up) scanned in 1494.53 seconds

```
