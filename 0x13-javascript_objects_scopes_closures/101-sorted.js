#!/usr/bin/node

const { dict } = require('./101-data'); // Import the dict from 101-data.js

const occurrencesByUserId = {};

// Iterate through the original dict
for (const userId in dict) {
  const occurrences = dict[userId];
  if (!occurrencesByUserId[occurrences]) {
    occurrencesByUserId[occurrences] = [];
  }
  occurrencesByUserId[occurrences].push(userId);
}

console.log(occurrencesByUserId);
