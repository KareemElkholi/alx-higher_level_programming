$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (json) {
  $('#hello').text(json.hello);
});
