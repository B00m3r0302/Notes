```bash
curl -sSik http://10.10.11.187:80/
```

[/home/kali/Notes/Labs/htb/flight/scans/tcp80/tcp_80_http_curl.html](file:///home/kali/Notes/Labs/htb/flight/scans/tcp80/tcp_80_http_curl.html):

```
HTTP/1.1 200 OK
Date: Tue, 14 Jan 2025 06:21:20 GMT
Server: Apache/2.4.52 (Win64) OpenSSL/1.1.1m PHP/8.1.1
Last-Modified: Thu, 24 Feb 2022 05:58:10 GMT
ETag: "1b9d-5d8bd444f0080"
Accept-Ranges: bytes
Content-Length: 7069
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
<title>g0 Aviation</title>
<meta charset="utf-8">
<link rel="stylesheet" href="css/reset.css" type="text/css" media="all">
<link rel="stylesheet" href="css/layout.css" type="text/css" media="all">
<link rel="stylesheet" href="css/style.css" type="text/css" media="all">
<script type="text/javascript" src="js/jquery-1.4.2.js" ></script>
<script type="text/javascript" src="js/cufon-yui.js"></script>
<script type="text/javascript" src="js/cufon-replace.js"></script>
<script type="text/javascript" src="js/Myriad_Pro_italic_600.font.js"></script>
<script type="text/javascript" src="js/Myriad_Pro_italic_400.font.js"></script>
<script type="text/javascript" src="js/Myriad_Pro_400.font.js"></script>
<!--[if lt IE 9]>
<script type="text/javascript" src="js/ie6_script_other.js"></script>
<script type="text/javascript" src="js/html5.js"></script>
<![endif]-->
</head>
<body id="page1">
<!-- START PAGE SOURCE -->
<div class="body1">
  <div class="main">
    <header>
      <div class="wrapper">
        <h1><a href="index.html" id="logo">g0</a><span id="slogan">International Travel</span></h1>
        <div class="right">
          <nav>
            <ul id="top_nav">
              <li><a href="#"><img src="images/img1.gif" alt=""></a></li>
              <li><a href="#"><img src="images/img2.gif" alt=""></a></li>
              <li class="bg_none"><a href="#"><img src="images/img3.gif" alt=""></a></li>
            </ul>
          </nav>
          <nav>
            <ul id="menu">
              <li id="menu_active"><a href="index.html">Home</a></li>
              <li><a href="#">Our Aircraft</a></li>
              <li><a href="#">Safety</a></li>
              <li><a href="#">Charters</a></li>
              <li><a href="#">Contacts</a></li>
            </ul>
          </nav>
        </div>
      </div>
    </header>
  </div>
</div>
<div class="main">
  <div id="banner">
    <div class="text1"> COMFORT<span>Guaranteed</span>
      <p>g0 is the world's largest aerospace company and leading manufacturer of commercial jetliners, defense, space and security systems, and service provider of aftermarket support.</p>
    </div>
    <a href="#" class="button_top">Order Tickets Online</a></div>
</div>
<div class="main">
  <section id="content">
    <article class="col1">
      <div class="pad_1">
        <h2>Your Flight Planner</h2>
        <form id="form_1" action="#" method="post">
          <div class="wrapper pad_bot1">
            <div class="radio marg_right1">
              <input type="radio" name="name1">
              Round Trip<br>
              <input type="radio" name="name1">
              One Way </div>
            <div class="radio">
              <input type="radio" name="name1">
              Empty-Leg<br>
              <input type="radio" name="name1">
              Multi-Leg </div>
          </div>
          <div class="wrapper"> Leaving From:
            <div class="bg">
              <input type="text" class="input input1" value="Enter City or Airport Code" onBlur="if(this.value=='') this.value='Enter City or Airport Code'" onFocus="if(this.value =='Enter City or Airport Code' ) this.value=''">
            </div>
          </div>
          <div class="wrapper"> Going To:
            <div class="bg">
              <input type="text" class="input input1" value="Enter City or Airport Code" onBlur="if(this.value=='') this.value='Enter City or Airport Code'" onFocus="if(this.value =='Enter City or Airport Code' ) this.value=''">
            </div>
          </div>
          <div class="wrapper"> Departure Date and Time:
            <div class="wrapper">
              <div class="bg left">
                <input type="text" class="input input2" value="mm/dd/yyyy " onBlur="if(this.value=='') this.value='mm/dd/yyyy '" onFocus="if(this.value =='mm/dd/yyyy ' ) this.value=''">
              </div>
              <div class="bg right">
                <input type="text" class="input input2" value="12:00am" onBlur="if(this.value=='') this.value='12:00am'" onFocus="if(this.value =='12:00am' ) this.value=''">
              </div>
            </div>
          </div>
          <div class="wrapper"> Return Date and Time:
            <div class="wrapper">
              <div class="bg left">
                <input type="text" class="input input2" value="mm/dd/yyyy " onBlur="if(this.value=='') this.value='mm/dd/yyyy '" onFocus="if(this.value =='mm/dd/yyyy ' ) this.value=''">
              </div>
              <div class="bg right">
                <input type="text" class="input input2" value="12:00am" onBlur="if(this.value=='') this.value='12:00am'" onFocus="if(this.value =='12:00am' ) this.value=''">
              </div>
            </div>
          </div>
          <div class="wrapper">
            <p>Passenger(s):</p>
            <div class="bg left">
              <input type="text" class="input input2" value="# passengers" onBlur="if(this.value=='') this.value='# passengers'" onFocus="if(this.value =='# passengers' ) this.value=''">
            </div>
            <a href="#" class="button2">go!</a> </div>
        </form>
        <h2>Recent News</h2>
        <p class="under"><a href="#" class="link1">Nemo enim ipsam voluptatem quia</a><br>
          November 5, 2010</p>
        <p class="under"><a href="#" class="link1">Voluptas aspernatur autoditaut fjugit</a><br>
          November 1, 2010</p>
        <p><a href="#" class="link1">Sed quia consequuntur magni</a><br>
          October 23, 2010</p>
      </div>
    </article>
    <article class="col2 pad_left1">
      <h2>Welcome to our Website!</h2>
      <p class="color1">As Italy's biggest manufacturing exporter, the company supports airlines and allied government customers in more than 150 countries.</p>

      <div class="wrapper pad_bot2"> <a href="#" class="button1">Reservation</a> <a href="#" class="button2">Fleet</a> </div>
      <div class="wrapper">
        <article class="cols">
          <h2>Apply to out Team!</h2>
          <p><strong>We are Hiring</strong> We are looking for talented engineers specializing in aeronautics. Quick apply to our team by going to the contact page.</p>
        </article>
        <div class="box1">
          <div class="pad_1">
            <div class="wrapper">
            </div>
          </div>
        </div>
      </div>
    </article>
  </section>
</div>
<div class="body2">
  <div class="main">
    <footer>
      <div class="footerlink">
        <p class="lf">Copyright 2022 <a href="#">flight.htb</a> - All Rights Reserved</p>
        <p class="rf">Designed by <a href="https://twitter.com/Geiseric4" class="twitter">Geiseric</a> & <a href="https://twitter.com/Janit10043163" class="twitter">JDgodd</a></p>
        <div style="clear:both;"></div>
      </div>
    </footer>
  </div>
</div>
<script type="text/javascript"> Cufon.now(); </script>
<!-- END PAGE SOURCE -->
</body>
</html>

```
