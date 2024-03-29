#!/usr/bin/node

const args = process.argv;
const apiUrl = args[2];
const request = require('request');

request(apiUrl, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    process.exit(1);
  }
  const userDict = {};
  const taskList = JSON.parse(response.body);
  taskList.forEach(task => {
    if (task.completed === true) {
      if (!userDict[task.userId]) {
        userDict[task.userId] = 0;
      }
      userDict[task.userId] += 1;
    }
  });
  console.log(userDict);
});
