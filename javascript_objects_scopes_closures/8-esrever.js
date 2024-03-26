#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  for (const element in list) {
    reversedList.unshift(list[element]);
  }
  return reversedList;
};
