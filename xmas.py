# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:48:12 2019

@author: CAA7BIE
"""
import os
import cherrypy


path   = os.path.abspath(os.path.dirname(__file__))
config = {
  'global' : {
    'server.socket_host' : '127.0.0.1',
    'server.socket_port' : 8080,
    'server.thread_pool' : 8,
  },
  '/public' : {
    'tools.staticdir.on'    : True,
    'tools.staticdir.dir'   : os.path.join(path, 'public'),
    'tools.gzip.on'         : True  
  }  
}
  
linkValue = "http://bzo.bosch.com/bzo/en/start_page.html"

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """
        <html>
            <head>
                <link href="public/style.css" rel="stylesheet">
                <script type="text/javascript" src="public/main.js"></script>
            </head>
            <body>
                <img src="public/wreath.png" alt="Xmas wreath" width="500" height="500">
                <!--
                <form method="get" action="get_vid">
                    <input type="text" value="8" name="length" />
                    <button type="submit" onclick="get_vid()">Give it now!</button>
                </form>
                -->
                <a href={} target="_blank" class="link-button">Test Button</a>
            </body>
        </html>""".format(linkValue)
    
    @cherrypy.expose
    def get_vid(self):
        return 'xmas vid link'
    
    
    @cherrypy.expose
    def test(self):
        return 'Hello World'


if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator(), '/', config)