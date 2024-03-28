#!/usr/bin/node

const request = require('request');
const process = require('process');
const args = process.argv;

if (args[2]) {
  request(args[2], function (error, response, body) {
    if (error) {
      console.log(`Error: ${error}`);
    }
    console.log(`Code: ${response.statusCode}`);
  });
}
