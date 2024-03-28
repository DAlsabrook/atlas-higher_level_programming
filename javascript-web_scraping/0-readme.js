#!/usr/bin/node

const fs = require('fs');
const process = require('process');
const args = process.argv;

if (args[2]) {
  const file = args[2];
  fs.readFile(file, function (err, data) {
    if (err) {
      console.log(err);
    } else {
      console.log(data.toString());
    }
  });
}
