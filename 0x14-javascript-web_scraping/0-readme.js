#!/usr/bin/node
const file = require('fs');

file.readFile(process.argv[2], (err, data) => {
  if (err) {
    throw err;
  }

  console.log(data.toString());
});
