#!/usr/bin/node

const request = require('request');
const process = require('process');

const url = `https://jsonplaceholder.typicode.com/todos`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    try {
      const tasks = JSON.parse(body);
      const taskCompleted = {};
      for (const task of tasks) {
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
