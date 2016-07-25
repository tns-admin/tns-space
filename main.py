import webapp2

from pytns import pages
from pytns import ajax

app = webapp2.WSGIApplication([
    ('/', pages.home.RequestHandler),
    ('/ajax', ajax.RequestHandler),
    ('/clients', pages.clients.RequestHandler),
    ('/client', pages.client.RequestHandler),
    ('/admin', pages.admin.RequestHandler),
], debug=True)
