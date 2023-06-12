#!/usr/bin/node

let firstArg = 0;

for (let i = 2; process.argv[i]; i++) {
  firstArg++;
  if (firstArg === 1) {
    console.log(process.argv[i]);
  }
}
if (firstArg === 0) {
  console.log('No argument');
}
