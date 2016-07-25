from tnspy import webenv
import client_main

class RequestHandler(webenv.RequestHandler):
  def get (self):
    response = client_main.RequestHandler().process_request (self.request)
    self.render_response (response)