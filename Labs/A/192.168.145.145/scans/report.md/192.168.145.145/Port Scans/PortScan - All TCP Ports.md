```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/A/192.168.145.145/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.145.145/scans/xml/_full_tcp_nmap.xml" 192.168.145.145
```

[/home/kali/Notes/Labs/A/192.168.145.145/scans/_full_tcp_nmap.txt](file:///home/kali/Notes/Labs/A/192.168.145.145/scans/_full_tcp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Aug  5 22:09:33 2024 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/kali/Notes/Labs/A/192.168.145.145/scans/_full_tcp_nmap.txt -oX /home/kali/Notes/Labs/A/192.168.145.145/scans/xml/_full_tcp_nmap.xml 192.168.145.145
Nmap scan report for 192.168.145.145
Host is up, received user-set (0.0027s latency).
Scanned at 2024-08-05 22:09:33 EDT for 106s
Not shown: 65496 filtered tcp ports (no-response), 38 filtered tcp ports (time-exceeded)
PORT   STATE SERVICE REASON         VERSION
53/tcp open  domain  syn-ack ttl 64 Unbound
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
No OS matches for host
TCP/IP fingerprint:
SCAN(V=7.94SVN%E=4%D=8/5%OT=53%CT=%CU=%PV=Y%DS=1%DC=T%G=N%TM=66B18647%P=x86_64-pc-linux-gnu)
SEQ(SP=102%GCD=1%ISR=110%TI=RD%TS=A)
SEQ(SP=102%GCD=1%ISR=110%TI=RD%TS=B)
OPS(O1=T11M560SNW0%O2=T11M560SNW0%O3=NNT11M560NW0%O4=T11M560SNW0%O5=T11M560SNW0%O6=T11M560S)
WIN(W1=EA60%W2=EA60%W3=EA60%W4=EA60%W5=EA60%W6=EA60)
ECN(R=Y%DF=N%TG=40%W=EA60%O=NNM560SNW0%CC=N%Q=)
T1(R=Y%DF=N%TG=40%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=Y%DF=N%TG=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
U1(R=N)
IE(R=N)

Uptime guess: 27.562 days (since Tue Jul  9 08:41:43 2024)
Network Distance: 1 hop
TCP Sequence Prediction: Difficulty=258 (Good luck!)
IP ID Sequence Generation: Randomized

TRACEROUTE (using port 53/tcp)
HOP RTT     ADDRESS
1   2.61 ms 192.168.145.145

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Aug  5 22:11:19 2024 -- 1 IP address (1 host up) scanned in 106.99 seconds

```
