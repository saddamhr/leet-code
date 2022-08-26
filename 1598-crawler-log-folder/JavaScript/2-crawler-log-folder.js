const logs = ['d1/', 'd2/', './', 'd3/', '../', 'd31/']; //3

var minOperations = function (logs) {
  let count = 0;
  for (let index = 0; index < logs.length; index++) {
    if (logs[index] === './') continue;
    logs[index] !== '../' ? count++ : (count = Math.max(0, count - 1));
  }
  return count;
};

console.log(minOperations(logs));
