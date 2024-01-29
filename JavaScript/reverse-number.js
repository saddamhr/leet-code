const getReverseNumber = (num) => {
  let reverseNumber = 0;

  while (num > 0) {
    reverseNumber = reverseNumber * 10 + (num % 10);
    num = Math.floor(num / 10);
  }
  return reverseNumber;
};

console.log(getReverseNumber(21));
