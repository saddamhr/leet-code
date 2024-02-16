// first approach
const getReversedString = (actualString) => {
  if (!actualString) return;
  let reveredString = '';
  for (let i = actualString.length-1; i >= 0; i--) {
    reveredString += actualString[i];
  }
  return reveredString;
};

// second approach
const getReversedString = (actualString) => {
  if (!actualString) return;
  const reveredString = actualString.split('').reverse().join('');
  return reveredString;
};

console.log(getReversedString('hello'));
