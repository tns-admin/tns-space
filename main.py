import webapp2

import pages

app = webapp2.WSGIApplication([
    ('/', pages.home.RequestHandler),
    ('/clients', pages.clients.RequestHandler),
    ('/client', pages.client.RequestHandler),
    ('/admin', pages.admin.RequestHandler),
], debug=True)
