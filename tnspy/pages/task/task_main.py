import logging as log

from tnspy.pages import header as header_page

import task_home
import task_attachments

pages = {
  'home':    {'text': "Home", 'request_handler': task_home.process_request},
  'attachments':   {'text': "Attachments", 'request_handler': task_attachments.process_request},
}

class RequestHandler:

  def process_request (self, request):
    client_id = request.get('id')
    page = request.get('page', 'home')

    data = {
      'header': header_page.process_request (request),
      'client_id': client_id,
      'body_template': "/templates/task/task_" + page + ".html",
    }

    #log.error (pages [page])

    data ["page"] = (pages [page] ['request_handler']) (request)

    return {"template": "task/task.html", "data": data}
