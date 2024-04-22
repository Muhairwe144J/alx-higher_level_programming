#!/usr/bin/node
const args = process.argv.slice(2).map(Number); // Convert arguments to numbers

if (args.length === 0) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  const sorted = args.sort((a, b) => b - a); // Sort in descending order
  console.log(sorted[1] || 0); // Get the second element or 0 if not found
}
