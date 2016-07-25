from pytns import webenv
import ajax_main

class RequestHandler(webenv.RequestHandler):
  def get (self):
    response = ajax_main.process_request (self.request)
    self.render_ajax_response (response)

  def post (self):
    response = ajax_main.process_request (self.request)
    self.render_ajax_response (response)
