from tnspy import webenv
import task_main

class RequestHandler(webenv.RequestHandler):
  def get (self):
    response = task_main.RequestHandler().process_request (self.request)
    self.render_response (response)