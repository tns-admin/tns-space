import logging as log

result = {
  "request": {
    "custom": None,
    "name": None,
    "ref": None,
    "cons": None
  },
  "consultants": {
    1: {"name": "Tatiana Gutu", "initials": "TG"},
    2: {"name": "Svetlana Onofrei", "initials": "SO"},
    3: {"name": "Sergii Romanov", "initials": "SR"}
  },

  "clients": [
    { 
      "id": 1,
      "ref": "TS0001TG",
      "name": "Vasia Pupkin",
      "consultant": 1,
      "projects": [
        {"id": 0, "abbr": "SA", "status": 0},
        {"id": 0, "abbr": "CHB", "status": 1},
      ]
    },
    { 
      "id": 2,
      "ref": "TS0002SO",
      "name": "Victoria Scotch",
      "consultant": 2,
      "projects": [
        {"id": 0, "abbr": "WTC", "status": 0},
        {"id": 0, "abbr": "MAT", "status": 1},
        {"id": 0, "abbr": "SA", "status": 2},
      ]
    },
    {
      "id": 3,
      "ref": "TS0003SR",
      "name": "Ivan Susanin",
      "consultant": 3,
      "projects": [
        {"id": 0, "abbr": "TCC", "status": 1},
        {"id": 0, "abbr": "NINO", "status": 2},
        {"id": 0, "abbr": "OTR", "status": 2},
      ]
    },
  ]
}


def process_request (request):
  name = request.get('name')
  reference = request.get('ref')
  consultant = request.get('cons')

  result ["request"]["custom"] = request.get ("custom")
  result ["request"]["name"] = request.get ("name")
  result ["request"]["ref"] = request.get ("ref")
  result ["request"]["cons"] = int(consultant) if consultant else None

  log.info (result ["request"])

  return result
