```bash
feroxbuster -u http://192.168.196.145:80/ -t 10 -w /root/.local/share/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -r -o "/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt):

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
    target_url: "http://192.168.196.145:80/",
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
    output: "/home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt",
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
200      GET        8l       29w    28898c http://192.168.196.145/assets/favicon.ico
200      GET      139l      444w    35267c http://192.168.196.145/assets/img/portfolio/safe.png
200      GET       54l      134w     1648c http://192.168.196.145/js/scripts.js
200      GET      195l      683w    66699c http://192.168.196.145/assets/img/portfolio/cabin.png
200      GET      248l      761w    12807c http://192.168.196.145/assets/img/avataaars.svg
200      GET      122l      415w    30702c http://192.168.196.145/assets/img/portfolio/cake.png
200      GET      150l      506w    43607c http://192.168.196.145/assets/img/portfolio/submarine.png
200      GET      151l      616w    50204c http://192.168.196.145/assets/img/portfolio/circus.png
200      GET      178l      601w    46744c http://192.168.196.145/assets/img/portfolio/game.png
200      GET    11073l    20897w   201168c http://192.168.196.145/css/styles.css
200      GET      464l     1868w    30823c http://192.168.196.145/
200      GET      464l     1868w    30823c http://192.168.196.145/Index.html
403      GET       29l       92w     1233c http://192.168.196.145/assets/
403      GET       29l       92w     1233c http://192.168.196.145/css/
200      GET      464l     1868w    30823c http://192.168.196.145/index.html
403      GET       29l       92w     1233c http://192.168.196.145/js/
404      GET        0l        0w     1245c http://192.168.196.145/perl5.aspx
404      GET        0l        0w     1245c http://192.168.196.145/session.asp
404      GET        0l        0w     1245c http://192.168.196.145/sessions.php
404      GET        0l        0w     1245c http://192.168.196.145/_pdfs
404      GET        0l        0w     1245c http://192.168.196.145/adressen.asp
404      GET        0l        0w     1245c http://192.168.196.145/advising.txt
404      GET        0l        0w     1245c http://192.168.196.145/alpha1.php
404      GET        0l        0w     1245c http://192.168.196.145/ark
404      GET        0l        0w     1245c http://192.168.196.145/artistas.php
404      GET        0l        0w     1245c http://192.168.196.145/asterix
404      GET        0l        0w     1245c http://192.168.196.145/asterias
404      GET        0l        0w     1245c http://192.168.196.145/astra
404      GET        0l        0w     1245c http://192.168.196.145/ava.asp
404      GET        0l        0w     1245c http://192.168.196.145/avisos
404      GET        0l        0w     1245c http://192.168.196.145/avn
404      GET        0l        0w     1245c http://192.168.196.145/bounce
404      GET        0l        0w     1245c http://192.168.196.145/botones.html
404      GET        0l        0w     1245c http://192.168.196.145/cox.aspx
404      GET        0l        0w     1245c http://192.168.196.145/emailcollector
404      GET        0l        0w     1245c http://192.168.196.145/emailcpopup
404      GET        0l        0w     1245c http://192.168.196.145/encyclopedia.aspx
404      GET        0l        0w     1245c http://192.168.196.145/event_images
404      GET        0l        0w     1245c http://192.168.196.145/eventcal
404      GET        0l        0w     1245c http://192.168.196.145/eway
404      GET        0l        0w     1245c http://192.168.196.145/eweb
404      GET        0l        0w     1245c http://192.168.196.145/eweb.html
404      GET        0l        0w     1245c http://192.168.196.145/expirados.jsp
404      GET        0l        0w     1245c http://192.168.196.145/gewinnspiel.jsp
404      GET        0l        0w     1245c http://192.168.196.145/instadia.jsp
404      GET        0l        0w     1245c http://192.168.196.145/install_images.html
404      GET        0l        0w     1245c http://192.168.196.145/ivanovo.txt
404      GET        0l        0w     1245c http://192.168.196.145/programsend.html
404      GET        0l        0w     1245c http://192.168.196.145/programmes.aspx
404      GET        0l        0w     1245c http://192.168.196.145/texto.txt
404      GET        0l        0w     1245c http://192.168.196.145/vai.asp
403      GET       29l       92w     1233c http://192.168.196.145/CSS/
403      GET       29l       92w     1233c http://192.168.196.145/JS/
403      GET       29l       92w     1233c http://192.168.196.145/Assets/
403      GET       29l       92w     1233c http://192.168.196.145/Css/
403      GET       29l       92w     1233c http://192.168.196.145/Js/
404      GET        0l        0w     1245c http://192.168.196.145/Tickets.aspx
404      GET        0l        0w     1245c http://192.168.196.145/1155.txt
404      GET        0l        0w     1245c http://192.168.196.145/1186
403      GET       29l       92w     1233c http://192.168.196.145/ASSETS/
404      GET        0l        0w     1245c http://192.168.196.145/dispbbs.aspx
200      GET      464l     1868w    30823c http://192.168.196.145/INDEX.html
404      GET        0l        0w     1245c http://192.168.196.145/paginator.txt
404      GET        0l        0w     1245c http://192.168.196.145/pagini.txt
404      GET        0l        0w     1245c http://192.168.196.145/user_photo.aspx
404      GET        0l        0w     1245c http://192.168.196.145/userpicgallery.php
404      GET        0l        0w     1245c http://192.168.196.145/8530.html
404      GET        0l        0w     1245c http://192.168.196.145/RED.aspx
404      GET        0l        0w     1245c http://192.168.196.145/beretta
404      GET        0l        0w     1245c http://192.168.196.145/common_pages.txt
404      GET        0l        0w     1245c http://192.168.196.145/ninos.txt
404      GET        0l        0w     1245c http://192.168.196.145/DMS-OLD.html
404      GET        0l        0w     1245c http://192.168.196.145/DMG.asp
404      GET        0l        0w     1245c http://192.168.196.145/JEApp
404      GET        0l        0w     1245c http://192.168.196.145/cjtiscaliuk.asp
404      GET        0l        0w     1245c http://192.168.196.145/djc.asp
404      GET        0l        0w     1245c http://192.168.196.145/djusd.txt
404      GET        0l        0w     1245c http://192.168.196.145/dj-ts.aspx
404      GET        0l        0w     1245c http://192.168.196.145/djibouti.php
404      GET        0l        0w     1245c http://192.168.196.145/dj-john-robert.jsp
403      GET       29l       92w     1233c http://192.168.196.145/jS/
404      GET        0l        0w     1245c http://192.168.196.145/optical.asp
404      GET        0l        0w     1245c http://192.168.196.145/optinconfirm
404      GET        0l        0w     1245c http://192.168.196.145/sanjoanlabritja.jsp

```