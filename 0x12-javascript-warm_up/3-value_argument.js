#!/usr/bin/node
const arg = process.argv[2]; // Get the first argument (index 2)

if (!arg) {
  console.log("No argument");
} else {
  console.log(arg);
}
