/* 
  STATUS: Time Limit Exceeded
  Time Complexity: 0(n)
  Space Complexity: 0(1)
*/

const heightsArray = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2];

const getTrappedRainwater = function (heights) {
  let left = 0;
  maxLeft = maxRight = totalWater = 0;
  right = heights.length - 1;
  while (left < right) {
    if (heights[left] <= heights[right]) {
      // operate left
      if (heights[left] >= maxLeft) {
        // update leftMax
        maxLeft = heights[left];
      } else {
        // calculate water
        totalWater += maxLeft - heights[left];
      }
      left++;
    } else {
      // operate right
      if (heights[right] >= maxRight) {
        maxRight = heights[right];
      } else {
        totalWater += maxRight - heights[right];
      }
      right--;
    }
  }
  return totalWater;
};

console.log(getTrappedRainwater(heightsArray));
