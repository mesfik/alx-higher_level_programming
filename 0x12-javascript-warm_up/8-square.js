#!/usr/bin/node

const arg = process.argv[2];
const size = parseInt(arg);

if (!isNaN(size)) {
  for (let x = 0; x < size; x++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
