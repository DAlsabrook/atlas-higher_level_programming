#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  if (!list && !searchElement) {
    return 0;
  }

  for (const element in list) {
    if (list[element] === searchElement) {
      counter += 1;
    }
  }
  return counter;
};
