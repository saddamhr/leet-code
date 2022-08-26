const logs = ['d1/', 'd2/', './', 'd3/', '../', 'd31/']; //3

var minOperations = function (logs) {
  const folder = [];
  for (let index = 0; index < logs.length; index++) {
    if (logs[index] !== './') {
      logs[index] !== '../' ? folder.push(logs[index]) : folder.pop();
    }
  }
  return folder.length;
};

console.log(minOperations(logs));
