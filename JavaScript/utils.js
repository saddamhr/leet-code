const swap = (a, b) => {
  // 10, 20
  a = a + b; // 30
  b = a - b; // 10
  a = a - b; // 20
  return [a, b];
};

export { swap };
