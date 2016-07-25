
from constants import *

class User:
  def __init__(self,
               id         = None,
               email      = None,
               first_name = None,
               last_name  = None,
               role       = None,
               status     = None,
               picture    = None):
    self._id         = id
    self._email      = email
    self._status     = status
    self._role       = role
    self._first_name = first_name
    self._last_name  = last_name
    self._picture    = picture

  def id (self):
    return self._id

  def email (self):
    return self._email

  def status (self):
    return self._status

  def first_name (self):
    return self._first_name

  def last_name (self):
    return self._last_name

  def full_name (self):
    return self._first_name + ' ' + self._last_name

  def picture (self):
    return self._picture

  def role (self):
    return self._role

  def is_active (self):
    return self._status == USER_STATUS_ACTIVE


