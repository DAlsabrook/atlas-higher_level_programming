#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

if (apiUrl) {
  request(apiUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const films = JSON.parse(response.body).results;
      let count = 0;

      films.forEach(film => {
        film.characters.forEach(url => {
          if (url.includes('/18/')) {
            count++;
          }
        });
      });
      console.log(count);
    }
  });
}

