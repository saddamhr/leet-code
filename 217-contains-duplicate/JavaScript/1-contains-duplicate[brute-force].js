nums = [1,2,3,1]

var containsDuplicate = function (nums) {
  for (let p1 = 0; p1 < nums.length-1; p1++) {
    for (let p2 = p1 + 1; p2 < nums.length; p2++) {
      if (nums[p1] === nums[p2]) {
        return true;
      }
    }
  }
  return false;
};

console.log(containsDuplicate(nums));
