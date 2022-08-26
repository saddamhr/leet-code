const s = 'ab#c';
t = 'ad#c';

const buildString = (string) => {
  const buildString = [];
  for (let p = 0; p < string.length; p++) {
    string[p] !== '#' ? buildString.push(string[p]) : buildString.pop();
  }
  return buildString;
};

var backspaceCompare = function (s, t) {
  const finalS = buildString(s);
  const finalT = buildString(t);

  if (finalS.length !== finalT.length) {
    return false;
  } else {
    for (let p = 0; p < finalS.length; p++) {
      if (finalS[p] !== finalT[p]) {
        return false;
      }
    }
  }
  return true;
};

console.log(backspaceCompare(s, t));
