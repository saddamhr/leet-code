import { swap } from './utils';

const reverseArray = (nums) => {
  let revArr = [];
  for (let i = nums.length - 1; i >= 0; i--) {
    revArr.push(nums[i]);
  }
  return revArr;
};

const nums = [1, 2, 3];
console.log(reverseArray(nums));

const reverseArray = (nums) => {
  let left = 0;
  let right = nums.length - 1;
  while (left < right) {
    nums[left] = nums[left] + nums[right];
    nums[right] = nums[left] - nums[right];
    nums[left] = nums[left] - nums[right];
    left += 1;
    right -= 1;
  }
};

const nums = [1, 2, 3];
reverseArray(nums);
console.log(nums);

const reverseArray = (nums, n) => {
  let revArr = [];
  if (n === -1) return revArr;
  revArr.push(nums[n]);
  return revArr.concat(reverseArray(nums, n - 1));
};

const nums = [1, 2, 3];
const n = nums.length - 1;
console.log(reverseArray(nums, n));

const reverseArray = (nums, left, right) => {
  if (left < right) {
    nums[left] = nums[left] + nums[right];
    nums[right] = nums[left] - nums[right];
    nums[left] = nums[left] - nums[right];
    reverseArray(nums, left + 1, right - 1);
  }
};

const nums = [1, 2, 3];
const left = 0;
const right = nums.length - 1;
console.log(reverseArray(nums, left, right));
console.log(nums);
