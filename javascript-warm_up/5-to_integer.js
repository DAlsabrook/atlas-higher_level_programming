#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (isNaN(args[2])) {
  console.log('Not a number');
} else {
  const num = parseInt(args[2]);
  console.log('My number: ' + num);
}
