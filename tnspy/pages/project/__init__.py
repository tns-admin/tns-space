from tnspy import webenv
import project_main

class RequestHandler(webenv.RequestHandler):
  def get (self):
    response = project_main.RequestHandler().process_request (self.request)
    self.render_response (response)