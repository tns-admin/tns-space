import logging as log

from pytns.utils import users
from pytns.pages import header as header_page

import admin_users
import admin_add_user
import admin_user_profile

admin_pages = {
  'users':       {'text': "Users", 'request_handler': admin_users.process_request},
  'add_user':    {'text': "Add User", 'request_handler': admin_add_user.process_request},
  'user_profile':{'text': "User Profile", 'request_handler': admin_user_profile.process_request},
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
      'header': header_page.process_request (request),
      'body_template': "/templates/admin/admin_" + page + ".html",
      'sidebar': generate_sidebar_data (page)
    }

    #log.error (admin_pages [page])

    data [page] = (admin_pages [page] ['request_handler']) (request)

    return {"template": "admin/admin.html", "data": data}

