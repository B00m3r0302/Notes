- Recommended command for ssh into the lab #ssh 
```
ssh -o "UseKnownHostsFile=/dev/null" -o "StrictHostKeyChecking=no" USER@IP
```
- If a binary doesn't work you can copy the binary of another file to one that is executable by you #privesc 
```
cp /usr/bin/ls chodfix
cat /usr/bin/chmod > chmodfix
# Chmodfix is now executable and can be run like chmod even if you   # can't run chmod at your current privilege level
```
- screenshots you can use the screenshot app or flameshot which has a built in editor #reporting 
	- https://github.com/flameshot-org/flameshot
