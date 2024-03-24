#!/usr/bin/node

const process = require('process');
const args = process.argv;
let arg = 0;
for (arg in args) {
  if (arg > 1) {
    console.log(args[arg]);
  }
}
if (arg < 2) {
  console.log('No argument');
}
