$('document').ready(function () {
  $('#btn_translate').on('click', translate);
  $('#language_code').keyup(function (event) {
    if (event.keyCode === 13) {
      translate();
    }
  });
});
function translate () {
  $.get(`https://hellosalut.stefanbohacek.dev/?lang=${$('#language_code').val()}`, function (json) {
    $('#hello').text(json.hello);
  });
}
