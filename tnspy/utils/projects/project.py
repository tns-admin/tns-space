from constants import *

class Project:
  def __init__ (self, data):
    self._id                = data ['id']
    self._code              = data ['code']
    self._title             = data ['title']
    self._description       = data ['description']
    self._client_id         = data ['client_id'] if 'client_id' in data else None
    self._owner_id          = data ['owner_id']
    self._creator_id        = data ['creator_id']
    self._created_timestamp = data ['created_timestamp']
    self._due_date          = data ['due_date'] if 'due_date' in data else None
    self._status            = data ['status']
    self._attachments       = []

  def id (self):
    return self._id

  def code (self):
    return self._code

  def title (self):
    return self._title

  def description (self):
    return self._description

  def client_id (self):
    return self.cliend_id

  def owner_id (self):
    return self._owner_id

  def creator_id (self):
    return self._creator_id

  def created_timestamp (self):
    return self._created_timestamp

  def due_date (self):
    return self._due_date

  def status (self):
    return self._status

  def attachments (self):
    return self._attachments
