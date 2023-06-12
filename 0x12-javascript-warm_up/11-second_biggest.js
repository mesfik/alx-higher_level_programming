#!/usr/bin/node

const arglen = process.argv.length;

if (arglen <= 3) {
  console.log(0);
} else {
  const secondbig = process.argv.slice(2).map(Number).sort((a, b) => b - a);
  console.log(secondbig[1]);
}
