

USER_STATUS_INVALID   = 0
USER_STATUS_ACTIVE    = 1
USER_STATUS_INACTIVE  = 2

USER_STATUS_MAP = {
  USER_STATUS_INVALID:  "INVALID",
  USER_STATUS_ACTIVE:   "ACTIVE",
  USER_STATUS_INACTIVE: "INACTIVE"
}

USER_ROLE_NONE    = 0
USER_ROLE_ADMIN   = 1
USER_ROLE_USER    = 2

USER_ROLE_MAP = {
  USER_ROLE_NONE:  "NONE",
  USER_ROLE_ADMIN: "ADMIN",
  USER_ROLE_USER:  "USER"
}

def status_to_str (status):
  if status in USER_STATUS_MAP:
    return USER_STATUS_MAP [status]
  else:
    return None


def status_from_str (status_str):
  for key, val in USER_STATUS_MAP:
    if val == status_str:
      return key
  return None

def role_to_str (role):
  if role in USER_ROLE_MAP:
    return USER_ROLE_MAP [role]
  else:
    return None


def role_from_str (role_str):
  for key, val in USER_ROLE_MAP:
    if val == role_str:
      return key
  return None
