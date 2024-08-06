```bash
enum4linux-ng -A -d -v 192.168.185.141 2>&1
```

[/home/kali/Notes/Labs/A/192.168.185.141/scans/tcp139/enum4linux-ng.txt](file:///home/kali/Notes/Labs/A/192.168.185.141/scans/tcp139/enum4linux-ng.txt):

```
[92mENUM4LINUX - next generation (v1.3.3)[0m

 ==========================
|    Target Information    |
 ==========================
[94m[*] Target ........... 192.168.185.141[0m
[94m[*] Username ......... ''[0m
[94m[*] Random Username .. 'plmlooxh'[0m
[94m[*] Password ......... ''[0m
[94m[*] Timeout .......... 5 second(s)[0m

 ========================================
|    Listener Scan on 192.168.185.141    |
 ========================================
[94m[*] Checking LDAP[0m
[91m[-] Could not connect to LDAP on 389/tcp: connection refused[0m
[94m[*] Checking LDAPS[0m
[91m[-] Could not connect to LDAPS on 636/tcp: connection refused[0m
[94m[*] Checking SMB[0m
[92m[+] SMB is accessible on 445/tcp[0m
[94m[*] Checking SMB over NetBIOS[0m
[92m[+] SMB over NetBIOS is accessible on 139/tcp[0m

 ==============================================================
|    NetBIOS Names and Workgroup/Domain for 192.168.185.141    |
 ==============================================================
[V] Trying to get NetBIOS names information, running command: nmblookup -s /tmp/tmp40y30u8i -A 192.168.185.141
[91m[-] Could not get NetBIOS names information via 'nmblookup': timed out[0m

 ============================================
|    SMB Dialect Check on 192.168.185.141    |
 ============================================
[94m[*] Trying on 445/tcp[0m
[92m[+] Supported dialects and settings:
Supported dialects:
  SMB 1.0: false
  SMB 2.02: true
  SMB 2.1: true
  SMB 3.0: true
  SMB 3.1.1: true
Preferred dialect: SMB 3.0
SMB1 only: false
SMB signing required: false[0m

 ==============================================================
|    Domain Information via SMB session for 192.168.185.141    |
 ==============================================================
[94m[*] Enumerating via unauthenticated SMB session on 445/tcp[0m
[92m[+] Found domain information via SMB
NetBIOS computer name: MS01
NetBIOS domain name: OSCP
DNS domain: oscp.exam
FQDN: MS01.oscp.exam
Derived membership: domain member
Derived domain: OSCP[0m

 ============================================
|    RPC Session Check on 192.168.185.141    |
 ============================================
[94m[*] Check for null session[0m
[V] Attempting to make session, running command: smbclient -W OSCP -U % -s /tmp/tmp40y30u8i -t 5 -c help '//192.168.185.141/ipc$'
[91m[-] Could not establish null session: STATUS_ACCESS_DENIED[0m
[94m[*] Check for random user[0m
[V] Attempting to make session, running command: smbclient -W OSCP -U plmlooxh% -s /tmp/tmp40y30u8i -t 5 -c help '//192.168.185.141/ipc$'
[91m[-] Could not establish random user session: STATUS_LOGON_FAILURE[0m
[91m[-] Sessions failed, neither null nor user sessions were possible[0m

 ==================================================
|    OS Information via RPC for 192.168.185.141    |
 ==================================================
[94m[*] Enumerating via unauthenticated SMB session on 445/tcp[0m
[92m[+] Found OS information via SMB[0m
[94m[*] Enumerating via 'srvinfo'[0m
[91m[-] Skipping 'srvinfo' run, not possible with provided credentials[0m
[92m[+] After merging OS information we have the following result:
OS: Windows 10, Windows Server 2019, Windows Server 2016
OS version: '10.0'
OS release: '2004'
OS build: '19041'
Native OS: not supported
Native LAN manager: not supported
Platform id: null
Server type: null
Server type string: null[0m

[93m[!] Aborting remainder of tests since sessions failed, rerun with valid credentials[0m

Completed after 8.56 seconds


```
