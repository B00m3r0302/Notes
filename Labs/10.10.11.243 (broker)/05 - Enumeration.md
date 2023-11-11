.hackthebox.com
# Andy Enumeration

## nmap

I ran the following command:

```bash
$ autorecon --single-target -v -o brok 10.10.11.243
```

Key Findings:
- ssh on port 22
- web server on port 80
- mqtt on port 1883
- amqp on port 5672
- http server on 8161
- tcpwrapped on 44741
- stomp on 61613
- http on 61614
- apachemq on 61616

### Web server enumeration (80)
- upon visiting the website it asks for a login and i was able to login with

|Username|Password|
|:---:|:---:|
|admin|admin|









