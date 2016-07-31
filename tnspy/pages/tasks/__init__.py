from tnspy import webenv
import tasks_main

class RequestHandler(webenv.RequestHandler):
  def get (self):
    response = tasks_main.RequestHandler().process_request (self.request)
    self.render_response (response)