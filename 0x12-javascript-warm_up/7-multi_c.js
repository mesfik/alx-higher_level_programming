#!/usr/bin/node

const arg = process.argv[2];
const TestNum = parseInt(arg);

if (!isNaN(TestNum)) {
  for (let x = 0; x < TestNum; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
