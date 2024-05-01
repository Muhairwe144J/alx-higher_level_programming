#!/usr/bin/node

const Rectangle = require('./4-rectangle'); // Import the Rectangle class

class Square extends Rectangle {
  constructor(size) {
    super(size, size); // Call the constructor of Rectangle with the same size for width and height
  }

  charPrint(c) {
    if (c === undefined) {
      c = 'X'; // Default character is 'X'
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square; // Export the Square class
