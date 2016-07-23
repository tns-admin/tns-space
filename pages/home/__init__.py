import webenv
import home_main

class RequestHandler(webenv.RequestHandler):
  def get (self):
    response = home_main.RequestHandler().process_request (self.request)
    self.render_response (response)