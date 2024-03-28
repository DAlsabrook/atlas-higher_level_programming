#!/usr/bin/node

const fs = require("fs");
process = require('process');
args = process.argv;

if (args[2]) {
  file = args[2];
  buffer = '';
  fs.readFile(file, function (err, data) {
    if (err) {
      console.log(err);
    } else {
      console.log(data.toString());
    }
    });
}
