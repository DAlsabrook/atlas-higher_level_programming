#!/usr/bin/node
const process = require('process');
const args = process.argv;

if (!args[2]) {
  args[2] = 'undefined';
}
if (!args[3]) {
  args[3] = 'undefined';
}
if (args.length === 4) {
  console.log(args[2] + ' is ' + args[3]);
}
