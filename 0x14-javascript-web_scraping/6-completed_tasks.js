#!/usr/bin/node

const request = require('request');
const process = require('process');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log('error:', response.statusCode);
  } else {
    try {
      const file = JSON.parse(body);
      const taskCompleted = {};
      for (const task of file) {
        if (task.completed) {
          if (!taskCompleted[task.userId]) {
            taskCompleted[task.userId] = 0;
          }
          taskCompleted[task.userId]++;
        }
      }
      console.log(taskCompleted);
    } catch (error) {
      console.log(error);
    }
  }
});
