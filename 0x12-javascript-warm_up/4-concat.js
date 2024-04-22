#!/usr/bin/node
const args = process.argv.slice(2); // Get arguments excluding script name

if (args.length < 2) {
  console.log('undefined is undefined');
} else {
  console.log(`${args[0]} is ${args[1]}`);
}
