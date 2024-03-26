#!/usr/bin/node

var functionCountLogMe = 0;
exports.logMe = function (item) {
  console.log(functionCountLogMe + ': ' + item);
  functionCountLogMe += 1;
}
