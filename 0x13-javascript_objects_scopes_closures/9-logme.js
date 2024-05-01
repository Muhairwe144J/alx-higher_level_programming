#!/usr/bin/node

let count = 0; // Initialize a counter for the number of arguments printed

exports.logMe = function (item) {
  console.log(`${count}: ${item}`); // Print the current argument value along with the count
  count++; // Increment the counter
};
