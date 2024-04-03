$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (json) {
  $.each(json.results, function (i, movie) {
    $('#list_movies').append(`<li>${movie.title}</li>`);
  });
});
