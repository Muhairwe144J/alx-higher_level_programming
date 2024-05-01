#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: node 102-concat.js <fileA> <fileB> <fileC>');
  process.exit(1);
}

const [, , fileA, fileB, fileC] = process.argv;

try {
  const contentA = fs.readFileSync(fileA, 'utf8');
  const contentB = fs.readFileSync(fileB, 'utf8');
  const concatenatedContent = contentA + '\n' + contentB;
  fs.writeFileSync(fileC, concatenatedContent);
  console.log(`Concatenated ${fileA} and ${fileB} into ${fileC}`);
} catch (error) {
  console.error('Error:', error.message);
  process.exit(1);
}
