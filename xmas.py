# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:48:12 2019

@author: CAA7BIE
Creating an advent calendar for the CC-PS/EMT2 Bosch team
Figures out if today is in advent or not and returns a page with an image of an
xmas wreath with the correct number of lit candles and a link to a funny 
gif/video or meme
"""
import os
import cherrypy
import datetime
import csv

#Configuration
path   = os.path.abspath(os.path.dirname(__file__))
config = {
  'global' : {
    'server.socket_host' : '0.0.0.0',
    'server.socket_port' : 8080,
    'server.thread_pool' : 8,
  },
  '/public' : {
    'tools.staticdir.on'    : True,
    'tools.staticdir.dir'   : os.path.join(path, 'public'),
    'tools.gzip.on'         : True  
  }  
}
  
#Dict of dates and links
with open('xmasLinks.csv') as links:
    linksReader = csv.reader(links, delimiter=';')
    Links = dict()

    for row in linksReader: #Building advent link dictionary
        dates = row[0]
        Links[dates] = row[1]

#Returns link for date in dictionary
def getLink(diction, now, sundays, xmas):
    if now>=sundays[3] and now<=xmas:
        linkValue = diction['({}, {})'.format(now.day,now.month)]
    else:
        linkValue = 'https://giphy.com/gifs/photoset-american-horror-story-ahs-2WcZzkFprBJHW/fullscreen'
    return linkValue

#Returns opacity of each flame
def getFlames(now, sundays, xmas, xmas_eve):
    flames = []
    if now<=xmas and now>=sundays[0]:
        flames = [1,1,1,1]
    elif now<sundays[0] and now>=sundays[1]:
        flames = [1,1,1,0]
    elif now<sundays[1] and now>=sundays[2]:
        flames = [1,1,0,0]
    elif now<sundays[2] and now>=sundays[3]:
        flames = [1,0,0,0]
    else:
        flames = [0,0,0,0] 
    return flames

#Finding sundays of advent
def SundaysOfAdvent(now):
    day = datetime.date(now.year, 12, 25)
    sundays = []
    while len(sundays)<4:
        day+= datetime.timedelta(days=-1)
        if day.weekday()==6:
            sundays.append((day))
    return sundays

#Dates




outer_glow = "animation: glowFlicker 3.6s linear infinite;"
outer_outer_glow = "animation: glowFlicker 3s linear infinite;"

class Xmas(object):
    @cherrypy.expose
    def index(self):
        now = datetime.date.today()
        xmas = datetime.date(now.year,12,25)
        days_to_go = (xmas - now).days        
        xmas_eve = datetime.date(now.year,12,24)        
        sundays = SundaysOfAdvent(now)
        linkValue = getLink(Links, now, sundays, xmas)
        flames = getFlames(now, sundays, xmas, xmas_eve)      
        return """
      <html>

<head>
    <link href="public/output-xmas.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Pacifico" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Calligraffitti" rel="stylesheet">
</head>
<body>
    <div class="wreath">
        <div class="wreath__inner">
        <a href=""" + linkValue + """ target="_blank">
            <div id="circle"></div>
            <script>
                var x = "", i;
                for (i = 0; i < 30; i++) {
                    x = x + '<div class="circle"></div>';
                }
                document.getElementById("circle").innerHTML = x;
            </script>

            <div id="pine"></div>
            <script>
                var x = "", i;
                for (i = 0; i < 1000; i++) {
                    x = x + '<div class="pine"></div>';
                }
                document.getElementById("pine").innerHTML = x;
            </script>

            <div id="holly"></div>
            <script>
                var x = "", i;
                for (i = 0; i < 50; i++) {
                    x = x + '<div class="holly"></div>';
                }
                document.getElementById("holly").innerHTML = x;
            </script>

            <div id="light"></div>
            <script>
                var x = "", i;
                for (i = 0; i < 50; i++) {
                    x = x + '<div class="light"></div>';
                }
                document.getElementById("light").innerHTML = x;
            </script>

            <div class="bow">
                <div class="actual"></div>
            </div>
        <div class="joie" >""" + str(days_to_go) + """
            <div class="second">Days til Xmas!</div>
            <div class="third">Click for a surprise!!</div>
            </a>
        </div>
        </div> """ + f"""
    <div class="container c1">
            <div class="flame" style="opacity:{flames[0]};" >
                <div class="inner-flame"></div>
            </div>
            <div class="outer-glow outer-glow1" style="opacity:{flames[0]}; {flames[0] * outer_glow}">
                <div class="outer-outer-glow outer-glow1" style="opacity:{flames[0]}; {flames[0] * outer_outer_glow}"></div>
                <div class="inner-outer-glow outer-inner-glow1" style="opacity:{flames[0]};"></div>
            </div>
            <div class="wick"></div>
            <div class="candle candle-bg1">
                <div class="top candle-top-bg1">
                    <div class="top_inner candle-top-inner-bg1"></div>
                </div>
                <div class="bottom candle-bg1"></div>
                <div class="wax-drip candle-wax1" style="opacity:{flames[0]};">
                    <div class="falling-wax candle-wax1"></div>
                </div>
                <div class="wax-droppings candle-wax1" style="opacity:{flames[0]};">
                    <div class="more-droppings candle-wax1"></div>
                </div>
            </div>
            <div class="plate">
                <div class="plate-inner"></div>
            </div>
            <div class="plate-bottom"></div>
    </div>
    <div class="container c2">
            <div class="flame" style="opacity:{flames[1]};">
                <div class="inner-flame"></div>
            </div>
            <div class="outer-glow outer-glow1" style="opacity:{flames[1]}; {flames[1] * outer_glow}">
                <div class="outer-outer-glow outer-glow1"  style="opacity:{flames[1]};{flames[1] * outer_outer_glow}"></div>
                <div class="inner-outer-glow outer-inner-glow1"  style="opacity:{flames[1]};"></div>
            </div>
            <div class="wick"></div>
            <div class="candle candle-bg1">
                <div class="top candle-top-bg1">
                    <div class="top_inner candle-top-inner-bg1"></div>
                </div>
                <div class="bottom candle-bg1"></div>
                <div class="wax-drip candle-wax1" style="opacity:{flames[1]};">
                    <div class="falling-wax candle-wax1"></div>
                </div>
                <div class="wax-droppings candle-wax1" style="opacity:{flames[1]};">
                    <div class="more-droppings candle-wax1"></div>
                </div>
            </div>
            <div class="plate">
                <div class="plate-inner"></div>
            </div>
            <div class="plate-bottom"></div>
    </div>
    <div class="container c3">
            <div class="flame" style="opacity:{flames[2]};">
                <div class="inner-flame"></div>
            </div>
            <div class="outer-glow outer-glow2"  style="opacity:{flames[2]}; {flames[2] * outer_glow}">
                <div class="outer-outer-glow outer-glow2"  style="opacity:{flames[2]};{flames[2] * outer_outer_glow}"></div>
                <div class="inner-outer-glow outer-inner-glow2"  style="opacity:{flames[2]};"></div>
            </div>
            <div class="wick"></div>
            <div class="candle candle-bg2">
                <div class="top candle-top-bg2">
                    <div class="top_inner candle-top-inner-bg2"></div>
                </div>
                <div class="bottom candle-bg2"></div>
                <div class="wax-drip candle-wax2" style="opacity:{flames[2]};">
                    <div class="falling-wax candle-wax2"></div>
                </div>
                <div class="wax-droppings candle-wax2" style="opacity:{flames[2]};">
                    <div class="more-droppings candle-wax2"></div>
                </div>
            </div>
            <div class="plate">
                <div class="plate-inner"></div>
            </div>
            <div class="plate-bottom"></div>
    </div>
    <div class="container c4">
            <div class="flame" style="opacity:{flames[3]};">
                <div class="inner-flame"></div>
            </div>
            <div class="outer-glow outer-glow1" style="opacity:{flames[3]}; {flames[3] * outer_glow}">
                <div class="outer-outer-glow outer-glow1" style="opacity:{flames[3]}; {flames[3] * outer_outer_glow}"></div>
                <div class="inner-outer-glow outer-inner-glow1" style="opacity:{flames[3]};"></div>
            </div>
            <div class="wick"></div>
            <div class="candle candle-bg1">
                <div class="top candle-top-bg1">
                    <div class="top_inner candle-top-inner-bg1"></div>
                </div>
                <div class="bottom candle-bg1"></div>
                <div class="wax-drip candle-wax1" style="opacity:{flames[3]};">
                    <div class="falling-wax candle-wax1"></div>
                </div>
                <div class="wax-droppings candle-wax1" style="opacity:{flames[3]};">
                    <div class="more-droppings candle-wax1"></div>
                </div>
            </div>
            <div class="plate">
                <div class="plate-inner"></div>
            </div>
            <div class="plate-bottom"></div>
    </div>
</div>
</body>

</html>"""
if __name__ == '__main__':
    cherrypy.quickstart(Xmas(), '/', config)
