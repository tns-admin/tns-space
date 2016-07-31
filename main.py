import webapp2

from tnspy import pages
from tnspy import ajax

app = webapp2.WSGIApplication([
    ('/',         pages.home.RequestHandler),
    ('/ajax',     ajax.RequestHandler),
    ('/clients',  pages.clients.RequestHandler),
    ('/client',   pages.client.RequestHandler),
    ('/projects', pages.projects.RequestHandler),
    ('/project',  pages.project.RequestHandler),
    ('/tasks',    pages.tasks.RequestHandler),
    ('/task',     pages.task.RequestHandler),
    ('/admin',    pages.admin.RequestHandler),
], debug=True)
