```bash
feroxbuster -u http://192.168.196.143:80/ -t 10 -w /root/.local/share/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -r -o "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"
```

[/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt](file:///home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt):

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
    target_url: "http://192.168.196.143:80/",
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
    output: "/home/kali/Notes/Labs/OSCP-A/192.168.196.143/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt",
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
200      GET       15l       74w     6147c http://192.168.196.143/icons/ubuntu-logo.png
200      GET      375l      964w    10918c http://192.168.196.143/
404      GET        0l        0w     4024c http://192.168.196.143/.listing.txt
404      GET        0l        0w     4024c http://192.168.196.143/.well-known/genid.html
200      GET        3l      116w     4577c http://192.168.196.143/themes/default/js/modernizr-3.3.1-custom.min.js
200      GET      246l     3452w    27688c http://192.168.196.143/theme
200      GET       61l      223w     2022c http://192.168.196.143/themes/default/css/fontello.css
200      GET      386l     1148w     8882c http://192.168.196.143/themes/default/css/style.css
200      GET       74l      180w     2388c http://192.168.196.143/themes/default/js/pico.js
200      GET       41l       83w     1920c http://192.168.196.143/themes/default/css/droidsans.css
200      GET        1l       29w      353c http://192.168.196.143/themes/default/img/pico-white.svg
200      GET       85l      500w     5830c http://192.168.196.143/sub/page
200      GET       85l      503w     5853c http://192.168.196.143/sub
200      GET      134l      401w     4168c http://192.168.196.143/themes/default/js/utils.js
200      GET      506l     3886w    33888c http://192.168.196.143/0
200      GET       21l      172w     1085c http://192.168.196.143/LICENSE
404      GET        9l       31w      277c http://192.168.196.143/api/experiments
404      GET        9l       31w      277c http://192.168.196.143/api/experiments/configurations
404      GET        9l       31w      277c http://192.168.196.143/api/experiments.txt
404      GET        9l       31w      277c http://192.168.196.143/api/experiments/configurations.txt
404      GET        9l       31w      277c http://192.168.196.143/api/experiments.html
404      GET        9l       31w      277c http://192.168.196.143/api/experiments/configurations.html
404      GET        9l       31w      277c http://192.168.196.143/api/experiments.php
404      GET        0l        0w     4024c http://192.168.196.143/antivirus
404      GET        9l       31w      277c http://192.168.196.143/api/experiments/configurations.php
404      GET        9l       31w      277c http://192.168.196.143/api/experiments.asp
404      GET        9l       31w      277c http://192.168.196.143/api/experiments/configurations.asp
404      GET        9l       31w      277c http://192.168.196.143/api/experiments.aspx
404      GET        9l       31w      277c http://192.168.196.143/api/experiments/configurations.aspx
404      GET        9l       31w      277c http://192.168.196.143/api/experiments.jsp
404      GET        9l       31w      277c http://192.168.196.143/api/experiments/configurations.jsp
404      GET        0l        0w     4024c http://192.168.196.143/bdata.asp
404      GET        0l        0w     4024c http://192.168.196.143/drop.php
404      GET        0l        0w     4024c http://192.168.196.143/dumpenv
404      GET        0l        0w     4024c http://192.168.196.143/dropped.html
404      GET        0l        0w     4024c http://192.168.196.143/drupal.asp
404      GET        0l        0w     4024c http://192.168.196.143/dragon.jsp
404      GET        0l        0w     4024c http://192.168.196.143/erros.php
404      GET        0l        0w     4024c http://192.168.196.143/errorpage.jsp
404      GET        0l        0w     4024c http://192.168.196.143/externalisation.php
404      GET        0l        0w     4024c http://192.168.196.143/fake
404      GET        0l        0w     4024c http://192.168.196.143/failure.txt
404      GET        0l        0w     4024c http://192.168.196.143/fcategory.html
404      GET        0l        0w     4024c http://192.168.196.143/feedback
404      GET        0l        0w     4024c http://192.168.196.143/forms1.jsp
404      GET        0l        0w     4024c http://192.168.196.143/forum1.jsp
404      GET        0l        0w     4024c http://192.168.196.143/gate.php
404      GET        0l        0w     4024c http://192.168.196.143/gdform.asp
404      GET        0l        0w     4024c http://192.168.196.143/gateway.asp
404      GET        0l        0w     4024c http://192.168.196.143/geeklog.asp
404      GET        0l        0w     4024c http://192.168.196.143/guide.html
404      GET        0l        0w     4024c http://192.168.196.143/gwt.aspx
404      GET        0l        0w     4024c http://192.168.196.143/guide.asp
404      GET        0l        0w     4024c http://192.168.196.143/hack.php
404      GET        0l        0w     4024c http://192.168.196.143/handler.txt
404      GET        0l        0w     4024c http://192.168.196.143/hadoop.aspx
404      GET        0l        0w     4024c http://192.168.196.143/high.html
404      GET        0l        0w     4024c http://192.168.196.143/highslide.php
404      GET        0l        0w     4024c http://192.168.196.143/hire.html
404      GET        0l        0w     4024c http://192.168.196.143/hilfe.php
404      GET        0l        0w     4024c http://192.168.196.143/homepage.php
200      GET      506l     3886w    33888c http://192.168.196.143/index
200      GET      375l      964w    10918c http://192.168.196.143/index.html
200      GET      506l     3886w    33888c http://192.168.196.143/index.php
404      GET        0l        0w     4024c http://192.168.196.143/introduction.aspx
404      GET        0l        0w     4024c http://192.168.196.143/linkex
404      GET        0l        0w     4024c http://192.168.196.143/line.aspx
404      GET        0l        0w     4024c http://192.168.196.143/low.html
404      GET        0l        0w     4024c http://192.168.196.143/lst.php
404      GET        0l        0w     4024c http://192.168.196.143/magnifier_xml.aspx
404      GET        0l        0w     4024c http://192.168.196.143/mainten.aspx
404      GET        0l        0w     4024c http://192.168.196.143/order_history.txt
404      GET        0l        0w     4024c http://192.168.196.143/others.aspx
404      GET        0l        0w     4024c http://192.168.196.143/output.txt
404      GET        0l        0w     4024c http://192.168.196.143/page1
404      GET        0l        0w     4024c http://192.168.196.143/panel
404      GET        0l        0w     4024c http://192.168.196.143/path.aspx
404      GET        0l        0w     4024c http://192.168.196.143/paypal_notify.txt
404      GET        0l        0w     4024c http://192.168.196.143/pay.aspx
404      GET        0l        0w     4024c http://192.168.196.143/personal.php
404      GET        0l        0w     4024c http://192.168.196.143/pgadmin.asp
404      GET        0l        0w     4024c http://192.168.196.143/perl5.asp
404      GET        0l        0w     4024c http://192.168.196.143/phone
404      GET        0l        0w     4024c http://192.168.196.143/php168
404      GET        0l        0w     4024c http://192.168.196.143/phpbb2.php
404      GET        0l        0w     4024c http://192.168.196.143/prices.asp
404      GET        0l        0w     4024c http://192.168.196.143/privacy
404      GET        0l        0w     4024c http://192.168.196.143/project-admins.php
404      GET        0l        0w     4024c http://192.168.196.143/queues
404      GET        0l        0w     4024c http://192.168.196.143/readfolder.txt
404      GET        0l        0w     4024c http://192.168.196.143/realestate.txt
404      GET        0l        0w     4024c http://192.168.196.143/reference
404      GET        0l        0w     4024c http://192.168.196.143/remind_password.aspx
404      GET        0l        0w     4024c http://192.168.196.143/remind_password.jsp
404      GET        0l        0w     4024c http://192.168.196.143/replicated
404      GET        0l        0w     4024c http://192.168.196.143/replicated.txt
404      GET        0l        0w     4024c http://192.168.196.143/require.html
404      GET        0l        0w     4024c http://192.168.196.143/roaming.php
404      GET        0l        0w     4024c http://192.168.196.143/rpc.html
404      GET        0l        0w     4024c http://192.168.196.143/sm.aspx
404      GET        0l        0w     4024c http://192.168.196.143/speakers.txt
404      GET        0l        0w     4024c http://192.168.196.143/spanish.asp
404      GET        0l        0w     4024c http://192.168.196.143/spam.aspx
404      GET        0l        0w     4024c http://192.168.196.143/specified.html
404      GET        0l        0w     4024c http://192.168.196.143/system-admin.php
404      GET        0l        0w     4024c http://192.168.196.143/urlrewriter.php
404      GET        0l        0w     4024c http://192.168.196.143/web-inf.php
404      GET        0l        0w     4024c http://192.168.196.143/webplus.txt
404      GET        0l        0w     4024c http://192.168.196.143/111
404      GET        0l        0w     4024c http://192.168.196.143/123456.txt
404      GET        0l        0w     4024c http://192.168.196.143/168.php
404      GET        0l        0w     4024c http://192.168.196.143/561
404      GET        0l        0w     4024c http://192.168.196.143/813.php
404      GET        0l        0w     4024c http://192.168.196.143/811.jsp
404      GET        0l        0w     4024c http://192.168.196.143/_archived
404      GET        0l        0w     4024c http://192.168.196.143/_email.html
404      GET        0l        0w     4024c http://192.168.196.143/absolutenl.jsp
404      GET        0l        0w     4024c http://192.168.196.143/absolutecr.aspx
404      GET        0l        0w     4024c http://192.168.196.143/absolutepm.jsp
404      GET        0l        0w     4024c http://192.168.196.143/access_logs.html
404      GET        0l        0w     4024c http://192.168.196.143/acms
404      GET        0l        0w     4024c http://192.168.196.143/actualidad.html
404      GET        0l        0w     4024c http://192.168.196.143/add_to_cart.aspx
404      GET        0l        0w     4024c http://192.168.196.143/adops.aspx
404      GET        0l        0w     4024c http://192.168.196.143/ads2
404      GET        0l        0w     4024c http://192.168.196.143/advil.jsp
404      GET        0l        0w     4024c http://192.168.196.143/affil.php
404      GET        0l        0w     4024c http://192.168.196.143/after.php
404      GET        0l        0w     4024c http://192.168.196.143/agriculture
404      GET        0l        0w     4024c http://192.168.196.143/agreements.asp
404      GET        0l        0w     4024c http://192.168.196.143/ai
404      GET        0l        0w     4024c http://192.168.196.143/air.php
404      GET        0l        0w     4024c http://192.168.196.143/airfrancejp
404      GET        0l        0w     4024c http://192.168.196.143/aimages.jsp
404      GET        0l        0w     4024c http://192.168.196.143/aiuto
404      GET        0l        0w     4024c http://192.168.196.143/ajaxcontent
404      GET        0l        0w     4024c http://192.168.196.143/ajaxfiles.txt
404      GET        0l        0w     4024c http://192.168.196.143/alienform
404      GET        0l        0w     4024c http://192.168.196.143/ama.jsp
404      GET        0l        0w     4024c http://192.168.196.143/analyze
404      GET        0l        0w     4024c http://192.168.196.143/analytic.php
404      GET        0l        0w     4024c http://192.168.196.143/andorra.txt
404      GET        0l        0w     4024c http://192.168.196.143/apartment.asp
404      GET        0l        0w     4024c http://192.168.196.143/appcode.jsp
404      GET        0l        0w     4024c http://192.168.196.143/appform.php
404      GET        0l        0w     4024c http://192.168.196.143/app_styles.php
404      GET        0l        0w     4024c http://192.168.196.143/ara.html
404      GET        0l        0w     4024c http://192.168.196.143/aqua_products.php
404      GET        0l        0w     4024c http://192.168.196.143/apteka.html
404      GET        0l        0w     4024c http://192.168.196.143/backup_db
404      GET        0l        0w     4024c http://192.168.196.143/badgdformmail.php
404      GET        0l        0w     4024c http://192.168.196.143/badges
404      GET        0l        0w     4024c http://192.168.196.143/badbots.asp
404      GET        0l        0w     4024c http://192.168.196.143/bad-behavior.jsp
404      GET        0l        0w     4024c http://192.168.196.143/badbottrap.aspx
404      GET        0l        0w     4024c http://192.168.196.143/baike.php
404      GET        0l        0w     4024c http://192.168.196.143/barnaul.aspx
404      GET        0l        0w     4024c http://192.168.196.143/bausteine
404      GET        0l        0w     4024c http://192.168.196.143/bec.html
404      GET        0l        0w     4024c http://192.168.196.143/bee.html
404      GET        0l        0w     4024c http://192.168.196.143/bellsouth.asp
404      GET        0l        0w     4024c http://192.168.196.143/bestellung
404      GET        0l        0w     4024c http://192.168.196.143/branche.php
404      GET        0l        0w     4024c http://192.168.196.143/caitlin.txt
404      GET        0l        0w     4024c http://192.168.196.143/car-rental.txt
404      GET        0l        0w     4024c http://192.168.196.143/cast.html
404      GET        0l        0w     4024c http://192.168.196.143/castle
404      GET        0l        0w     4024c http://192.168.196.143/catads
404      GET        0l        0w     4024c http://192.168.196.143/catalog_test.txt
404      GET        0l        0w     4024c http://192.168.196.143/categ.txt
404      GET        0l        0w     4024c http://192.168.196.143/category_search.txt
404      GET        0l        0w     4024c http://192.168.196.143/categorydisplay.html
404      GET        0l        0w     4024c http://192.168.196.143/cgidir.html
404      GET        0l        0w     4024c http://192.168.196.143/cgv.asp
404      GET        0l        0w     4024c http://192.168.196.143/cgi-sec.jsp
404      GET        0l        0w     4024c http://192.168.196.143/charleston.php
404      GET        0l        0w     4024c http://192.168.196.143/charming.html
404      GET        0l        0w     4024c http://192.168.196.143/chpurl
404      GET        0l        0w     4024c http://192.168.196.143/choose.aspx
404      GET        0l        0w     4024c http://192.168.196.143/cic.php
404      GET        0l        0w     4024c http://192.168.196.143/clientvarremoval
404      GET        0l        0w     4024c http://192.168.196.143/clienttools.php
404      GET        0l        0w     4024c http://192.168.196.143/com_jomcomment.html
404      GET        0l        0w     4024c http://192.168.196.143/continguts.asp
404      GET        0l        0w     4024c http://192.168.196.143/continental.php
404      GET        0l        0w     4024c http://192.168.196.143/copying.aspx
404      GET        0l        0w     4024c http://192.168.196.143/corner.aspx
404      GET        0l        0w     4024c http://192.168.196.143/crea.aspx
404      GET        0l        0w     4024c http://192.168.196.143/crew.html
404      GET        0l        0w     4024c http://192.168.196.143/december.asp
404      GET        0l        0w     4024c http://192.168.196.143/delete_account
404      GET        0l        0w     4024c http://192.168.196.143/dev1.jsp
404      GET        0l        0w     4024c http://192.168.196.143/exhibitions.jsp
404      GET        0l        0w     4024c http://192.168.196.143/forum-old.html
404      GET        0l        0w     4024c http://192.168.196.143/fpp.txt
404      GET        0l        0w     4024c http://192.168.196.143/gbu0-display
404      GET        0l        0w     4024c http://192.168.196.143/give.txt
404      GET        0l        0w     4024c http://192.168.196.143/giving
404      GET        0l        0w     4024c http://192.168.196.143/giveaways.txt
404      GET        0l        0w     4024c http://192.168.196.143/gis.php
404      GET        0l        0w     4024c http://192.168.196.143/glasses
404      GET        0l        0w     4024c http://192.168.196.143/hiiamembership
404      GET        0l        0w     4024c http://192.168.196.143/home2
404      GET        0l        0w     4024c http://192.168.196.143/hp3
404      GET        0l        0w     4024c http://192.168.196.143/hpc.php
404      GET        0l        0w     4024c http://192.168.196.143/html_templates
404      GET        0l        0w     4024c http://192.168.196.143/htmleditor
404      GET        0l        0w     4024c http://192.168.196.143/htmlfiles.php
404      GET        0l        0w     4024c http://192.168.196.143/htmlrotate.html
404      GET        0l        0w     4024c http://192.168.196.143/htmleditor.aspx
404      GET        0l        0w     4024c http://192.168.196.143/hypernews.html
404      GET        0l        0w     4024c http://192.168.196.143/i18n.jsp
404      GET        0l        0w     4024c http://192.168.196.143/ib_html.txt
404      GET        0l        0w     4024c http://192.168.196.143/ill.txt
404      GET        0l        0w     4024c http://192.168.196.143/imagecrop.txt
404      GET        0l        0w     4024c http://192.168.196.143/imageresizer.html
404      GET        0l        0w     4024c http://192.168.196.143/infusions.txt
404      GET        0l        0w     4024c http://192.168.196.143/ing.html
404      GET        0l        0w     4024c http://192.168.196.143/ingredients.txt
404      GET        0l        0w     4024c http://192.168.196.143/isbn
404      GET        0l        0w     4024c http://192.168.196.143/it-ch.asp
404      GET        0l        0w     4024c http://192.168.196.143/itemd.txt
404      GET        0l        0w     4024c http://192.168.196.143/java-script.html
404      GET        0l        0w     4024c http://192.168.196.143/kris.jsp
404      GET        0l        0w     4024c http://192.168.196.143/lnk
404      GET        0l        0w     4024c http://192.168.196.143/media_new.asp
404      GET        0l        0w     4024c http://192.168.196.143/miles.html
404      GET        0l        0w     4024c http://192.168.196.143/miki.asp
404      GET        0l        0w     4024c http://192.168.196.143/mikey.aspx
404      GET        0l        0w     4024c http://192.168.196.143/millennium.asp
404      GET        0l        0w     4024c http://192.168.196.143/million.php
404      GET        0l        0w     4024c http://192.168.196.143/mikey.jsp
404      GET        0l        0w     4024c http://192.168.196.143/ml2.txt
404      GET        0l        0w     4024c http://192.168.196.143/mktg.asp
404      GET        0l        0w     4024c http://192.168.196.143/mng.html
404      GET        0l        0w     4024c http://192.168.196.143/mocks
404      GET        0l        0w     4024c http://192.168.196.143/niners
404      GET        0l        0w     4024c http://192.168.196.143/old-pages.txt
404      GET        0l        0w     4024c http://192.168.196.143/onlineoffice.php
404      GET        0l        0w     4024c http://192.168.196.143/px.php
404      GET        0l        0w     4024c http://192.168.196.143/pyramid.php
404      GET        0l        0w     4024c http://192.168.196.143/qalert
404      GET        0l        0w     4024c http://192.168.196.143/qanda.aspx
404      GET        0l        0w     4024c http://192.168.196.143/rotatorwidget
404      GET        0l        0w     4024c http://192.168.196.143/scaffolding
404      GET        0l        0w     4024c http://192.168.196.143/sbs.asp
404      GET        0l        0w     4024c http://192.168.196.143/sheets.jsp
404      GET        0l        0w     4024c http://192.168.196.143/specification.aspx
404      GET        0l        0w     4024c http://192.168.196.143/user_session.asp
404      GET        0l        0w     4024c http://192.168.196.143/440.aspx
404      GET        0l        0w     4024c http://192.168.196.143/MessageCenter.php
404      GET        0l        0w     4024c http://192.168.196.143/1049.jsp
404      GET        0l        0w     4024c http://192.168.196.143/AK.jsp
404      GET        0l        0w     4024c http://192.168.196.143/Track.txt
404      GET        0l        0w     4024c http://192.168.196.143/handbooks.asp
404      GET        0l        0w     4024c http://192.168.196.143/1713.aspx
404      GET        0l        0w     4024c http://192.168.196.143/1780
404      GET        0l        0w     4024c http://192.168.196.143/1713.jsp
404      GET        0l        0w     4024c http://192.168.196.143/1806.asp
404      GET        0l        0w     4024c http://192.168.196.143/1852.txt
404      GET        0l        0w     4024c http://192.168.196.143/1889.txt
404      GET        0l        0w     4024c http://192.168.196.143/1876.asp
404      GET        0l        0w     4024c http://192.168.196.143/1956
404      GET        0l        0w     4024c http://192.168.196.143/1977.html
404      GET        0l        0w     4024c http://192.168.196.143/2033.aspx
404      GET        0l        0w     4024c http://192.168.196.143/2158.php
404      GET        0l        0w     4024c http://192.168.196.143/2351
404      GET        0l        0w     4024c http://192.168.196.143/2290.asp
404      GET        0l        0w     4024c http://192.168.196.143/hodnoceni
404      GET        0l        0w     4024c http://192.168.196.143/gos.aspx
404      GET        0l        0w     4024c http://192.168.196.143/horoscopo.html
404      GET        0l        0w     4024c http://192.168.196.143/viewContent.aspx
404      GET        0l        0w     4024c http://192.168.196.143/whatshot.txt
404      GET        0l        0w     4024c http://192.168.196.143/ebm.txt
404      GET        0l        0w     4024c http://192.168.196.143/downloadnow.jsp
404      GET        0l        0w     4024c http://192.168.196.143/5965.php
404      GET        0l        0w     4024c http://192.168.196.143/GSA.html
404      GET        0l        0w     4024c http://192.168.196.143/pathology
404      GET        0l        0w     4024c http://192.168.196.143/partners-links.asp
404      GET        0l        0w     4024c http://192.168.196.143/10354.html
404      GET        0l        0w     4024c http://192.168.196.143/2559.php
404      GET        0l        0w     4024c http://192.168.196.143/6250.aspx
404      GET        0l        0w     4024c http://192.168.196.143/Armani.php
404      GET        0l        0w     4024c http://192.168.196.143/Aurora
404      GET        0l        0w     4024c http://192.168.196.143/App_Services.aspx
404      GET        0l        0w     4024c http://192.168.196.143/Association.html
404      GET        0l        0w     4024c http://192.168.196.143/browserepos.jsp
404      GET        0l        0w     4024c http://192.168.196.143/test_folder.txt
404      GET        0l        0w     4024c http://192.168.196.143/testflash.php
404      GET        0l        0w     4024c http://192.168.196.143/thematiques
404      GET        0l        0w     4024c http://192.168.196.143/thriller
404      GET        0l        0w     4024c http://192.168.196.143/2606.jsp
404      GET        0l        0w     4024c http://192.168.196.143/6932.jsp
404      GET        0l        0w     4024c http://192.168.196.143/Spiritual.html
404      GET        0l        0w     4024c http://192.168.196.143/ashby.asp
404      GET        0l        0w     4024c http://192.168.196.143/aves.php
404      GET        0l        0w     4024c http://192.168.196.143/avo.php
404      GET        0l        0w     4024c http://192.168.196.143/ayamonte.txt
404      GET        0l        0w     4024c http://192.168.196.143/blz.aspx
404      GET        0l        0w     4024c http://192.168.196.143/boc_import.jsp
404      GET        0l        0w     4024c http://192.168.196.143/how-to-use.html
404      GET        0l        0w     4024c http://192.168.196.143/hrms.html
404      GET        0l        0w     4024c http://192.168.196.143/hubdisplay
404      GET        0l        0w     4024c http://192.168.196.143/hubpages.asp
404      GET        0l        0w     4024c http://192.168.196.143/hurley.html
404      GET        0l        0w     4024c http://192.168.196.143/regent.txt
404      GET        0l        0w     4024c http://192.168.196.143/PointRollAds.asp
404      GET       67l      149w     2752c http://192.168.196.143/_meta
404      GET        0l        0w     4024c http://192.168.196.143/allcategories.aspx
404      GET        0l        0w     4024c http://192.168.196.143/dcl.txt
404      GET        0l        0w     4024c http://192.168.196.143/foglalas.txt
404      GET        0l        0w     4024c http://192.168.196.143/foosun.asp
404      GET        0l        0w     4024c http://192.168.196.143/footer-faqs.php
404      GET        0l        0w     4024c http://192.168.196.143/form_1
404      GET        0l        0w     4024c http://192.168.196.143/index99.aspx
404      GET        0l        0w     4024c http://192.168.196.143/indexNEW.asp
404      GET        0l        0w     4024c http://192.168.196.143/index_OLD.txt
404      GET        0l        0w     4024c http://192.168.196.143/index_content
404      GET        0l        0w     4024c http://192.168.196.143/main_news.asp
404      GET        0l        0w     4024c http://192.168.196.143/matola.aspx
404      GET        0l        0w     4024c http://192.168.196.143/maven-repository
404      GET        0l        0w     4024c http://192.168.196.143/p134
404      GET        0l        0w     4024c http://192.168.196.143/p100.jsp
404      GET        0l        0w     4024c http://192.168.196.143/p131.asp
404      GET        0l        0w     4024c http://192.168.196.143/rojales.asp
404      GET        0l        0w     4024c http://192.168.196.143/sprava.html
404      GET        0l        0w     4024c http://192.168.196.143/system_cache
404      GET        0l        0w     4024c http://192.168.196.143/tabernas.jsp
404      GET        0l        0w     4024c http://192.168.196.143/torroellafluvia.php
404      GET        0l        0w     4024c http://192.168.196.143/webverzeichnis.aspx
404      GET        0l        0w     4024c http://192.168.196.143/weightwatchers.aspx
404      GET        0l        0w     4024c http://192.168.196.143/10506.txt
404      GET        0l        0w     4024c http://192.168.196.143/14372.txt
404      GET        0l        0w     4024c http://192.168.196.143/FT
404      GET        0l        0w     4024c http://192.168.196.143/Impala.php
404      GET        0l        0w     4024c http://192.168.196.143/ImportData.aspx
404      GET        0l        0w     4024c http://192.168.196.143/Incident.jsp
404      GET        0l        0w     4024c http://192.168.196.143/PACKAGES.jsp
404      GET        0l        0w     4024c http://192.168.196.143/actrice-porno.jsp
404      GET        0l        0w     4024c http://192.168.196.143/algarpalancia.jsp
404      GET        0l        0w     4024c http://192.168.196.143/billybush
404      GET        0l        0w     4024c http://192.168.196.143/classified_ads.jsp
404      GET        0l        0w     4024c http://192.168.196.143/classifications.jsp
404      GET        0l        0w     4024c http://192.168.196.143/developing.aspx
404      GET        0l        0w     4024c http://192.168.196.143/directory-rss.jsp
404      GET        0l        0w     4024c http://192.168.196.143/easels.txt
404      GET        0l        0w     4024c http://192.168.196.143/fiche_visite.html
404      GET        0l        0w     4024c http://192.168.196.143/gsbs.php
404      GET        0l        0w     4024c http://192.168.196.143/icecast
404      GET        0l        0w     4024c http://192.168.196.143/kittitas.aspx
404      GET        0l        0w     4024c http://192.168.196.143/kriminalistika.aspx
404      GET        0l        0w     4024c http://192.168.196.143/krl.aspx
404      GET        0l        0w     4024c http://192.168.196.143/photoUpload.asp
404      GET        0l        0w     4024c http://192.168.196.143/photos_jpgs.html
404      GET        0l        0w     4024c http://192.168.196.143/wish-news.html

```
