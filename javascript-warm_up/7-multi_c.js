#!/usr/bin/node

const process = require('process');
const args = process.argv;
const strToPrint = 'C is fun';

if (isNaN(args[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < args[2]; i++) {
    console.log(strToPrint);
  }
}
