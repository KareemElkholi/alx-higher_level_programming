#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length < 4) {
  console.log(0);
} else {
  console.log(argv.filter(Number).sort(function (a, b) { return b - a; })[1]);
}
