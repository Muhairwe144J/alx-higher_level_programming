#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject); // { type: 'object', value: 12 }

// Create a new object with the updated value
const updatedObject = {
  ...myObject, // Spread operator to copy properties
  value: 89
};

console.log(updatedObject); // { type: 'object', value: 89 }
