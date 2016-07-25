g_prev_values = {}

function edit_get_prev_value (field_name) {
  return g_prev_values [field_name];
}

function edit_field_changed (field_name) {
  document.getElementById(field_name).value == g_prev_values [field_name];
}

function edit_page_enable () {
  $(".edit-field-enable-btn").show ();
  $("#edit-page-enable-btn").hide ();
  $("#edit-page-disable-btn").show ();
}

function edit_page_disable () {
  $(".edit-field-enable-btn").hide ();
  $("#edit-page-disable-btn").hide ();
  $("#edit-page-enable-btn").show ();
}

function edit_enable (field_name) {
  document.getElementById(field_name).disabled = false;
  g_prev_values [field_name] = document.getElementById(field_name).value;

  $("#" + field_name + "-edit-btn").hide ();
  $("#" + field_name + "-save-btn").show ();
  $("#" + field_name + "-cancel-btn").show ();
}

function edit_cancel (field_name) {
  document.getElementById(field_name).disabled = true;
  document.getElementById(field_name).value = g_prev_values [field_name];

  $("#" + field_name + "-edit-btn").show ();
  $("#" + field_name + "-save-btn").hide ();
  $("#" + field_name + "-cancel-btn").hide ();
}

function edit_save_finish (field_name, success) {
  if (!success) {
    document.getElementById(field_name).value = g_prev_values [field_name];
  }

  document.getElementById(field_name).disabled = true;

  $("#" + field_name + "-edit-btn").show ();
  $("#" + field_name + "-save-btn").hide ();
  $("#" + field_name + "-cancel-btn").hide ();
}