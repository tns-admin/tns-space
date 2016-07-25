from tnspy import webenv
import home_main

from tnspy.google_utils import users as google_users

class RequestHandler(webenv.RequestHandler):
  def get (self):
#    self.redirect(google_users.create_login_url(self.request.uri))
    response = home_main.RequestHandler().process_request (self.request)
    self.render_response (response)
