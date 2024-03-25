#!/usr/bin/node

const args = process.argv.slice(2);
if (!args[0]) {
  args[0] = 0;
}
let largestNum = -Infinity;
let secondLargest = -Infinity;
for (const idx in args) {
  if (args[idx] > largestNum) {
    secondLargest = largestNum;
    largestNum = args[idx];
  }
}
if (args.length === 1) {
  console.log('0');
} else {
  console.log(secondLargest);
}
