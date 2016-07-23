import logging as log

from google.appengine.api import users as gusers

import admin_users

admin_pages = {
  'users':    {'text': "Users", 'request_handler': admin_users.process_request},
}

def generate_sidebar_data (current_page):
  # ordered list of visible pages
  visible_pages = ['users']

  pages = []
  for page in visible_pages:
    page_entry = {'page': page,
                  'text': admin_pages [page] ['text'],
                  'url' : '/admin?page=' + page}
    pages.append (page_entry)

  return {'current_page': current_page, "pages": pages}

class RequestHandler:

  def process_request (self, request):
    page = request.get('page', 'users')
    data = {
      'user': gusers.get_current_user(),
      'body_template': "/templates/admin/admin_" + page + ".html",
      'sidebar': generate_sidebar_data (page)
    }

    #log.error (admin_pages [page])

    data [page] = (admin_pages [page] ['request_handler']) (request)

    return {"template": "admin/admin.html", "data": data}