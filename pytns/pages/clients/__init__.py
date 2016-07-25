from pytns import webenv
import clients_main

class RequestHandler(webenv.RequestHandler):
  def get (self):
    response = clients_main.RequestHandler().process_request (self.request)
    self.render_response (response)