#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const size = this.width;
    let char = 'X';
    if (c) {
      char = c;
    }
    const rowToPrint = char.repeat(size);
    for (let row = 0; row < size; row++) {
      console.log(rowToPrint);
    }
  }
}

module.exports = Square;
