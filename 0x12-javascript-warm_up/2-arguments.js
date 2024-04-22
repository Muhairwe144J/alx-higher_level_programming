#!/usr/bin/node

const argsLength = process.argv.length; // Get arguments excluding script name

if (argsLength === 0) {
  console.log('No argument');
} else if (argsLength === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
