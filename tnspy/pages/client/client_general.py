
result = {
  "consultants": {
    1: {"name": "Tatiana Gutu", "initials": "TG"},
    2: {"name": "Svetlana Onofrei", "initials": "SO"},
    3: {"name": "Sergii Romanov", "initials": "SR"}
  },
  "client_name": "Ivan Susanin",
  "consultant": 1,
  "reference": "TS00003TG",
  "projects": [
    {"id": 0, "title": "Self-Assessment 2015", "status": "In progress"},
    {"id": 0, "title": "Child Benefits", "status": "Overdue"},
    {"id": 0, "title": "Annual tax return 2016", "status": "Completed"}
  ],
  "total_projects": 4,
  "payments": {
    "xero_id": "000X0000",
    "total_invoices": 16,
    "unpaid_invoices": 3,
    "overdue_invoices": 1
  },
  "notes": [
    {
      "user_name": "Svetlana Onofrei",
      "timestamp": "18/01/2016",
      "text": "Project specific notes should go to the corresponding project. Same for tasks. Only general client notes should be here."
    },
    {
      "user_name": "Sergii Romanov",
      "timestamp": "18/01/2016",
      "text": "This client needs WTC and Child Benefits. Maybe Annual Tax return"
    },
    {
      "user_name": "Sergii Romanov",
      "timestamp": "18/01/2016",
      "text": "Notes cannot be edited. All corrections must come as followup notes"
    },
    {
      "user_name": "Tatiana Gutu",
      "timestamp": "18/01/2016",
      "text": "Maybe add notes here"
    }
  ]
}


def process_request (request):
    return result
