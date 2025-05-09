```bash
feroxbuster -u http://10.10.11.187:80/ -t 10 -w /home/kali/.local/share/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -r -o "/home/kali/Notes/Labs/htb/flight/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"
```

[/home/kali/Notes/Labs/htb/flight/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt](file:///home/kali/Notes/Labs/htb/flight/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt):

```
Configuration {
    kind: "configuration",
    wordlist: "/home/kali/.local/share/AutoRecon/wordlists/dirbuster.txt",
    config: "/etc/feroxbuster/ferox-config.toml",
    proxy: "",
    replay_proxy: "",
    server_certs: [],
    client_cert: "",
    client_key: "",
    target_url: "http://10.10.11.187:80/",
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
            "user-agent": "feroxbuster/2.11.0",
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
    output: "/home/kali/Notes/Labs/htb/flight/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt",
    debug_log: "",
    user_agent: "feroxbuster/2.11.0",
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
    scan_dir_listings: false,
    request_file: "",
    protocol: "https",
    limit_bars: 0,
}
200      GET        1l        6w      170c http://10.10.11.187/images/img2.gif
200      GET       34l       71w     1381c http://10.10.11.187/js/html5.js
200      GET        4l      174w     2112c http://10.10.11.187/js/ie6_script_other.js
200      GET      402l      656w     7269c http://10.10.11.187/css/style.css
200      GET        7l      347w    18257c http://10.10.11.187/js/cufon-yui.js
200      GET       24l      104w    21971c http://10.10.11.187/js/Myriad_Pro_italic_400.font.js
200      GET        4l       33w      293c http://10.10.11.187/js/cufon-replace.js
200      GET      154l      530w     7069c http://10.10.11.187/index.html
200      GET       30l      123w      887c http://10.10.11.187/css/reset.css
200      GET        2l        7w      109c http://10.10.11.187/images/img3.gif
200      GET        1l        7w      194c http://10.10.11.187/images/img1.gif
200      GET       40l       69w      535c http://10.10.11.187/css/layout.css
200      GET      154l     1206w    72326c http://10.10.11.187/js/jquery-1.4.2.js
200      GET       23l       87w    77620c http://10.10.11.187/js/Myriad_Pro_400.font.js
200      GET       24l      104w    35323c http://10.10.11.187/js/Myriad_Pro_italic_600.font.js
200      GET      154l      530w     7069c http://10.10.11.187/
200      GET       36l      227w    19188c http://10.10.11.187/Images/page4_img2.jpg
200      GET        1l        7w      194c http://10.10.11.187/Images/img1.gif
200      GET      154l      530w     7069c http://10.10.11.187/Index.html
200      GET      227l     1260w    96501c http://10.10.11.187/Images/bg_img2.jpg
200      GET        1l        6w      170c http://10.10.11.187/Images/img2.gif
200      GET        1l        3w      181c http://10.10.11.187/Images/button1_bg.gif
200      GET        1l        4w       75c http://10.10.11.187/Images/line_top.gif
200      GET       45l      299w    28174c http://10.10.11.187/Images/page3_img1.jpg
200      GET        7l       23w     2618c http://10.10.11.187/Images/bg_testimonials.gif
200      GET       71l      284w    21166c http://10.10.11.187/Images/bg_top.jpg
200      GET       35l      181w    13683c http://10.10.11.187/Images/logo.jpg
200      GET        2l        7w      109c http://10.10.11.187/Images/img3.gif
200      GET       80l      453w    35976c http://10.10.11.187/Images/page2_img1.jpg
200      GET        8l       49w     3042c http://10.10.11.187/Images/button_top_active.jpg
200      GET       36l      295w    26685c http://10.10.11.187/Images/page4_img1.jpg
200      GET       42l      202w    15855c http://10.10.11.187/Images/page2_img2.jpg
200      GET       36l      295w    26685c http://10.10.11.187/Images/page3_img2.jpg
200      GET       43l      236w    13634c http://10.10.11.187/Images/bg_bot.jpg
200      GET      706l     4305w   291438c http://10.10.11.187/Images/bg_img.jpg
200      GET        1l        2w      177c http://10.10.11.187/Images/marker_1.gif
200      GET        5l       57w     3124c http://10.10.11.187/Images/button_top.jpg
200      GET        1l        5w      698c http://10.10.11.187/Images/bg_box1.jpg
200      GET        2l        5w      281c http://10.10.11.187/Images/button2_bg.gif
200      GET       37l      289w     5512c http://10.10.11.187/Images/
200      GET       18l       84w     1397c http://10.10.11.187/css/
503      GET       11l       44w      401c http://10.10.11.187/examples
200      GET       36l      227w    19188c http://10.10.11.187/images/page4_img2.jpg
200      GET       43l      236w    13634c http://10.10.11.187/images/bg_bot.jpg
200      GET        1l        2w      177c http://10.10.11.187/images/marker_1.gif
200      GET       71l      284w    21166c http://10.10.11.187/images/bg_top.jpg
200      GET        2l        5w      281c http://10.10.11.187/images/button2_bg.gif
200      GET        5l       57w     3124c http://10.10.11.187/images/button_top.jpg
200      GET        1l        4w       75c http://10.10.11.187/images/line_top.gif
200      GET       80l      453w    35976c http://10.10.11.187/images/page2_img1.jpg
200      GET      227l     1260w    96501c http://10.10.11.187/images/bg_img2.jpg
200      GET        7l       23w     2618c http://10.10.11.187/images/bg_testimonials.gif
200      GET        1l        3w      181c http://10.10.11.187/images/button1_bg.gif
200      GET        8l       49w     3042c http://10.10.11.187/images/button_top_active.jpg
200      GET       42l      202w    15855c http://10.10.11.187/images/page2_img2.jpg
200      GET       36l      295w    26685c http://10.10.11.187/images/page4_img1.jpg
200      GET       35l      181w    13683c http://10.10.11.187/images/logo.jpg
200      GET       36l      295w    26685c http://10.10.11.187/images/page3_img2.jpg
200      GET        1l        5w      698c http://10.10.11.187/images/bg_box1.jpg
200      GET       45l      299w    28174c http://10.10.11.187/images/page3_img1.jpg
200      GET      706l     4305w   291438c http://10.10.11.187/images/bg_img.jpg
200      GET       37l      289w     5512c http://10.10.11.187/images/
200      GET       77l      518w    28280c http://10.10.11.187/js/PIE.htc
200      GET       25l      168w     2978c http://10.10.11.187/js/
403      GET       11l       47w      420c http://10.10.11.187/licenses
403      GET       11l       47w      420c http://10.10.11.187/phpmyadmin
403      GET       11l       47w      420c http://10.10.11.187/server-info
403      GET       11l       47w      420c http://10.10.11.187/server-status
403      GET       11l       47w      420c http://10.10.11.187/webalizer
200      GET      402l      656w     7269c http://10.10.11.187/CSS/style.css
200      GET       30l      123w      887c http://10.10.11.187/CSS/reset.css
200      GET       40l       69w      535c http://10.10.11.187/CSS/layout.css
200      GET       18l       84w     1397c http://10.10.11.187/CSS/
200      GET        4l       33w      293c http://10.10.11.187/JS/cufon-replace.js
200      GET        4l      174w     2112c http://10.10.11.187/JS/ie6_script_other.js
200      GET       24l      104w    35323c http://10.10.11.187/JS/Myriad_Pro_italic_600.font.js
200      GET       34l       71w     1381c http://10.10.11.187/JS/html5.js
200      GET        7l      347w    18257c http://10.10.11.187/JS/cufon-yui.js
200      GET       24l      104w    21971c http://10.10.11.187/JS/Myriad_Pro_italic_400.font.js
200      GET      154l     1206w    72326c http://10.10.11.187/JS/jquery-1.4.2.js
200      GET       77l      518w    28280c http://10.10.11.187/JS/PIE.htc
200      GET       23l       87w    77620c http://10.10.11.187/JS/Myriad_Pro_400.font.js
200      GET       25l      168w     2978c http://10.10.11.187/JS/
200      GET       30l      123w      887c http://10.10.11.187/Css/reset.css
200      GET      402l      656w     7269c http://10.10.11.187/Css/style.css
200      GET       40l       69w      535c http://10.10.11.187/Css/layout.css
200      GET       18l       84w     1397c http://10.10.11.187/Css/
200      GET        4l      174w     2112c http://10.10.11.187/Js/ie6_script_other.js
200      GET        4l       33w      293c http://10.10.11.187/Js/cufon-replace.js
200      GET       34l       71w     1381c http://10.10.11.187/Js/html5.js
200      GET       77l      518w    28280c http://10.10.11.187/Js/PIE.htc
200      GET        7l      347w    18257c http://10.10.11.187/Js/cufon-yui.js
200      GET       24l      104w    35323c http://10.10.11.187/Js/Myriad_Pro_italic_600.font.js
200      GET       24l      104w    21971c http://10.10.11.187/Js/Myriad_Pro_italic_400.font.js
200      GET       23l       87w    77620c http://10.10.11.187/Js/Myriad_Pro_400.font.js
200      GET      154l     1206w    72326c http://10.10.11.187/Js/jquery-1.4.2.js
200      GET       25l      168w     2978c http://10.10.11.187/Js/
200      GET        2l        5w      281c http://10.10.11.187/IMAGES/button2_bg.gif
200      GET        1l        4w       75c http://10.10.11.187/IMAGES/line_top.gif
200      GET        1l        7w      194c http://10.10.11.187/IMAGES/img1.gif
200      GET        1l        6w      170c http://10.10.11.187/IMAGES/img2.gif
200      GET        2l        7w      109c http://10.10.11.187/IMAGES/img3.gif
200      GET        1l        2w      177c http://10.10.11.187/IMAGES/marker_1.gif
200      GET       36l      295w    26685c http://10.10.11.187/IMAGES/page3_img2.jpg
200      GET      227l     1260w    96501c http://10.10.11.187/IMAGES/bg_img2.jpg
200      GET        1l        5w      698c http://10.10.11.187/IMAGES/bg_box1.jpg
200      GET       36l      295w    26685c http://10.10.11.187/IMAGES/page4_img1.jpg
200      GET        1l        3w      181c http://10.10.11.187/IMAGES/button1_bg.gif
200      GET        5l       57w     3124c http://10.10.11.187/IMAGES/button_top.jpg
200      GET        8l       49w     3042c http://10.10.11.187/IMAGES/button_top_active.jpg
200      GET       42l      202w    15855c http://10.10.11.187/IMAGES/page2_img2.jpg
200      GET        7l       23w     2618c http://10.10.11.187/IMAGES/bg_testimonials.gif
200      GET       36l      227w    19188c http://10.10.11.187/IMAGES/page4_img2.jpg
200      GET       35l      181w    13683c http://10.10.11.187/IMAGES/logo.jpg
200      GET       71l      284w    21166c http://10.10.11.187/IMAGES/bg_top.jpg
200      GET       45l      299w    28174c http://10.10.11.187/IMAGES/page3_img1.jpg
200      GET       43l      236w    13634c http://10.10.11.187/IMAGES/bg_bot.jpg
200      GET       80l      453w    35976c http://10.10.11.187/IMAGES/page2_img1.jpg
200      GET      706l     4305w   291438c http://10.10.11.187/IMAGES/bg_img.jpg
200      GET       37l      289w     5512c http://10.10.11.187/IMAGES/
200      GET      154l      530w     7069c http://10.10.11.187/INDEX.html
200      GET        4l       33w      293c http://10.10.11.187/jS/cufon-replace.js
200      GET       34l       71w     1381c http://10.10.11.187/jS/html5.js
200      GET       24l      104w    21971c http://10.10.11.187/jS/Myriad_Pro_italic_400.font.js
200      GET        4l      174w     2112c http://10.10.11.187/jS/ie6_script_other.js
200      GET       24l      104w    35323c http://10.10.11.187/jS/Myriad_Pro_italic_600.font.js
200      GET       23l       87w    77620c http://10.10.11.187/jS/Myriad_Pro_400.font.js
200      GET      154l     1206w    72326c http://10.10.11.187/jS/jquery-1.4.2.js
200      GET        7l      347w    18257c http://10.10.11.187/jS/cufon-yui.js
200      GET       77l      518w    28280c http://10.10.11.187/jS/PIE.htc
200      GET       25l      168w     2978c http://10.10.11.187/jS/

```
