import logging as log

from tnspy.pages import header as header_page

import projects_search
import projects_create

pages = {
  'search':    {'text': "Search", 'request_handler': projects_search.process_request},
  'create':   {'text': "New Project", 'request_handler': projects_create.process_request},
}

class RequestHandler:

  def process_request (self, request):
    client_id = request.get('id')
    page = request.get('page', 'search')

    data = {
      'header': header_page.process_request (request),
      'client_id': client_id,
      'body_template': "/templates/projects/projects_" + page + ".html"
    }

    data ["page"] = (pages [page] ['request_handler']) (request)

    return {"template": "projects/projects.html", "data": data}
