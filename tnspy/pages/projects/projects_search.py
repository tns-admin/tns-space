import tnspy.utils.projects as tns_projects
from tnspy.utils.users import Database as users_db

import logging as log

def process_request (request):
  users = users_db ().get_all_users ()
  projects = tns_projects.Database ().get_all_projects ()

  result = {}
  result ['projects'] = []
  for project in projects:
    item = {
      "id": project.id (),
      "code": tns_projects.ProjectCode (project.code ()).abbr (),
      "title": project.title (),
      "client": 0,
      "owner": project.owner_id (),
      "status": tns_projects.project_status_to_str (project.status ()),
      "due_date": project.due_date ()
    }

    result ['projects'].append (item)

  result ["users"] = {}
  for user in users:
    result ["users"] [user.id ()] = user.full_name ()

  result ["project_codes"] = tns_projects.get_all_project_codes ()

  return result

  
