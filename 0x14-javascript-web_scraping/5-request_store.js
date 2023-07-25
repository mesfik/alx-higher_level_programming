#!/usr/bin/node

const request = require('request');
const process = require('process');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request.get(url, (error, response) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log('error:', response.statusCode);
  } else {
    fs.writeFile(file, response.body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
