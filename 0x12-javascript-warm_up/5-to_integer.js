#!/usr/bin/node

const arg = process.argv[2];
const TestNum = parseInt(arg);

if (!isNaN(TestNum)) {
  console.log('My number: ' + TestNum);
} else {
  console.log('Not a number');
}
