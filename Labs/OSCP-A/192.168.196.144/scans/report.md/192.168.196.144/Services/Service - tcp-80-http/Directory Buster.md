```bash
feroxbuster -u http://192.168.196.144:80/ -t 10 -w /root/.local/share/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -r -o "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt):

```
Configuration {
    kind: "configuration",
    wordlist: "/root/.local/share/AutoRecon/wordlists/dirbuster.txt",
    config: "/etc/feroxbuster/ferox-config.toml",
    proxy: "",
    replay_proxy: "",
    server_certs: [],
    client_cert: "",
    client_key: "",
    target_url: "http://192.168.196.144:80/",
    status_codes: [
        100,
        101,
        102,
        200,
        201,
        202,
        203,
        204,
        205,
        206,
        207,
        208,
        226,
        300,
        301,
        302,
        303,
        304,
        305,
        307,
        308,
        400,
        401,
        402,
        403,
        404,
        405,
        406,
        407,
        408,
        409,
        410,
        411,
        412,
        413,
        414,
        415,
        416,
        417,
        418,
        421,
        422,
        423,
        424,
        426,
        428,
        429,
        431,
        451,
        500,
        501,
        502,
        503,
        504,
        505,
        506,
        507,
        508,
        510,
        511,
        103,
        425,
    ],
    replay_codes: [
        100,
        101,
        102,
        200,
        201,
        202,
        203,
        204,
        205,
        206,
        207,
        208,
        226,
        300,
        301,
        302,
        303,
        304,
        305,
        307,
        308,
        400,
        401,
        402,
        403,
        404,
        405,
        406,
        407,
        408,
        409,
        410,
        411,
        412,
        413,
        414,
        415,
        416,
        417,
        418,
        421,
        422,
        423,
        424,
        426,
        428,
        429,
        431,
        451,
        500,
        501,
        502,
        503,
        504,
        505,
        506,
        507,
        508,
        510,
        511,
        103,
        425,
    ],
    filter_status: [],
    client: Client {
        accepts: Accepts,
        proxies: [
            Proxy(
                System(
                    {},
                ),
                None,
            ),
        ],
        referer: true,
        default_headers: {
            "accept": "*/*",
            "user-agent": "feroxbuster/2.10.4",
        },
        timeout: 7s,
    },
    replay_client: None,
    threads: 10,
    timeout: 7,
    verbosity: 1,
    silent: false,
    quiet: true,
    output_level: Quiet,
    auto_bail: false,
    auto_tune: false,
    requester_policy: Default,
    json: false,
    output: "/home/kali/Notes/Labs/OSCP-A/192.168.196.144/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt",
    debug_log: "",
    user_agent: "feroxbuster/2.10.4",
    random_agent: false,
    redirects: true,
    insecure: true,
    extensions: [
        "txt",
        "html",
        "php",
        "asp",
        "aspx",
        "jsp",
    ],
    methods: [
        "GET",
    ],
    data: [],
    headers: {},
    queries: [],
    no_recursion: true,
    extract_links: true,
    add_slash: false,
    stdin: false,
    depth: 4,
    scan_limit: 0,
    parallel: 0,
    rate_limit: 0,
    filter_size: [],
    filter_line_count: [],
    filter_word_count: [],
    filter_regex: [],
    dont_filter: false,
    resumed: false,
    resume_from: "",
    save_state: true,
    time_limit: "",
    filter_similar: [],
    url_denylist: [],
    regex_denylist: [],
    collect_extensions: false,
    dont_collect: [
        "tif",
        "tiff",
        "ico",
        "cur",
        "bmp",
        "webp",
        "svg",
        "png",
        "jpg",
        "jpeg",
        "jfif",
        "gif",
        "avif",
        "apng",
        "pjpeg",
        "pjp",
        "mov",
        "wav",
        "mpg",
        "mpeg",
        "mp3",
        "mp4",
        "m4a",
        "m4p",
        "m4v",
        "ogg",
        "webm",
        "ogv",
        "oga",
        "flac",
        "aac",
        "3gp",
        "css",
        "zip",
        "xls",
        "xml",
        "gz",
        "tgz",
    ],
    collect_backups: false,
    backup_extensions: [
        "~",
        ".bak",
        ".bak2",
        ".old",
        ".1",
    ],
    collect_words: false,
    force_recursion: false,
    update_app: false,
}
200      GET     2561l     4882w    50917c http://192.168.196.144/Home.css
200      GET       25l      103w     5553c http://192.168.196.144/images/561127-62cb0522.png
200      GET       22l       95w     5501c http://192.168.196.144/images/2282272-a53296b6.png
200      GET       22l      112w     7717c http://192.168.196.144/images/323275.png
200      GET       11l       29w      306c http://192.168.196.144/.git/config
200      GET        1l       10w       73c http://192.168.196.144/.git/description
200      GET        2l        8w      112c http://192.168.196.144/.git/packed-refs
200      GET      193l      209w    24941c http://192.168.196.144/images/color-logo-2_150.png
200      GET       22l      130w    10327c http://192.168.196.144/images/159832-67406b0e.png
200      GET        6l       31w     1064c http://192.168.196.144/.git/index
200      GET      188l      197w    23434c http://192.168.196.144/images/color-logo-5_150.png
200      GET      191l      206w    25027c http://192.168.196.144/images/color-logo-4_150.png
200      GET       25l      115w    10396c http://192.168.196.144/images/197507.png
200      GET       25l      108w     7890c http://192.168.196.144/images/197430.png
200      GET        2l        4w       22c http://192.168.196.144/.git/robots.txt
200      GET      194l      214w    26434c http://192.168.196.144/images/color-logo-1_150.png
200      GET      195l      207w    26075c http://192.168.196.144/images/color-logo-3_150.png
200      GET        1l        2w       21c http://192.168.196.144/.git/HEAD
200      GET        1l        2w       16c http://192.168.196.144/.git/COMMIT_EDITMSG
200      GET        2l        5w       25c http://192.168.196.144/.git/README.md
200      GET       41l      187w    12658c http://192.168.196.144/images/953831-b84098f9.png
200      GET       29l      191w    12540c http://192.168.196.144/images/171561-778b2060.png
200      GET       18l      114w    10037c http://192.168.196.144/images/4628635.png
200      GET       28l      241w    17032c http://192.168.196.144/images/3720937-98b53606.png
200      GET       32l      239w     4068c http://192.168.196.144/.git/
200      GET       29l      150w    10555c http://192.168.196.144/images/115968-2e2f0d19.png
200      GET      386l     2264w   199215c http://192.168.196.144/images/dsddd.jpg
200      GET      404l     3541w   258077c http://192.168.196.144/images/595119f1-6ce3-edb5-2421-cc21a4b24655.jpg
200      GET       25l      151w    12811c http://192.168.196.144/images/535239-7ec8b6a6.png
200      GET      490l     2529w    46103c http://192.168.196.144/Home.html
200      GET        2l       18w      335c http://192.168.196.144/.git/logs/HEAD
200      GET       17l       71w     1134c http://192.168.196.144/.git/logs/
200      GET        2l     1297w    89476c http://192.168.196.144/jquery.js
200      GET       42l     4194w   246601c http://192.168.196.144/nicepage.js
200      GET        0l        0w  1299887c http://192.168.196.144/nicepage.css
200      GET      490l     2529w    46103c http://192.168.196.144/
200      GET       61l      235w     2209c http://192.168.196.144/cms/includes/app.php
200      GET       38l     1475w    21131c http://192.168.196.144/cms/templates/system/incompatible.html
200      GET       32l      138w     1068c http://192.168.196.144/cms/
200      GET       18l      119w     8505c http://192.168.196.144/images/535239.png
200      GET       12l       63w     5135c http://192.168.196.144/images/115968.png
200      GET        9l       57w     3839c http://192.168.196.144/images/2282272.png
200      GET       11l       76w     5403c http://192.168.196.144/images/171561.png
200      GET       27l       76w     4932c http://192.168.196.144/images/159832.png
200      GET       23l      138w     9173c http://192.168.196.144/images/3720937.png
200      GET       22l      119w     7924c http://192.168.196.144/images/953831.png
200      GET        8l       70w     4023c http://192.168.196.144/images/561127.png
200      GET      606l     3551w   287098c http://192.168.196.144/images/ddd.jpg
200      GET       43l      306w     6650c http://192.168.196.144/images/
200      GET      490l     2529w    46103c http://192.168.196.144/index.html

```
