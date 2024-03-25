#!/usr/bin/node

const args = process.argv.slice(2);
if (!args[0]) {
  args[0] = 0;
}
let largestNum = -Infinity;
let secondLargest = -Infinity;
for (const idx in args) {
  const num = parseInt(args[idx])
  if (num > largestNum) {
    secondLargest = largestNum;
    largestNum = num;
  } else if (num > secondLargest) {
    secondLargest = num;
  }
}
if (args.length === 1) {
  console.log('0');
} else {
  console.log(secondLargest);
}
