#import os
#import urllib
import jinja2
import webapp2
import logging as log

from google.appengine.api import users as gusers

from utils.users import validate_current_user

import client_general
import client_personal
import client_agreements

client_pages = {
  'general':    {'text': "General", 'request_handler': client_general.process_request},
  'personal':   {'text': "Personal", 'request_handler': client_personal.process_request},
  'agreements': {'text': "Agreements", 'request_handler': client_agreements.process_request}
}

def generate_sidebar_data (current_page):
  # ordered list of visible pages
  visible_pages = ['general', 'personal', 'agreements']

  pages = []
  for page in visible_pages:
    page_entry = {'page': page,
                  'text': client_pages [page] ['text'],
                  'url' : '/client?page=' + page}
    pages.append (page_entry)

  return {'current_page': current_page, "pages": pages}


class RequestHandler:

  def process_request (self, request):
    client_id = request.get('id')
    page = request.get('page', 'general')

    data = {
      'user': gusers.get_current_user(),
      'client_id': client_id,
      'body_template': "/templates/client/client_" + page + ".html",
      'sidebar': generate_sidebar_data (page)
    }

    #log.error (client_pages [page])

    data [page] = (client_pages [page] ['request_handler']) (request)

    return {"template": "client/client.html", "data": data}

'''
class RequestHandler(webapp2.RequestHandler):

    def get(self):
        validate_current_user (self)
        client_id = self.request.get('id')
        page = self.request.get('page')

        data = {
            'user': gusers.get_current_user(),
            'client_id': client_id,
            'page': page,
            'sidebar': client_sidebar.process_request (self.request)
        }

        if page == "general":
            data ["general"] = client_general.process_request (self.request)
        if page == "personal":

            data ["personal"] = client_personal.process_request (self.request)
        if page == "agreements":
            data ["agreements"] = client_agreements.process_request (self.request)

        template = JINJA_ENVIRONMENT.get_template('templates/client.html')
        self.response.write(template.render({'data': data}))
'''