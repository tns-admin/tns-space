import logging as log

from google.appengine.api import users as gusers

from utils.users import validate_current_user

import clients_search
import clients_create

client_pages = {
  'search':    {'text': "Search", 'request_handler': clients_search.process_request},
  'create':   {'text': "Create New Client", 'request_handler': clients_create.process_request},
}

def generate_sidebar_data (current_page):
  # ordered list of visible pages
  visible_pages = ['search', 'create']

  pages = []
  for page in visible_pages:
    page_entry = {'page': page,
                  'text': client_pages [page] ['text'],
                  'url' : '/clients?page=' + page}
    pages.append (page_entry)

  return {'current_page': current_page, "pages": pages}

class RequestHandler:

  def process_request (self, request):
    page = request.get('page', 'search')
    data = {
      'user': gusers.get_current_user(),
      'body_template': "/templates/clients/clients_" + page + ".html",
      'sidebar': generate_sidebar_data (page)
    }

    #log.error (client_pages [page])

    data [page] = (client_pages [page] ['request_handler']) (request)

    return {"template": "clients/clients.html", "data": data}
