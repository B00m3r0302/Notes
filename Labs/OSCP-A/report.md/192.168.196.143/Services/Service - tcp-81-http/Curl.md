```bash
curl -sSik http://192.168.196.143:81/
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp81/tcp_81_http_curl.html](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp81/tcp_81_http_curl.html):

```
HTTP/1.1 200 OK
Date: Wed, 21 Aug 2024 17:09:32 GMT
Server: Apache/2.4.41 (Ubuntu)
Last-Modified: Mon, 10 May 2021 22:21:48 GMT
ETag: "e74-5c201341a9efc"
Accept-Ranges: bytes
Content-Length: 3700
Vary: Accept-Encoding
Content-Type: text/html

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
    <head>
        <title>Test Page for the Nginx HTTP Server on Fedora</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <style type="text/css">
            /*<![CDATA[*/
            body {
                background-color: #fff;
                color: #000;
                font-size: 0.9em;
                font-family: sans-serif,helvetica;
                margin: 0;
                padding: 0;
            }
            :link {
                color: #c00;
            }
            :visited {
                color: #c00;
            }
            a:hover {
                color: #f50;
            }
            h1 {
                text-align: center;
                margin: 0;
                padding: 0.6em 2em 0.4em;
                background-color: #294172;
                color: #fff;
                font-weight: normal;
                font-size: 1.75em;
                border-bottom: 2px solid #000;
            }
            h1 strong {
                font-weight: bold;
                font-size: 1.5em;
            }
            h2 {
                text-align: center;
                background-color: #3C6EB4;
                font-size: 1.1em;
                font-weight: bold;
                color: #fff;
                margin: 0;
                padding: 0.5em;
                border-bottom: 2px solid #294172;
            }
            hr {
                display: none;
            }
            .content {
                padding: 1em 5em;
            }
            .alert {
                border: 2px solid #000;
            }

            img {
                border: 2px solid #fff;
                padding: 2px;
                margin: 2px;
            }
            a:hover img {
                border: 2px solid #294172;
            }
            .logos {
                margin: 1em;
                text-align: center;
            }
            /*]]>*/
        </style>
    </head>

    <body>
        <h1>Welcome to <strong>nginx</strong> on Fedora!</h1>

        <div class="content">
            <p>This page is used to test the proper operation of the
            <strong>nginx</strong> HTTP server after it has been
            installed. If you can read this page, it means that the
            web server installed at this site is working
            properly.</p>

            <div class="alert">
                <h2>Website Administrator</h2>
                <div class="content">
                    <p>This is the default <tt>index.html</tt> page that
                    is distributed with <strong>nginx</strong> on
                    Fedora.  It is located in
                    <tt>/usr/share/nginx/html</tt>.</p>

                    <p>You should now put your content in a location of
                    your choice and edit the <tt>root</tt> configuration
                    directive in the <strong>nginx</strong>
                    configuration file
                    <tt>/etc/nginx/nginx.conf</tt>.</p>

                </div>
            </div>

            <div class="logos">
                <a href="http://nginx.net/"><img
                    src="nginx-logo.png"
                    alt="[ Powered by nginx ]"
                    width="121" height="32" /></a>

                <a href="http://fedoraproject.org/"><img
                    src="poweredby.png"
                    alt="[ Powered by Fedora ]"
                    width="88" height="31" /></a>
            </div>
        </div>
    </body>
</html>


```
