import logging as log

from tnspy.pages import header as header_page

import project_home
import project_tasks
import project_attachments

pages = {
  'home':    {'text': "Home", 'request_handler': project_home.process_request},
  'tasks':   {'text': "Tasks", 'request_handler': project_tasks.process_request},
  'attachments':   {'text': "Attachments", 'request_handler': project_attachments.process_request},
}

class RequestHandler:

  def process_request (self, request):
    client_id = request.get('id')
    page = request.get('page', 'home')

    data = {
      'header': header_page.process_request (request),
      'client_id': client_id,
      'body_template': "/templates/project/project_" + page + ".html",
    }

    #log.error (pages [page])

    data ["page"] = (pages [page] ['request_handler']) (request)

    return {"template": "project/project.html", "data": data}
