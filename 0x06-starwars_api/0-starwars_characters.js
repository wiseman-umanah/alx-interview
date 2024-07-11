#!/usr/bin/node
const request = require('request');
const process = require('process');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

request(url, (error, response, body) => {
  if (error) console.log(error);

  const characters = JSON.parse(body).characters;
  const promises = characters.map(charUrl => {
    return new Promise((resolve, reject) => {
      request(charUrl, (error, response, body) => {
        if (error) reject(error);
        else {
          const characterName = JSON.parse(body).name;
          resolve(characterName);
        }
      });
    });
  });
  Promise.all(promises)
    .then(names => {
      names.forEach(name => console.log(name));
    });
});
