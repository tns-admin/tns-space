from tnspy import webenv
import projects_main

class RequestHandler(webenv.RequestHandler):
  def get (self):
    response = projects_main.RequestHandler().process_request (self.request)
    self.render_response (response)