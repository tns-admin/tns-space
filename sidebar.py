import webapp2

def process_request (request):
    return {
        'current_page': request.get('page','dashboard'),
        'pages': [
            {'page': 'dashboard', 'text': "Dashboard", 'url': '/?page=dashboard'},
            {'page': 'users',     'text': "Users",     'url': '/?page=users'},
            {'page': 'clients',   'text': "Clients",   'url': '/?page=clients'}
        ]
    }
