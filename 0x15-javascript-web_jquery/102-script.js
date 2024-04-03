$('document').ready(function () {
  $('#btn_translate').on('click', function () {
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${$('#language_code').val()}`, function (json) {
      $('#hello').text(json.hello);
    });
  });
});
