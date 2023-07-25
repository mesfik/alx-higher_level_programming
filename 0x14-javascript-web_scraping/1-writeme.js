#!/usr/bin/node

const process = require('process');
const fs = require('fs');

const file = process.argv[2];
const data = process.argv[3];

fs.writeFile(file, data, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
