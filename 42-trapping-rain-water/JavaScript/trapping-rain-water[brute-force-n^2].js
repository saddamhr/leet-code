/* 
  STATUS: Time Limit Exceeded
  Time Complexity: 0(n^2)
  Space Complexity: 0(1)
*/

const heightsArray = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2];
MAX = 'max';
MIN = 'min';

const getMinMax = (a, b, type) => {
  let minOrMaxValue = 0;
  if (type === 'min') {
    minOrMaxValue = a < b ? a : b;
  } else if (type === 'max') {
    minOrMaxValue = a > b ? a : b;
  }
  return minOrMaxValue;
};

const getTrappedRainwater = function (heights) {
  let totalWater = 0;
  for (let p = 0; p < heights.length; p++) {
    let leftP = (rightP = p);
    maxLeft = maxRight = 0;

    // find left max value from current position
    while (leftP >= 0) {
      maxLeft = getMinMax(maxLeft, heights[leftP], MAX);
      // maxLeft = Math.max(maxLeft, heights[leftP]); alternative
      leftP--;
    }

    // find right max value from current position
    while (rightP < heights.length) {
      maxRight = getMinMax(maxRight, heights[rightP], MAX);
      // maxRight = Math.max(maxRight, heights[rightP]); alternative
      rightP++;
    }

    // calculate water for current position
    const curentWater = getMinMax(maxLeft, maxRight, MIN) - heights[p];
    // const curentWater = Math.min(maxLeft, maxRight) - heights[p]; alternative

    // calculate total water
    if (curentWater >= 0) {
      totalWater += curentWater;
    }
  }
  return totalWater;
};

console.log(getTrappedRainwater(heightsArray));
