```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/xml/_quick_tcp_nmap.xml" 192.168.196.144
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/_quick_tcp_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/_quick_tcp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:00:01 2024 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/_quick_tcp_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/xml/_quick_tcp_nmap.xml 192.168.196.144
Increasing send delay for 192.168.196.144 from 0 to 5 due to 257 out of 642 dropped probes since last increase.
Increasing send delay for 192.168.196.144 from 5 to 10 due to 11 out of 23 dropped probes since last increase.
adjust_timeouts2: packet supposedly had rtt of -136056 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -136056 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -160404 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -160404 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -162956 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -162956 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -95449 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -95449 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -120468 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -120468 microseconds.  Ignoring time.
Nmap scan report for 192.168.196.144
Host is up, received user-set (0.095s latency).
Scanned at 2024-08-21 13:00:02 EDT for 42s
Not shown: 997 closed tcp ports (reset)
PORT   STATE SERVICE REASON         VERSION
21/tcp open  ftp     syn-ack ttl 61 vsftpd 3.0.5
22/tcp open  ssh     syn-ack ttl 61 OpenSSH 8.9p1 Ubuntu 3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 fb:ea:e1:18:2f:1d:7b:5e:75:96:5a:98:df:3d:17:e4 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKsVbkM4POotpYfh0WatqzVPFWbtiDS0sp2YAxr55TtgpEbeVB8j6CCJjqKJvbgTkIvClq52Jd3XzmYJaK07Ue4=
|   256 66:f4:54:42:1f:25:16:d7:f3:eb:f7:44:9f:5a:1a:0b (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDqyf3tokk0DxqCJOiczEEGgFJsXh09VNspar/n7CtRs
80/tcp open  http    syn-ack ttl 61 Apache httpd 2.4.52 ((Ubuntu))
|_http-generator: Nicepage 4.21.12, nicepage.com
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
Aggressive OS guesses: Linux 2.6.32 (88%), Linux 2.6.39 (88%), Linux 3.10 - 3.12 (88%), Linux 3.4 (88%), Linux 3.5 (88%), Linux 4.4 (88%), Synology DiskStation Manager 5.1 (88%), WatchGuard Fireware 11.8 (88%), Linux 2.6.35 (87%), Linux 3.10 (87%)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=8/21%OT=21%CT=1%CU=32022%PV=Y%DS=4%DC=T%G=Y%TM=66C6
OS:1D3C%P=aarch64-unknown-linux-gnu)SEQ(SP=106%GCD=1%ISR=10C%TI=Z%TS=A)SEQ(
OS:SP=106%GCD=1%ISR=10C%TI=Z%II=I%TS=A)SEQ(SP=106%GCD=1%ISR=10C%TI=Z%II=I%T
OS:S=C)SEQ(SP=106%GCD=3%ISR=10C%TI=Z%TS=A)OPS(O1=M551ST11NW7%O2=M551ST11NW7
OS:%O3=M551NNT11NW7%O4=M551ST11NW7%O5=M551ST11NW7%O6=M551ST11)WIN(W1=FE88%W
OS:2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)ECN(R=Y%DF=Y%TG=40%W=FAF0%O=M551N
OS:NSNW7%CC=Y%Q=)ECN(R=Y%DF=Y%T=40%W=FAF0%O=M551NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%
OS:TG=40%S=O%A=S+%F=AS%RD=0%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=
OS:N)T3(R=N)T4(R=N)T5(R=Y%DF=Y%TG=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T5(R=Y%DF
OS:=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=N)T7(R=N)U1(R=N)U1(R=Y%DF=N%T=
OS:40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=E621%RUD=G)IE(R=Y%DFI=N%TG=40%
OS:CD=S)IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 18.798 days (since Fri Aug  2 17:52:05 2024)
Network Distance: 4 hops
TCP Sequence Prediction: Difficulty=262 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 1720/tcp)
HOP RTT      ADDRESS
1   91.79 ms 192.168.45.1
2   86.54 ms 192.168.45.254
3   92.13 ms 192.168.251.1
4   84.74 ms 192.168.196.144

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:00:44 2024 -- 1 IP address (1 host up) scanned in 43.26 seconds

```