- host is htb.local or sizzle.htb.local
- added it to /etc/hosts
- listed smb shares with 
```bash
smbclient -L ////10.10.10.103//
```
- Output
```
        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        CertEnroll      Disk      Active Directory Certificate Services share
        Department Shares Disk      
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share 
        Operations      Disk      
        SYSVOL          Disk      Logon server share 
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.10.10.103 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```
- Need to get permissions for each share 
- nothing on smbmap
- write a loop to test these. First I’ll `grep` on “Disk” to get just the lines with the shares (I don’t mind missing the IPC share here). Then I’ll use `sed` to match on the entire line, selecting the share name, and then replace it with the share group selection
```bash
smbclient -N -L \\\\10.10.10.103 | grep Disk | sed 's/^\s*\(.*\)\s*Disk.*/\1/'
```
- Output
```
ADMIN$          
C$              
CertEnroll      
Department Shares 
NETLOGON        
Operations      
SYSVOL 
```
- Now, it’s just a manner of looping over those shares, trying to connect, and seeing if i can do a `dir`
```bash
smbclient -N -L \\\\10.10.10.103 | grep Disk | sed 's/^\s*\(.*\)\s*Disk.*/\1/' | while read share; do echo "======${share}======"; smbclient -N "//10.10.10.103/${share}" -c dir; echo; done
```
- Output
```
======ADMIN$======
tree connect failed: NT_STATUS_ACCESS_DENIED

======C$======
tree connect failed: NT_STATUS_ACCESS_DENIED

======CertEnroll======
NT_STATUS_ACCESS_DENIED listing \*

======Department Shares======
  .                                   D        0  Tue Jul  3 11:22:32 2018
  ..                                  D        0  Tue Jul  3 11:22:32 2018
  Accounting                          D        0  Mon Jul  2 15:21:43 2018
  Audit                               D        0  Mon Jul  2 15:14:28 2018
  Banking                             D        0  Tue Jul  3 11:22:39 2018
  CEO_protected                       D        0  Mon Jul  2 15:15:01 2018
  Devops                              D        0  Mon Jul  2 15:19:33 2018
  Finance                             D        0  Mon Jul  2 15:11:57 2018
  HR                                  D        0  Mon Jul  2 15:16:11 2018
  Infosec                             D        0  Mon Jul  2 15:14:24 2018
  Infrastructure                      D        0  Mon Jul  2 15:13:59 2018
  IT                                  D        0  Mon Jul  2 15:12:04 2018
  Legal                               D        0  Mon Jul  2 15:12:09 2018
  M&A                                 D        0  Mon Jul  2 15:15:25 2018
  Marketing                           D        0  Mon Jul  2 15:14:43 2018
  R&D                                 D        0  Mon Jul  2 15:11:47 2018
  Sales                               D        0  Mon Jul  2 15:14:37 2018
  Security                            D        0  Mon Jul  2 15:21:47 2018
  Tax                                 D        0  Mon Jul  2 15:16:54 2018
  Users                               D        0  Tue Jul 10 17:39:32 2018
  ZZ_ARCHIVE                          D        0  Mon Jul  2 15:32:58 2018

                7779839 blocks of size 4096. 3517292 blocks available

======NETLOGON======
NT_STATUS_ACCESS_DENIED listing \*

======Operations======
NT_STATUS_ACCESS_DENIED listing \*

======SYSVOL======
NT_STATUS_ACCESS_DENIED listing \*
```
- Going to go after department shares
- Got in
```bash
smbclient -N "//10.10.10.103/Department Shares"
```
- Output
```
  .                                   D        0  Tue Jul  3 11:22:32 2018
  ..                                  D        0  Tue Jul  3 11:22:32 2018
  Accounting                          D        0  Mon Jul  2 15:21:43 2018
  Audit                               D        0  Mon Jul  2 15:14:28 2018
  Banking                             D        0  Tue Jul  3 11:22:39 2018
  CEO_protected                       D        0  Mon Jul  2 15:15:01 2018
  Devops                              D        0  Mon Jul  2 15:19:33 2018
  Finance                             D        0  Mon Jul  2 15:11:57 2018
  HR                                  D        0  Mon Jul  2 15:16:11 2018
  Infosec                             D        0  Mon Jul  2 15:14:24 2018
  Infrastructure                      D        0  Mon Jul  2 15:13:59 2018
  IT                                  D        0  Mon Jul  2 15:12:04 2018
  Legal                               D        0  Mon Jul  2 15:12:09 2018
  M&A                                 D        0  Mon Jul  2 15:15:25 2018
  Marketing                           D        0  Mon Jul  2 15:14:43 2018
  R&D                                 D        0  Mon Jul  2 15:11:47 2018
  Sales                               D        0  Mon Jul  2 15:14:37 2018
  Security                            D        0  Mon Jul  2 15:21:47 2018
  Tax                                 D        0  Mon Jul  2 15:16:54 2018
  Users                               D        0  Tue Jul 10 17:39:32 2018
  ZZ_ARCHIVE                          D        0  Mon Jul  2 15:32:58 2018

                7779839 blocks of size 4096. 3515908 blocks available
```
- Files in 
	- Banking
		- empty
	- HR
		- empty
	- Tax
		- empty
	- users
		- empty
	- ZZ_ARCHIVE
		- a bunch of crap
- Going to try to mount and manipulate it
```bash
mount -t cifs "//10.10.10.103/Department Shares" /mnt/tmp
```
- Check for writeabiliity anywhere with 
```bash
find . -type d | while read directory; do touch ${directory}/kali 2>/dev/null && echo "${directory} - write file" && rm ${directory}/kali; mkdir ${directory}/kali 2>/dev/null && echo "${directory} - write directory" && rmdir ${directory}/kali; done
```

