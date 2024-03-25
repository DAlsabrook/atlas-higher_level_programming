#!/usr/bin/node

class Rectangle {
  constructor(height, width) {
    if (height > 0) {
      this.height = height;
    }
    if (width > 0) {
      this.width = width;
    }
  }
}

module.exports = Rectangle;
