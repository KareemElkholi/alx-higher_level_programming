#!/usr/bin/node
const newDict = {};
const dict = require('./101-data.js').dict;
for (const [k, v] of Object.entries(dict)) {
  if (!newDict[v]) {
    newDict[v] = [k];
  } else {
    newDict[v][newDict[v].length] = k;
  }
}
console.log(newDict);
