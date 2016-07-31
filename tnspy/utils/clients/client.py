from constants import *

class Client:
  
  def __init__ (self, data):
    self._id                = data ["id"]
    self._reference         = data ["reference"]
    self._consultant        = data ["consultant"]
    self._first_name        = data ["first_name"]
    self._last_name         = data ["last_name"]
    self._dob               = data ["dob"] if "dob" in data else None
    self._marital_status    = date ["marital_status"] if "marital_status" in data else None
    self._marriage_date     = date ["marriage_date"] if "marriage_date" in data else None
    self._nationality       = date ["nationality"] if "nationality" in data else None
    self._uk_entry_date     = date ["uk_entry_date"] if "uk_entry_date" in data else None
    self._address           = date ["address"] if "address" in data else None
    self._post_code         = date ["post_code"] if "post_code" in data else None
    self._address_date_from = date ["address_date_from"] if "address_date_from" in data else None
    self._address_history   = date ["address_history"] if "address_history" in data else None
    self._phone             = date ["phone"] if "phone" in data else None
    self._email             = date ["email"] if "email" in data else None
    self._employment_status = date ["employment_status"] if "employment_status" in data else None
    self._job_title         = date ["job_title"] if "job_title" in data else None
    self._job_start_date    = date ["job_start_date"] if "job_start_date" in data else None
    self._nino              = date ["nino"] if "nino" in data else None
    self._utr               = date ["utr"] if "utr" in data else None
    self._bank_name         = date ["bank_name"] if "bank_name" in data else None
    self._bank_sort_code    = date ["bank_sort_code"] if "bank_sort_code" in data else None
    self._bank_account      = date ["bank_account"] if "bank_account" in data else None
    self._partner_info      = date ["partner_info"] if "partner_info" in data else None
    self._children_info     = date ["children_info"] if "children_info" in data else None
    self._notes             = date ["notes"] if "notes" in data else None


  def id (self):
    return self._id

  def reference (self):
    return self._reference

  def consultant (self):
    return self._consultant

  def first_name (self):
    return self._first_name

  def last_name (self):
    return self._last_name

  def full_name (self):
    return self._first_name + " " + self._last_name

  def dob (self):
    return self._dob

  def marital_status (self):
    return self._marital_status

  def marriage_date (self):
    return self._marriage_date

  def nationality (self):
    return self._nationality

  def uk_entry_date (self):
    return self._uk_entry_date

  def address (self):
    return self._address

  def post_code (self):
    return self._post_code

  def address_date_from (self):
    return self._address_date_from

  def address_history (self):
    return self._address_history

  def phone (self):
    return self._phone

  def email (self):
    return self._email

  def employment_status (self):
    return self._employment_status

  def job_title (self):
    return self._job_title

  def job_start_date (self):
    return self._job_start_date

  def nino (self):
    return self._nino

  def utr (self):
    return self._utr

  def bank_name (self):
    return self._bank_name

  def bank_sort_code (self):
    return self._bank_sort_code

  def bank_account (self):
    return self._bank_account

  def partner_info (self):
    return self._partner_info

  def children_info (self):
    return self._children_info

  def notes (self):
    return self._notes
