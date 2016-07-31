import logging as log

from tnspy.pages import header as header_page

import tasks_search
import tasks_create

pages = {
  'search':   {'text': "Search", 'request_handler': tasks_search.process_request},
  'create':   {'text': "Create New Task", 'request_handler': tasks_create.process_request},
}

class RequestHandler:

  def process_request (self, request):
    task_id = request.get('id')
    page = request.get('page', 'search')

    data = {
      'header': header_page.process_request (request),
      'task_id': task_id,
      'body_template': "/templates/tasks/tasks_" + page + ".html"
    }

    data ["page"] = (pages [page] ['request_handler']) (request)

    return {"template": "tasks/tasks.html", "data": data}
