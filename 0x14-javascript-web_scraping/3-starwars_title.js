#!/usr/bin/node

const request = require('request');
const process = require('process');

const urlId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${urlId}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(response.name);
  } else if (response.statusCode !== 200) {
    console.log(error);
  } else {
    try {
      const movies = JSON.parse(body);
      console.log(movies.title);
    } catch (error) {
      console.log(error);
    }
  }
});
