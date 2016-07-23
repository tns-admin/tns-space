import webenv
import admin_main

class RequestHandler(webenv.RequestHandler):
  def get (self):
    response = admin_main.RequestHandler().process_request (self.request)
    self.render_response (response)