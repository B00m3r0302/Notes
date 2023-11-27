### Subsection 8.3.3 Enumerating and abusing APIs
- The following files are useful in finding directories and files 
	- robots.txt
	- sitemap.xml
- Brute-forcing an api with gobuster 
	- Generate a wordlist that looks like the following:
```
{GOBUSTER}/v1
{GOBUSTER}/v2
```

- run your gobuster command with the -p flag followed by the path to the file at the end of the command
- Send command line data like stuff from curl to burpsuite using the following at the end of your command 
```
--proxy IP:PORT
```
## Exercises To-Do

- [ ] 2.1.1 (page 20)