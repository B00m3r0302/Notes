```bash
smbclient -L //10.10.10.192 -N -I 10.10.10.192 2>&1
```

[/home/kali/Notes/Labs/htb/blackfield/scans/tcp445/smbclient.txt](file:///home/kali/Notes/Labs/htb/blackfield/scans/tcp445/smbclient.txt):

```
do_connect: Connection to 10.10.10.192 failed (Error NT_STATUS_IO_TIMEOUT)

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	forensic        Disk      Forensic / Audit share.
	IPC$            IPC       Remote IPC
	NETLOGON        Disk      Logon server share
	profiles$       Disk
	SYSVOL          Disk      Logon server share
Reconnecting with SMB1 for workgroup listing.
Unable to connect with SMB1 -- no workgroup available


```
