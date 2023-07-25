#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log(error);
  } else {
    try {
      const movies = JSON.parse(body).results;
      let count = 0;

      for (const movie of movies) {
        if (movie.characters.some(charUrl => charUrl.endsWith('18/'))) {
          count++;
        }
      }
      console.log(count);
    } catch (error) {
      console.log(error);
    }
  }
});
