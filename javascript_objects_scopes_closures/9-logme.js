#!/usr/bin/node

let functionCountLogMe = 0;
function logMe(item) {
  console.log(functionCountLogMe + ': ' + item);
  functionCountLogMe += 1;
}
