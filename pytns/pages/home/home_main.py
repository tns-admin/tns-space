import logging as log

from pytns.utils import users

from pytns.pages import header as header_page

import home_dashboard

admin_pages = {
  'dashboard':    {'text': "Dashboard", 'request_handler': home_dashboard.process_request}
}

def generate_sidebar_data (current_page):
  # ordered list of visible pages
  visible_pages = ['dashboard']

  pages = []
  for page in visible_pages:
    page_entry = {'page': page,
                  'text': admin_pages [page] ['text'],
                  'url' : '/?page=' + page}
    pages.append (page_entry)

  return {'current_page': current_page, "pages": pages}

class RequestHandler:

  def process_request (self, request):
    page = request.get('page', 'dashboard')
    data = {
      'header': header_page.process_request (request),
      'body_template': "/templates/home/home_" + page + ".html",
      'sidebar': generate_sidebar_data (page)
    }

    #log.error (admin_pages [page])

    data [page] = (admin_pages [page] ['request_handler']) (request)

    return {"template": "home/home.html", "data": data}
