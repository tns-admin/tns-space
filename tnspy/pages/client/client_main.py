#import os
#import urllib
import jinja2
import webapp2
import logging as log

from tnspy.utils import users
from tnspy.pages import header as header_page

import client_general
import client_personal
import client_agreements
import client_projects

client_pages = {
  'general':    {'text': "General", 'request_handler': client_general.process_request},
  'personal':   {'text': "Personal", 'request_handler': client_personal.process_request},
  'agreements': {'text': "Agreements", 'request_handler': client_agreements.process_request},
  'projects': {'text': "Projects", 'request_handler': client_projects.process_request}
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
      'header': header_page.process_request (request),
      'client_id': client_id,
      'body_template': "/templates/client/client_" + page + ".html",
      'sidebar': generate_sidebar_data (page)
    }

    #log.error (client_pages [page])

    data [page] = (client_pages [page] ['request_handler']) (request)

    return {"template": "client/client.html", "data": data}
