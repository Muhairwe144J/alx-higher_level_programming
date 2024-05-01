#!/usr/bin/node

const { list } = require('./100-data'); // Import the list from 100-data.js

const newList = list.map((value, index) => value * index);

console.log(list);
console.log(newList);
