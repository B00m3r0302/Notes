```bash
nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/xml/_top_100_udp_nmap.xml" 192.168.196.141
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/_top_100_udp_nmap.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/_top_100_udp_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Aug 21 13:00:01 2024 as: nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN /home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/_top_100_udp_nmap.txt -oX /home/kali/Notes/Labs/OSCP-A/192.168.196.141/scans/xml/_top_100_udp_nmap.xml 192.168.196.141
Warning: 192.168.196.141 giving up on port because retransmission cap hit (6).
Increasing send delay for 192.168.196.141 from 100 to 200 due to 11 out of 12 dropped probes since last increase.
Increasing send delay for 192.168.196.141 from 200 to 400 due to 11 out of 11 dropped probes since last increase.
Increasing send delay for 192.168.196.141 from 400 to 800 due to 11 out of 12 dropped probes since last increase.
Increasing send delay for 192.168.196.141 from 800 to 1000 due to 11 out of 13 dropped probes since last increase.
Nmap scan report for 192.168.196.141
Host is up, received user-set (0.18s latency).
Scanned at 2024-08-21 13:00:02 EDT for 486s

PORT      STATE         SERVICE         REASON               VERSION
7/udp     closed        echo            port-unreach ttl 125
9/udp     closed        discard         port-unreach ttl 125
17/udp    closed        qotd            port-unreach ttl 125
19/udp    closed        chargen         port-unreach ttl 125
49/udp    closed        tacacs          port-unreach ttl 125
53/udp    closed        domain          port-unreach ttl 125
67/udp    closed        dhcps           port-unreach ttl 125
68/udp    closed        dhcpc           port-unreach ttl 125
69/udp    closed        tftp            port-unreach ttl 125
80/udp    open|filtered http            no-response
88/udp    closed        kerberos-sec    port-unreach ttl 125
111/udp   closed        rpcbind         port-unreach ttl 125
120/udp   closed        cfdptkt         port-unreach ttl 125
123/udp   open|filtered ntp             no-response
135/udp   closed        msrpc           port-unreach ttl 125
136/udp   closed        profile         port-unreach ttl 125
137/udp   open|filtered netbios-ns      no-response
138/udp   open|filtered netbios-dgm     no-response
139/udp   closed        netbios-ssn     port-unreach ttl 125
158/udp   closed        pcmail-srv      port-unreach ttl 125
161/udp   closed        snmp            port-unreach ttl 125
162/udp   open|filtered snmptrap        no-response
177/udp   closed        xdmcp           port-unreach ttl 125
427/udp   open|filtered svrloc          no-response
443/udp   closed        https           port-unreach ttl 125
445/udp   open|filtered microsoft-ds    no-response
497/udp   open|filtered retrospect      no-response
500/udp   open|filtered isakmp          no-response
514/udp   open|filtered syslog          no-response
515/udp   closed        printer         port-unreach ttl 125
518/udp   closed        ntalk           port-unreach ttl 125
520/udp   closed        route           port-unreach ttl 125
593/udp   closed        http-rpc-epmap  port-unreach ttl 125
623/udp   closed        asf-rmcp        port-unreach ttl 125
626/udp   closed        serialnumberd   port-unreach ttl 125
631/udp   open|filtered ipp             no-response
996/udp   closed        vsinet          port-unreach ttl 125
997/udp   closed        maitrd          port-unreach ttl 125
998/udp   open|filtered puparp          no-response
999/udp   open|filtered applix          no-response
1022/udp  closed        exp2            port-unreach ttl 125
1023/udp  closed        unknown         port-unreach ttl 125
1025/udp  closed        blackjack       port-unreach ttl 125
1026/udp  closed        win-rpc         port-unreach ttl 125
1027/udp  closed        unknown         port-unreach ttl 125
1028/udp  open|filtered ms-lsa          no-response
1029/udp  closed        solid-mux       port-unreach ttl 125
1030/udp  open|filtered iad1            no-response
1433/udp  closed        ms-sql-s        port-unreach ttl 125
1434/udp  closed        ms-sql-m        port-unreach ttl 125
1645/udp  closed        radius          port-unreach ttl 125
1646/udp  closed        radacct         port-unreach ttl 125
1701/udp  open|filtered L2TP            no-response
1718/udp  open|filtered h225gatedisc    no-response
1719/udp  open|filtered h323gatestat    no-response
1812/udp  closed        radius          port-unreach ttl 125
1813/udp  closed        radacct         port-unreach ttl 125
1900/udp  open|filtered upnp            no-response
2000/udp  open|filtered cisco-sccp      no-response
2048/udp  open|filtered dls-monitor     no-response
2049/udp  closed        nfs             port-unreach ttl 125
2222/udp  closed        msantipiracy    port-unreach ttl 125
2223/udp  closed        rockwell-csp2   port-unreach ttl 125
3283/udp  open|filtered netassistant    no-response
3456/udp  closed        IISrpc-or-vat   port-unreach ttl 125
3703/udp  closed        adobeserver-3   port-unreach ttl 125
4444/udp  closed        krb524          port-unreach ttl 125
4500/udp  open|filtered nat-t-ike       no-response
5000/udp  closed        upnp            port-unreach ttl 125
5060/udp  closed        sip             port-unreach ttl 125
5353/udp  open|filtered zeroconf        no-response
5632/udp  closed        pcanywherestat  port-unreach ttl 125
9200/udp  open|filtered wap-wsp         no-response
10000/udp closed        ndmp            port-unreach ttl 125
17185/udp closed        wdbrpc          port-unreach ttl 125
20031/udp closed        bakbonenetvault port-unreach ttl 125
30718/udp open|filtered unknown         no-response
31337/udp closed        BackOrifice     port-unreach ttl 125
32768/udp closed        omad            port-unreach ttl 125
32769/udp closed        filenet-rpc     port-unreach ttl 125
32771/udp closed        sometimes-rpc6  port-unreach ttl 125
32815/udp closed        unknown         port-unreach ttl 125
33281/udp closed        unknown         port-unreach ttl 125
49152/udp closed        unknown         port-unreach ttl 125
49153/udp closed        unknown         port-unreach ttl 125
49154/udp open|filtered unknown         no-response
49156/udp closed        unknown         port-unreach ttl 125
49181/udp closed        unknown         port-unreach ttl 125
49182/udp closed        unknown         port-unreach ttl 125
49185/udp open|filtered unknown         no-response
49186/udp closed        unknown         port-unreach ttl 125
49188/udp closed        unknown         port-unreach ttl 125
49190/udp closed        unknown         port-unreach ttl 125
49191/udp closed        unknown         port-unreach ttl 125
49192/udp closed        unknown         port-unreach ttl 125
49193/udp closed        unknown         port-unreach ttl 125
49194/udp closed        unknown         port-unreach ttl 125
49200/udp closed        unknown         port-unreach ttl 125
49201/udp closed        unknown         port-unreach ttl 125
65024/udp closed        unknown         port-unreach ttl 125
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing an open TCP port so results incomplete
Aggressive OS guesses: Linux 2.6.18 (91%), Linux 2.6.30 (91%), Microsoft Windows Server 2008 R2 (89%), Microsoft Windows Server 2008 R2 SP1 (89%), Microsoft Windows Server 2008 SP2 Datacenter Version (89%), Microsoft Windows Server 2012 Data Center (89%), Microsoft Windows Server 2012 R2 (89%), Microsoft Windows Server 2016 (89%), Microsoft Windows 7 (89%), Microsoft Windows 7 SP1 (89%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.94SVN%E=4%D=8/21%OT=%CT=%CU=7%PV=Y%DS=4%DC=T%G=N%TM=66C61EF9%P=aarch64-unknown-linux-gnu)
SEQ()
T5(R=Y%DF=Y%T=80%W=0%S=Z%A=O%F=AR%O=%RD=0%Q=)
U1(R=N)
U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=6032%RUD=G)
IE(R=N)

Network Distance: 4 hops

TRACEROUTE (using port 1023/udp)
HOP RTT       ADDRESS
1   674.45 ms 192.168.45.1
2   674.37 ms 192.168.45.254
3   683.41 ms 192.168.251.1
4   683.52 ms 192.168.196.141

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Aug 21 13:08:09 2024 -- 1 IP address (1 host up) scanned in 488.23 seconds

```
