#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const width = this.width;
    const height = this.height;
    const strToPrint = 'X'.repeat(width);
    for (let row = 0; row < height; row++) {
      console.log(strToPrint);
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= this.width;
    this.height *= this.height;
  }
}

module.exports = Rectangle;
