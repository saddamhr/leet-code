// STATUS: Accepted

const heightsArray = [1, 8, 6, 2, 5, 4, 8, 3, 7];

const getMinMax = (a, b, type) => {
  let minOrMaxValue = 0;
  if (type === 'min') {
    minOrMaxValue = a < b ? a : b;
  } else if (type === 'max') {
    minOrMaxValue = a > b ? a : b;
  }
  return minOrMaxValue;
};

const getMaxWaterContainer = (heights) => {
  let p1 = 0, p2 = heights.length - 1, maxArea = 0;
  while (p1 < p2) {
    const height = getMinMax(heights[p1], heights[p2], 'min');
    const width = p2 - p1;
    const area = height * width;
    maxArea = getMinMax(maxArea, area, 'max');
    heights[p1] <= heights[p2] ? p1++ : p2--;
  }
  return maxArea;
};


console.log(getMaxWaterContainer(heightsArray));
