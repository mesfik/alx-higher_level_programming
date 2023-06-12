#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  const newnum = number + 1;
  theFunction(newnum);
};
