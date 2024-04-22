#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
  incr() { // Method to increment value (using arrow function for brevity)
    return { // Return a new object to preserve immutability
      ...this, // Spread operator to copy existing properties
      value: this.value + 1
    };
  }
};

console.log(myObject); // { type: 'object', value: 12 }

const incrementedObject1 = myObject.incr();
console.log(incrementedObject1); // { type: 'object', value: 13 } (new object)
console.log(myObject); // { type: 'object', value: 12 } (original object remains unchanged)

const incrementedObject2 = incrementedObject1.incr();
console.log(incrementedObject2); // { type: 'object', value: 14 } (another new object)
console.log(incrementedObject1); // { type: 'object', value: 13 } (unchanged)
console.log(myObject);           // { type: 'object', value: 12 } (unchanged)
