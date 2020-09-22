#!/usr/bin/node

exports.esrever = function (list) {
  return (list.map((value, idx) => list[list.length - 1 - idx]));
};
