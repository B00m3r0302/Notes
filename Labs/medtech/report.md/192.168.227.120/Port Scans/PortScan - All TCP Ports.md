```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Notes/Labs/medtech/192.168.227.120/scans/_full_tcp_nmap.txt" -oX "/home/kali/Notes/Labs/medtech/192.168.227.120/scans/xml/_full_tcp_nmap.xml" 192.168.227.120
```

[/home/kali/Notes/Labs/medtech/192.168.227.120/scans/_full_tcp_nmap.txt](file:///home/kali/Notes/Labs/medtech/192.168.227.120/scans/_full_tcp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Mon Jul 29 07:55:21 2024 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/kali/Notes/Labs/medtech/192.168.227.120/scans/_full_tcp_nmap.txt -oX /home/kali/Notes/Labs/medtech/192.168.227.120/scans/xml/_full_tcp_nmap.xml 192.168.227.120
Increasing send delay for 192.168.227.120 from 0 to 5 due to 1227 out of 3067 dropped probes since last increase.
Increasing send delay for 192.168.227.120 from 5 to 10 due to 11 out of 14 dropped probes since last increase.
adjust_timeouts2: packet supposedly had rtt of -112189 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -112189 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -108657 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -108657 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -105361 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -105361 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -151718 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -151718 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -260299 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -260299 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -407372 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -407372 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -294987 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -294987 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -288994 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -288994 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -270376 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -270376 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -288614 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -288614 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -296036 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -296036 microseconds.  Ignoring time.
Nmap scan report for 192.168.227.120
Host is up, received user-set (0.18s latency).
Scanned at 2024-07-29 07:55:27 EDT for 910s
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 61 OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 84:72:7e:4c:bb:ff:86:ae:b0:03:00:79:a1:c5:af:34 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDkLNDFG9Ksbp5P6tGeMkTaAWEz2kRFfmnXuClhYdhdUw7F+b/usqfzszEQFdRP3R3vpy3LnLrkDmaMuIAL/lazj55FsrhC3cnbNgNCEzapQNf0ZpAydfT4ypFiSrqLDE0Bq+xZmAT9S8eZ2efR5sfCPw9NB/hMlmW6s91xekPtBbINNhgPy8beAvkyfSlGMWj8kHKqP6onEoo+J5IkOjMcnXh+zLdxoPdo6HnuQ/VMims8qYEaxxJndN1Y46jEMdBtznbUavHrD8NIbviVFUBIfHyUEs5kWp1LK1TMSGBA9ILxGumIJRXdIV3OouR+KLlva+DxJdri9pSZ4g5TVP7iutPogBm8U7h14MfXt+jhT+NC8xRZi/30zQOtHmV+nsKzhbCmveRed3UZvcLE+t5nYuo8+EV1vqaRtvhds188FbDif1AI9ISdytjPaOomUEcRg63jUuc32iokqFLNcYba7339M8Q18HzneLXj7NGo+/avQ4D/zZVXSDki9BT+Hhs=
|   256 f1:31:e5:75:31:36:a2:59:f3:12:1b:58:b4:bb:dc:0f (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBF1H0xp5zQUrhCWusjcxvbE4BrHOhMzFjCtti37V8JXBwBvi6uM7mmuwfkTr5eImaQsg+Py3ZA4rejeFoVgIITE=
|   256 5a:05:9c:fc:2f:7b:7e:0b:81:a6:20:48:5a:1d:82:7e (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILG7AuVkWzcrlnj9+BnFPawjXQbi/iHkE80UL/RPXFUf
80/tcp open  http    syn-ack ttl 61 WEBrick httpd 1.6.1 (Ruby 2.7.4 (2021-07-07))
|_http-server-header: WEBrick/1.6.1 (Ruby/2.7.4/2021-07-07)
|_http-title: PAW! (PWK Awesome Website)
| http-methods: 
|_  Supported Methods: GET HEAD OPTIONS
Aggressive OS guesses: Linux 2.6.32 (88%), Linux 2.6.32 or 3.10 (88%), Linux 2.6.39 (88%), Linux 3.10 - 3.12 (88%), Linux 3.4 (88%), Linux 3.5 (88%), Linux 4.4 (88%), Synology DiskStation Manager 5.1 (88%), WatchGuard Fireware 11.8 (88%), Linux 2.6.35 (87%)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=7/29%OT=22%CT=1%CU=35576%PV=Y%DS=4%DC=T%G=Y%TM=66A7
OS:86BD%P=x86_64-pc-linux-gnu)SEQ(SP=104%GCD=1%ISR=10C%TI=Z%II=I%TS=A)SEQ(S
OS:P=104%GCD=1%ISR=10D%TI=Z%TS=A)SEQ(SP=105%GCD=1%ISR=10E%TI=Z%TS=A)SEQ(SP=
OS:105%GCD=1%ISR=10E%TI=Z%TS=C)SEQ(SP=105%GCD=1%ISR=10E%TI=Z%II=I%TS=C)OPS(
OS:O1=M551ST11NW7%O2=M551ST11NW7%O3=M551NNT11NW7%O4=M551ST11NW7%O5=M551ST11
OS:NW7%O6=M551ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)ECN(
OS:R=Y%DF=Y%T=40%W=FAF0%O=M551NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS
OS:%RD=0%Q=)T2(R=N)T3(R=N)T4(R=N)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0
OS:%Q=)T6(R=N)T7(R=N)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUC
OS:K=8367%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 30.615 days (since Fri Jun 28 17:25:32 2024)
Network Distance: 4 hops
TCP Sequence Prediction: Difficulty=260 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 1723/tcp)
HOP RTT       ADDRESS
1   206.48 ms 192.168.45.1
2   206.47 ms 192.168.45.254
3   270.49 ms 192.168.251.1
4   270.57 ms 192.168.227.120

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jul 29 08:10:37 2024 -- 1 IP address (1 host up) scanned in 916.01 seconds

```
