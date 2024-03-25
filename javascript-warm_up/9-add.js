#!/usr/bin/node

function add (numOne, numTwo) {
  return numOne + numTwo;
}

const args = process.argv.slice(2);
const numOne = parseInt(args[0]);
const numTwo = parseInt(args[1]);
const result = add(numOne, numTwo);
console.log(result);
