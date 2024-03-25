#!/usr/bin/node

class Rectangle {
  constructor(h, w) {
    if (h > 0) {
      this.height = h;
    }
    if (w > 0) {
      this.width = w;
    }
  }
}

module.exports = Rectangle;
