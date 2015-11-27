import webapp2
import jinja2
import sys
sys.path.insert(0, 'lib')
import httplib2
import os
from google.appengine.ext.webapp import template
from apiclient.discovery import build
from oauth2client.appengine import AppAssertionCredentials
 
class ShowHome(webapp2.RequestHandler):
    def get(self):
        temp_data = {}
        temp_path = 'Templates/index.html'
        self.response.out.write(template.render(temp_path,temp_data))

class ShowDash(webapp2.RequestHandler):
    def get(self):
        temp_data = {}
        temp_path = 'Templates/dash.html'
        self.response.out.write(template.render(temp_path,temp_data)) 

class ShowDashHijos(webapp2.RequestHandler):
    def get(self):
        temp_data = {}
        temp_path = 'Templates/dashHijos.html'
        self.response.out.write(template.render(temp_path,temp_data)) 

class ShowDashEdades(webapp2.RequestHandler):
    def get(self):
        temp_data = {}
        temp_path = 'Templates/dashEdades.html'
        self.response.out.write(template.render(temp_path,temp_data)) 

class ShowDashOficina(webapp2.RequestHandler):
    def get(self):
        temp_data = {}
        temp_path = 'Templates/dashOficina.html'
        self.response.out.write(template.render(temp_path,temp_data)) 

class ShowDashInteres(webapp2.RequestHandler):
    def get(self):
        temp_data = {}
        temp_path = 'Templates/dashInteres.html'
        self.response.out.write(template.render(temp_path,temp_data))

class ShowDashPorcentaje(webapp2.RequestHandler):
    def get(self):
        temp_data = {}
        temp_path = 'Templates/dashPorcentaje.html'
        self.response.out.write(template.render(temp_path,temp_data))

class ShowMapa(webapp2.RequestHandler):
    def get(self):
        temp_data = {}
        temp_path = 'Templates/mapa.html'
        self.response.out.write(template.render(temp_path,temp_data)) 

class ShowCustom(webapp2.RequestHandler):
    def get(self):
        temp_data = {}
        temp_path = 'Templates/custom.html'
        self.response.out.write(template.render(temp_path,temp_data)) 

class ShowTwitter(webapp2.RequestHandler):
    def get(self):
        temp_data = {}
        temp_path = 'Templates/twitter.html'
        self.response.out.write(template.render(temp_path,temp_data)) 

application = webapp2.WSGIApplication([
    ('/dash',ShowDash),
    ('/dashEdades',ShowDashEdades),
    ('/dashHijos',ShowDashHijos),
    ('/dashOficina',ShowDashOficina),
    ('/dashInteres',ShowDashInteres),
    ('/dashPorcentaje',ShowDashPorcentaje),
    ('/mapa',ShowMapa),
    ('/twitter',ShowTwitter),
    ('/custom',ShowCustom),
    ('/', ShowHome),
], debug=True)