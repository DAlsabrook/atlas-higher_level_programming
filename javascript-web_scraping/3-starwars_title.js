#!/usr/bin/node

const process = require('process');
const request = require('request');
const args = process.argv;
episodeNumber = args[2];
baseUrl = "https://swapi-api.hbtn.io/api/films/";

if (episodeNumber)  {
  api = baseUrl + episodeNumber;
  request(api, function (error, response, body) {
    if (!error && response.statusCode == 200) {
      const data = JSON.parse(response.body);
      console.log(data.title);
    }
  })
}
