```bash
smbclient -L //10.10.10.103 -N -I 10.10.10.103 2>&1
```

[/home/kali/Notes/Labs/htb/sizzle/scans/tcp139/smbclient.txt](file:///home/kali/Notes/Labs/htb/sizzle/scans/tcp139/smbclient.txt):

```
do_connect: Connection to 10.10.10.103 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)

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
Unable to connect with SMB1 -- no workgroup available


```
