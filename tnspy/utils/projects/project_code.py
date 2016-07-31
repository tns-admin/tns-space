
class ProjectCode:
  _codes = {
    1: { 'abbr': 'SA', 'title': 'Self Assessment' },
    2: { 'abbr': 'CB', 'title': 'Child Benefits' },
    3: { 'abbr': 'ATR', 'title': 'Annual Tax Return' },
    4: { 'abbr': 'MSC', 'title': 'Miscellaneous Project' }
  }

  def __init__ (self, code_id):
    if code_id in self._codes:
      self._id = code_id
      self._abbr = self._codes [code_id] ["abbr"]
      self._title = self._codes [code_id] ["title"]
    else:
      raise Exception ("Invalid project code " + code_id)

  def id (self):
    return self._id

  def abbr (self):
    return self._abbr

  def title (self):
    return self._title


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# global functions
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def get_all_project_codes ():
  result = []
  for code_id in ProjectCode._codes:
    result.append (ProjectCode (code_id))
  return result


