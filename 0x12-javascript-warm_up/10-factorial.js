#!/usr/bin/node
const { argv } = require('node:process');
function factorial (n) {
  n = parseInt(n);
  if (isNaN(n) || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(argv[2]));
