#!/usr/bin/node
const request = require('request');
request.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, function (error, response, body) {
  if (error === null) {
    const { title } = JSON.parse(body);
    console.log(title);
  } else {
    console.log(error);
  }
});
