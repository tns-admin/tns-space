import os
import urllib
import jinja2
import webapp2
import json

from pytns.google_utils import users as google_users
from pytns.utils import users

import logging as log

def get_root_path ():
    file_path = os.path.dirname(__file__)
    return os.path.dirname(os.path.dirname(file_path))


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(get_root_path ()),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class RequestHandler(webapp2.RequestHandler):

    def __init__ (self, arg1, arg2):
        super (RequestHandler, self).__init__(arg1, arg2)
        # validate user
        user = users.get_current_user ()
        if not user or not user.is_active ():
            self.redirect(google_users.create_logout_url())


    def render_response (self, response):
        template_path = "/templates/" + response ['template'];
        template = JINJA_ENVIRONMENT.get_template(template_path)
        self.response.write(template.render({'data': response ['data']}))

    def render_ajax_response (self, response):
        json_string = json.dumps(response)
        self.response.write(json_string)
