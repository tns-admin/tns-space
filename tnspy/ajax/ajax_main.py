import ajax_users

def process_request (request):
  request_id = request.get ("request_id")
  reqs = request_id.split ('.')
  module = reqs[0]
  if (module == "users"):
    return ajax_users.process_request (request)
  else:
    return {msg: "Invelid request_id"}