#!/usr/bin/node

function factorial (fact) {
  if (fact < 0) {
    return -1;
  } else if (fact === 0) {
    return 1;
  } else {
    return (fact * factorial(fact - 1));
  }
}

const args = process.argv.slice(2);
if (!args[0]) {
  args[0] = 0;
}
const fact = parseInt(args[0]);
console.log(factorial(fact));
