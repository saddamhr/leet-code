nums = [1, 2, 3, 1];

var containsDuplicate = function (nums) {
  nums = nums.sort();
  for (let p1 = 0; p1 < nums.length - 1; p1++) {
    const nextIndex = p1 + 1;
    const currentIndex = p1;
    if (nums[currentIndex] === nums[nextIndex]) {
      return true;
    }
  }
  return false;
};

console.log(containsDuplicate(nums));
