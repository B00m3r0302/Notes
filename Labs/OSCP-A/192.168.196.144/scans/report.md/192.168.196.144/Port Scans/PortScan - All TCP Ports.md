```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/xml/_full_tcp_nmap.xml" 192.168.196.144
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/_full_tcp_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/_full_tcp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:00:01 2024 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/_full_tcp_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/xml/_full_tcp_nmap.xml 192.168.196.144
Warning: 192.168.196.144 giving up on port because retransmission cap hit (6).
adjust_timeouts2: packet supposedly had rtt of 8042609 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8042609 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8032379 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8032379 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8022512 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8022512 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8012389 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8012389 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8014913 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8014913 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8004697 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8004697 microseconds.  Ignoring time.
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
adjust_timeouts2: packet supposedly had rtt of 8201476 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8201476 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8322688 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8322688 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8183360 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8183360 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8172409 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8172409 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8163449 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8163449 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8151227 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8151227 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8145489 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8145489 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8135263 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8135263 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8125195 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8125195 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8115342 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8115342 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8203616 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8203616 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8193159 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8193159 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8182896 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8182896 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8115418 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8115418 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8024740 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8024740 microseconds.  Ignoring time.
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
adjust_timeouts2: packet supposedly had rtt of 8666416 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8666416 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8654108 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8654108 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8643931 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8643931 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8632492 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8632492 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8686118 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8686118 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8728931 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8728931 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8599499 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8599499 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8589426 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8589426 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8625370 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8625370 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8637060 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8637060 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9620928 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9620928 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9643645 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9643645 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9631511 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9631511 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9610252 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9610252 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9627128 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9627128 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9978312 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9978312 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10003229 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10003229 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10000416 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10000416 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9972810 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9972810 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10015520 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10015520 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10030890 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10030890 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10023379 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10023379 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10037536 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10037536 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10051572 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10051572 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10062378 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10062378 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9977880 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9977880 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9218341 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9218341 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9101300 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9101300 microseconds.  Ignoring time.
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
adjust_timeouts2: packet supposedly had rtt of 8271597 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8271597 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8261632 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8261632 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8289056 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8289056 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9025648 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9025648 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9005928 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9005928 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9055874 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9055874 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9015336 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9015336 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9023737 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9023737 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9011464 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9011464 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9001391 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9001391 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8989349 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8989349 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8979265 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8979265 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8971141 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8971141 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8855457 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8855457 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8199026 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8199026 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8212959 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8212959 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8188933 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8188933 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8175181 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8175181 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8020923 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8020923 microseconds.  Ignoring time.
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
adjust_timeouts2: packet supposedly had rtt of 8779647 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8779647 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8767018 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8767018 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9487133 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9487133 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9962459 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9962459 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10056195 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10056195 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10085385 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10085385 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10075886 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10075886 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10067421 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10067421 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10057655 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10057655 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10564417 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 10564417 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9391747 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9391747 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9239136 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9239136 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9229059 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9229059 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9218961 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9218961 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9208876 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 9208876 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8947404 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8947404 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8880957 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8880957 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8870861 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8870861 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8264616 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8264616 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8070354 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8070354 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8060329 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8060329 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8051549 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8051549 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -6932553 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -6932553 microseconds.  Ignoring time.
Nmap scan report for 192.168.196.144
Host is up, received user-set (0.61s latency).
Scanned at 2024-08-21 13:00:02 EDT for 2579s
Not shown: 65504 closed tcp ports (reset)
PORT      STATE    SERVICE    REASON         VERSION
21/tcp    open     ftp        syn-ack ttl 61 vsftpd 3.0.5
22/tcp    open     ssh        syn-ack ttl 61 OpenSSH 8.9p1 Ubuntu 3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 fb:ea:e1:18:2f:1d:7b:5e:75:96:5a:98:df:3d:17:e4 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKsVbkM4POotpYfh0WatqzVPFWbtiDS0sp2YAxr55TtgpEbeVB8j6CCJjqKJvbgTkIvClq52Jd3XzmYJaK07Ue4=
|   256 66:f4:54:42:1f:25:16:d7:f3:eb:f7:44:9f:5a:1a:0b (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDqyf3tokk0DxqCJOiczEEGgFJsXh09VNspar/n7CtRs
80/tcp    open     http       syn-ack ttl 61 Apache httpd 2.4.52 ((Ubuntu))
|_http-title: Home
| http-methods: 
|_  Supported Methods: POST OPTIONS HEAD GET
| http-git: 
|   192.168.196.144:80/.git/
|     Git repository found!
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|     Last commit message: Security Update 
|     Remotes:
|_      https://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@github.com/PWK-Challenge-Lab/dev.git
|_http-server-header: Apache/2.4.52 (Ubuntu)
|_http-generator: Nicepage 4.21.12, nicepage.com
937/tcp   filtered unknown    no-response
5971/tcp  filtered unknown    no-response
6926/tcp  filtered unknown    no-response
7165/tcp  filtered doc-server no-response
9196/tcp  filtered unknown    no-response
10735/tcp filtered unknown    no-response
10780/tcp filtered unknown    no-response
11285/tcp filtered unknown    no-response
12863/tcp filtered unknown    no-response
14656/tcp filtered unknown    no-response
15590/tcp filtered unknown    no-response
18297/tcp filtered unknown    no-response
21206/tcp filtered unknown    no-response
23973/tcp filtered unknown    no-response
34579/tcp filtered unknown    no-response
35352/tcp filtered unknown    no-response
36011/tcp filtered unknown    no-response
38536/tcp filtered unknown    no-response
41049/tcp filtered unknown    no-response
43218/tcp filtered unknown    no-response
48094/tcp filtered unknown    no-response
51320/tcp filtered unknown    no-response
52593/tcp filtered unknown    no-response
55536/tcp filtered unknown    no-response
57746/tcp filtered unknown    no-response
58519/tcp filtered unknown    no-response
61044/tcp filtered unknown    no-response
61861/tcp filtered unknown    no-response
OS fingerprint not ideal because: maxTimingRatio (5.202000e+00) is greater than 1.4
Aggressive OS guesses: Linux 2.6.32 (88%), Linux 2.6.39 (88%), Linux 3.10 - 3.12 (88%), Linux 3.4 (88%), Linux 3.5 (88%), Linux 4.2 (88%), Linux 4.4 (88%), Synology DiskStation Manager 5.1 (88%), Linux 2.6.35 (87%), Linux 3.10 (87%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.94SVN%E=4%D=8/21%OT=21%CT=1%CU=30792%PV=Y%DS=4%DC=T%G=N%TM=66C62725%P=aarch64-unknown-linux-gnu)
SEQ(SP=101%GCD=1%ISR=101%TI=Z%TS=A)
SEQ(SP=107%GCD=1%ISR=10B%TI=Z%TS=A)
SEQ(SP=107%GCD=1%ISR=10B%TI=Z%II=I%TS=A)
SEQ(SP=107%GCD=1%ISR=10B%TI=Z%II=I%TS=B)
OPS(O1=M551ST11NW7%O2=M551ST11NW7%O3=M551NNT11NW7%O4=M551ST11NW7%O5=M551ST11NW7%O6=M551ST11)
WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)
ECN(R=Y%DF=Y%T=40%W=FAF0%O=M551NNSNW7%CC=Y%Q=)
T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=N)
T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
T6(R=N)
T7(R=N)
U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=D320%RUD=G)
IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 18.827 days (since Fri Aug  2 17:52:05 2024)
Network Distance: 4 hops
TCP Sequence Prediction: Difficulty=257 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 1723/tcp)
HOP RTT       ADDRESS
1   902.82 ms 192.168.45.1
2   902.87 ms 192.168.45.254
3   902.92 ms 192.168.251.1
4   936.86 ms 192.168.196.144

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:43:01 2024 -- 1 IP address (1 host up) scanned in 2580.84 seconds

```
