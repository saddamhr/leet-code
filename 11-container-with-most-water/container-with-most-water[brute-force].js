// STATUS: Time Limit Exceeded

const heightsArray = [1, 8, 6, 2, 5, 4, 8, 3, 7];

const getMinNumber = (a, b) => (a < b ? a : b);

const getMaxWaterContainer = (heights) => {
  let maxArea = 0;
  for (let a = 0; a < heights.length; a++) {
    for (let b = a + 1; b < heights.length; b++) {
      const height = getMinNumber(heights[a], heights[b]);
      const width = b - a;
      const area = height * width;
      if (maxArea < area) {
        maxArea = area;
      }
    }
  }
  return maxArea;
};

console.log(getMaxWaterContainer(heightsArray));
