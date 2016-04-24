import os
#import MySQLdb

from google.appengine.api import users

import jinja2
import webapp2

def process_request (request):
    user = users.get_current_user ()
    return {
        'all_users': [
            {'id': 1, 'name': user.nickname (), 'email': user.email ()},
            {'id': 2, 'name': 'Full Name', 'email': 'email@tnstax.co.uk'}
        ]
    }
