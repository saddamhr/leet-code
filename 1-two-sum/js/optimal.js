/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSum = function (nums, target) {
  const hashMap = {};
  for (let i = 0; i < nums.length; i++) {
    const numberToFind = target - nums[i];
    if (hashMap.hasOwnProperty(numberToFind)) {
    //   return [i, hashMap[numberToFind]];
      return [nums[i], nums[hashMap[numberToFind]]]; // if we need to return number instead of value
    }
    hashMap[nums[i]] = i;
  }
};

console.log(twoSum([2, 7, 11, 15], 9));
