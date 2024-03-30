$(document).ready(() => {
  $.get("https://swapi-api.hbtn.io/api/films/?format=json", (data) => {
    const films = data.results;
    films.forEach(film => {
      const title = film.title;
      $('ul#list_movies').append('<li>' + title + '</li>')
    });
  });
});
