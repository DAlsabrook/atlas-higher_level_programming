#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const args = process.argv;
const api = args[2];
const file = args[3];

if (!api || !file) {
  process.exit(1);
}

request(api, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    process.exit(1);
  }
  fs.writeFile(file, body, function (err, body) {
    if (err) {
      console.log(err);
    }
  });
});
