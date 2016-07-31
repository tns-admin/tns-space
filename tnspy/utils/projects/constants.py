
PROJECT_STATUS_INVALID     = 0
PROJECT_STATUS_SUSPENDED   = 1
PROJECT_STATUS_IN_PROGRESS = 2
PROJECT_STATUS_COMPLETED   = 3
PROJECT_STATUS_CANCELED    = 4


PROJECT_STATUS_MAP = {
  PROJECT_STATUS_INVALID:     "INVALID",
  PROJECT_STATUS_SUSPENDED:   "SUSPENDED",
  PROJECT_STATUS_IN_PROGRESS: "SUSPENDED",
  PROJECT_STATUS_COMPLETED:   "COMPLETED",
  PROJECT_STATUS_CANCELED:    "CANCELED"
}


def project_status_to_str (status):
  if status in PROJECT_STATUS_MAP:
    return PROJECT_STATUS_MAP [status]
  else:
    return None


def project_status_from_str (status_str):
  for key, val in PROJECT_STATUS_MAP:
    if val == status_str:
      return key
  return None
