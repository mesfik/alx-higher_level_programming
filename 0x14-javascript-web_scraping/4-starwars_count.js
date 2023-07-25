#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log('error:', response.statusCode);
  } else {
    try {
      const movies = JSON.parse(body).results;
      let count = 0;

      for (const movie of movies) {
        if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
          count++;
        }
      }
      console.log(count);
    } catch (error) {
      console.log(error);
    }
  }
});
