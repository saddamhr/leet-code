const s = 'ab#c';
t = 'ad#c';

const buildString = (string) => {
  const buildString = [];
  for (let p = 0; p < string.length; p++) {
    string[p] !== '#' ? buildString.push(string[p]) : buildString.pop();
  }

  return buildString.join('').toString();
};

var backspaceCompare = function (s, t) {
  const finalS = buildString(s);
  const finalT = buildString(t);

  return finalS === finalT;
};

console.log(backspaceCompare(s, t));
