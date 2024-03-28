#!/usr/bin/node

const fs = require('fs');
const process = require('process');
const args = process.argv;

if (args[2] && args[3]) {
  const file = args[2];
  const str = args[3];
  fs.writeFile(file, str, function (err, data) {
    if (err) {
      console.log(err);
    }
  });
}
