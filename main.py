import os
import urllib
import jinja2
import webapp2

import tns_users
import sidebar

from google.appengine.api import users
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def validate_current_user (request_handler):
    valid_users = ["admin@tnstax.co.uk",
                   "sergii.romanov@tnstax.co.uk",
                   "tatiana.gutu@tnstax.co.uk",
                  ]
    user = users.get_current_user()
    if not user or user.email () not in valid_users:
        request_handler.redirect(users.create_login_url(request_handler.request.uri))

class MainPage(webapp2.RequestHandler):

    def get(self):
        validate_current_user (self)
        page = self.request.get('page')

        data = {
            'user': users.get_current_user(),
            'page': page,
            'sidebar': sidebar.process_request (self.request)
        }

        if page == "users":
            data ["users"] = tns_users.process_request (self.request)
#        if page == "clients":
#            data ["clients"] = clients.process_request (request)
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render({'data': data}))


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
