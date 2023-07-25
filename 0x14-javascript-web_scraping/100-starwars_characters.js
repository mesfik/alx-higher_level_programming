#!/usr/bin/node
// prints all characters of a Star Wars movie
const request = require('request');
const url = 'https://swapi.dev/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const filmData = JSON.parse(body);
    for (const character of filmData.characters) {
      request(character, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          const charData = JSON.parse(body);
          console.log(charData.name);
        }
      });
    }
  }
});
