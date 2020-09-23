#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (error, { statusCode }, body) {
  if (error) throw error;
  console.log(`code: ${statusCode}`);
});
