```bash
feroxbuster -u http://192.168.227.121:80/ -t 10 -w /root/.local/share/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -r -o "/home/kali/Notes/Labs/medtech/192.168.227.121/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"
```

[/home/kali/Notes/Labs/medtech/192.168.227.121/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt](file:///home/kali/Notes/Labs/medtech/192.168.227.121/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt):

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
    target_url: "http://192.168.227.121:80/",
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
    output: "/home/kali/Notes/Labs/medtech/192.168.227.121/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt",
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
200      GET       33l       73w      988c http://192.168.227.121/assets/css/flaticon.css
200      GET       11l       40w     2570c http://192.168.227.121/assets/img/logo/loder.png
200      GET        6l       64w     2936c http://192.168.227.121/assets/css/owl.carousel.min.css
200      GET      215l      419w     5390c http://192.168.227.121/assets/js/main.js
200      GET      120l      339w     4820c http://192.168.227.121/assets/js/jquery.ajaxchimp.min.js
200      GET      288l      914w    10085c http://192.168.227.121/assets/js/jquery.sticky.js
200      GET      262l      614w     5732c http://192.168.227.121/assets/css/slicknav.css
200      GET        5l      351w    19188c http://192.168.227.121/assets/js/popper.min.js
200      GET       85l      206w     3024c http://192.168.227.121/assets/js/contact.js
200      GET       21l      106w     7966c http://192.168.227.121/assets/img/icon/quotes-sign.png
200      GET      100l     2406w    46910c http://192.168.227.121/assets/img/gallery/section_bg01.png
200      GET     1174l     4381w    41095c http://192.168.227.121/assets/js/jquery.form.js
200      GET       63l      359w    25802c http://192.168.227.121/assets/img/icon/testimonial.png
200      GET        8l      165w     8044c http://192.168.227.121/assets/js/waypoints.min.js
200      GET       11l       63w     2849c http://192.168.227.121/assets/img/icon/services3.svg
200      GET       11l      513w    56048c http://192.168.227.121/assets/css/animate.min.css
200      GET       39l      280w     7689c http://192.168.227.121/assets/img/icon/about2.svg
200      GET        4l      212w    20216c http://192.168.227.121/assets/js/jquery.magnific-popup.js
200      GET      138l      371w     4007c http://192.168.227.121/assets/css/nice-select.css
200      GET       92l      353w     8570c http://192.168.227.121/assets/img/icon/services2.svg
200      GET        7l      279w    42766c http://192.168.227.121/assets/js/owl.carousel.min.js
200      GET     1264l     2489w    27021c http://192.168.227.121/assets/css/animated-headline.css
200      GET        1l        6w     2340c http://192.168.227.121/assets/img/favicon.ico
200      GET      360l     2412w   205402c http://192.168.227.121/assets/img/gallery/blog1.png
200      GET        4l       42w     2942c http://192.168.227.121/assets/js/jquery.nice-select.min.js
200      GET        5l     1434w    97163c http://192.168.227.121/assets/js/vendor/jquery-1.12.4.min.js
200      GET     2031l    12635w  1057918c http://192.168.227.121/assets/img/gallery/about2.png
200      GET      648l     4104w   318437c http://192.168.227.121/assets/img/gallery/blog2.png
200      GET        3l      215w     8636c http://192.168.227.121/assets/js/vendor/modernizr-3.5.0.min.js
200      GET        8l       36w     1067c http://192.168.227.121/assets/js/jquery.counterup.min.js
200      GET        6l      102w     8415c http://192.168.227.121/assets/js/jquery.slicknav.min.js
200      GET      386l     1108w    19928c http://192.168.227.121/services.aspx
200      GET      561l     1487w    30752c http://192.168.227.121/blog.aspx
200      GET     3319l    19843w  1558735c http://192.168.227.121/assets/img/gallery/video-bg.png
200      GET     1602l     9849w   805575c http://192.168.227.121/assets/img/gallery/about.png
200      GET      119l      179w     1776c http://192.168.227.121/assets/css/slick.css
200      GET        1l        4w      867c http://192.168.227.121/assets/js/hover-direction-snake.min.js
200      GET      154l      437w     5532c http://192.168.227.121/assets/js/animated.headline.js
200      GET      522l     1550w    25997c http://192.168.227.121/default.aspx
200      GET       22l      253w     5369c http://192.168.227.121/assets/js/jquery.countdown.min.js
200      GET        2l      364w    21068c http://192.168.227.121/assets/js/jquery.validate.min.js
200      GET        7l     1667w   140936c http://192.168.227.121/assets/css/bootstrap.min.css
200      GET     1083l     1807w    16452c http://192.168.227.121/assets/css/themify-icons.css
200      GET        1l     2188w   177487c http://192.168.227.121/assets/js/gijgo.min.js
200      GET       31l      113w     1230c http://192.168.227.121/assets/js/mail-script.js
200      GET       23l      102w     2481c http://192.168.227.121/assets/img/icon/services1.svg
200      GET        2l      132w     8415c http://192.168.227.121/assets/js/wow.min.js
200      GET      457l     1312w    22575c http://192.168.227.121/about.aspx
200      GET      354l     3002w    46706c http://192.168.227.121/contact.aspx
200      GET        1l      248w    42863c http://192.168.227.121/assets/js/slick.min.js
200      GET        7l      567w    48944c http://192.168.227.121/assets/js/bootstrap.min.js
200      GET      351l      795w     6951c http://192.168.227.121/assets/css/magnific-popup.css
200      GET       24l       88w      760c http://192.168.227.121/assets/js/plugins.js
200      GET        5l       82w    34680c http://192.168.227.121/assets/css/fontawesome-all.min.css
200      GET     2698l     5518w    57518c http://192.168.227.121/assets/css/gijgo.css
200      GET       98l      251w     4083c http://192.168.227.121/login.aspx
200      GET       31l     3252w    59665c http://192.168.227.121/assets/img/gallery/footer-bg.png
200      GET        6l       28w     2962c http://192.168.227.121/assets/img/icon/about1.svg
200      GET        1l     2605w    87568c http://192.168.227.121/assets/css/style.css
200      GET      800l     4517w   347072c http://192.168.227.121/assets/img/gallery/blog3.png
200      GET      522l     1550w    25997c http://192.168.227.121/
200      GET      430l     2538w   201967c http://192.168.227.121/assets/img/gallery/team2.png
200      GET      487l     2978w   249033c http://192.168.227.121/assets/img/gallery/team1.png
200      GET      437l     2439w   207752c http://192.168.227.121/assets/img/gallery/team3.png
200      GET      457l     1312w    22575c http://192.168.227.121/About.aspx
200      GET       81l      439w    30760c http://192.168.227.121/assets/img/post/post_9.png
200      GET       58l      400w    28663c http://192.168.227.121/assets/img/post/post_1.png
200      GET       90l      481w    34290c http://192.168.227.121/assets/img/post/post_10.png
200      GET       59l      383w    31370c http://192.168.227.121/assets/img/post/post_6.png
200      GET       42l      328w    23739c http://192.168.227.121/assets/img/post/post_2.png
200      GET       32l       67w      449c http://192.168.227.121/assets/css/responsive.css
200      GET       90l      501w    37857c http://192.168.227.121/assets/img/post/post_5.png
200      GET       41l      314w    25656c http://192.168.227.121/assets/img/post/post_3.png
200      GET       84l      451w    37441c http://192.168.227.121/assets/img/post/post_7.png
200      GET       43l      261w    20757c http://192.168.227.121/assets/img/post/post_4.png
200      GET       59l      373w    29182c http://192.168.227.121/assets/img/post/post_8.png
200      GET     1738l    10206w   819368c http://192.168.227.121/assets/img/blog/single_blog_1.png
200      GET     1369l     8419w   695947c http://192.168.227.121/assets/img/blog/single_blog_2.png
200      GET      354l     3002w    46706c http://192.168.227.121/Contact.aspx
200      GET     1741l    10101w   822302c http://192.168.227.121/assets/img/blog/single_blog_3.png
200      GET     1808l    10471w   881382c http://192.168.227.121/assets/img/blog/single_blog_5.png
200      GET      522l     1550w    25997c http://192.168.227.121/Default.aspx
200      GET     1307l     7512w   627731c http://192.168.227.121/assets/img/blog/single_blog_4.png
200      GET      561l     1487w    30752c http://192.168.227.121/Blog.aspx
200      GET       14l       22w      261c http://192.168.227.121/js/main.js
200      GET        6l       77w     3351c http://192.168.227.121/css/style-owl.carousel.min.css
200      GET        2l     1283w    86926c http://192.168.227.121/js/jquery-3.3.1.min.js
200      GET        7l      662w    58072c http://192.168.227.121/js/bootstrap.min.js
200      GET       98l      251w     4083c http://192.168.227.121/Login.aspx
200      GET     4919l     8218w    79820c http://192.168.227.121/fonts/icomoon/style.css
200      GET      400l     2888w   190407c http://192.168.227.121/assets/img/Medical_doctor.png
200      GET      196l      548w     5103c http://192.168.227.121/css/style-login.css
200      GET        5l      369w    21003c http://192.168.227.121/js/popper.min.js
200      GET        7l     3223w   178198c http://192.168.227.121/css/style-bootstrap.min.css
200      GET      386l     1108w    19928c http://192.168.227.121/Services.aspx
403      GET       29l       92w     1233c http://192.168.227.121/assets/
403      GET       29l       92w     1233c http://192.168.227.121/css/
200      GET       20l       86w      962c http://192.168.227.121/error.aspx
403      GET       29l       92w     1233c http://192.168.227.121/fonts/
403      GET       29l       92w     1233c http://192.168.227.121/js/
403      GET       29l       92w     1233c http://192.168.227.121/master/
403      GET       29l       92w     1233c http://192.168.227.121/CSS/
200      GET       20l       86w      962c http://192.168.227.121/Error.aspx
403      GET       29l       92w     1233c http://192.168.227.121/JS/
403      GET       29l       92w     1233c http://192.168.227.121/Assets/
403      GET       29l       92w     1233c http://192.168.227.121/Css/
403      GET       29l       92w     1233c http://192.168.227.121/Js/
403      GET       29l       92w     1233c http://192.168.227.121/Master/
403      GET       29l       92w     1233c http://192.168.227.121/Fonts/
200      GET       98l      251w     4083c http://192.168.227.121/LogIn.aspx
200      GET       98l      251w     4083c http://192.168.227.121/LOGIN.aspx
200      GET      457l     1312w    22575c http://192.168.227.121/ABOUT.aspx
200      GET      561l     1487w    30752c http://192.168.227.121/BLOG.aspx
200      GET      354l     3002w    46706c http://192.168.227.121/CONTACT.aspx
403      GET       29l       92w     1233c http://192.168.227.121/ASSETS/
200      GET      386l     1108w    19928c http://192.168.227.121/SERVICES.aspx
200      GET      522l     1550w    25997c http://192.168.227.121/DEFAULT.aspx
200      GET       20l       86w      962c http://192.168.227.121/ERROR.aspx
403      GET       29l       92w     1233c http://192.168.227.121/FONTS/
403      GET       29l       92w     1233c http://192.168.227.121/jS/
200      GET       98l      251w     4083c http://192.168.227.121/logIn.aspx

```
