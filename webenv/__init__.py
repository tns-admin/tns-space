import os
import urllib
import jinja2
import webapp2

from utils.users import validate_current_user

from google.appengine.api import users as gusers
from google.appengine.ext import ndb


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(os.path.dirname(__file__))),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class RequestHandler(webapp2.RequestHandler):

    def __init__ (self, arg1, arg2):
        super (RequestHandler, self).__init__(arg1, arg2)
        validate_current_user (self)

    def render_response (self, response):
        template_path = "/templates/" + response ['template'];
        template = JINJA_ENVIRONMENT.get_template(template_path)
        self.response.write(template.render({'data': response ['data']}))

