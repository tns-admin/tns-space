from pytns import webenv
import header_main

class RequestHandler(webenv.RequestHandler):
  def get (self):
    response = header_main.RequestHandler().process_request (self.request)
    self.render_response (response)