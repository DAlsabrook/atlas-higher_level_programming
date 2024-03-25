#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  const strToPrint = 'X'.repeat(size);
  for (let row = 0; row < size; row++) {
    console.log(strToPrint);
  }
}
