```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/A/192.168.145.144/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/A/192.168.145.144/scans/xml/_full_tcp_nmap.xml" 192.168.145.144
```

[/home/kali/Notes/Labs/A/192.168.145.144/scans/_full_tcp_nmap.txt](file:///home/kali/Notes/Labs/A/192.168.145.144/scans/_full_tcp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Aug  5 22:07:56 2024 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/kali/Notes/Labs/A/192.168.145.144/scans/_full_tcp_nmap.txt -oX /home/kali/Notes/Labs/A/192.168.145.144/scans/xml/_full_tcp_nmap.xml 192.168.145.144
Increasing send delay for 192.168.145.144 from 0 to 5 due to 39 out of 96 dropped probes since last increase.
Increasing send delay for 192.168.145.144 from 5 to 10 due to 60 out of 149 dropped probes since last increase.
Nmap scan report for 192.168.145.144
Host is up, received user-set (0.0034s latency).
Scanned at 2024-08-05 22:07:57 EDT for 8293s
Not shown: 47362 filtered tcp ports (no-response), 18139 filtered tcp ports (time-exceeded), 32 filtered tcp ports (net-unreach)
PORT    STATE  SERVICE REASON         VERSION
53/tcp  open   domain  syn-ack ttl 64 Unbound
113/tcp closed ident   reset ttl 64
OS fingerprint not ideal because: Didn't receive UDP response. Please try again with -sSU
No OS matches for host
TCP/IP fingerprint:
SCAN(V=7.94SVN%E=4%D=8/6%OT=53%CT=113%CU=%PV=Y%DS=1%DC=T%G=N%TM=66B1A5E2%P=x86_64-pc-linux-gnu)
SEQ(SP=104%GCD=1%ISR=109%TI=RD%TS=A)
SEQ(SP=104%GCD=3%ISR=109%TI=RD%TS=A)
OPS(O1=T11M560SNW0%O2=T11M560SNW0%O3=NNT11M560NW0%O4=T11M560SNW0%O5=T11M560SNW0%O6=T11M560S)
WIN(W1=EA60%W2=EA60%W3=EA60%W4=EA60%W5=EA60%W6=EA60)
ECN(R=Y%DF=N%TG=40%W=EA60%O=NNM560SNW0%CC=N%Q=)
T1(R=Y%DF=N%TG=40%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=Y%DF=N%TG=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T5(R=N)
T5(R=Y%DF=Y%TG=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
T6(R=N)
T7(R=N)
U1(R=N)
IE(R=N)

Uptime guess: 27.656 days (since Tue Jul  9 08:41:43 2024)
Network Distance: 1 hop
TCP Sequence Prediction: Difficulty=260 (Good luck!)
IP ID Sequence Generation: Randomized

TRACEROUTE (using port 113/tcp)
HOP RTT     ADDRESS
1   4.82 ms 192.168.145.144

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Aug  6 00:26:10 2024 -- 1 IP address (1 host up) scanned in 8294.71 seconds

```