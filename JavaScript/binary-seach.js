const binarySearch = (nums, target) => {
  let start = 0;
  let end = nums.length - 1;

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);

    if (target == nums[mid]) return mid;

    if (target < nums[mid]) end = mid - 1;
    else start = mid + 1;
  }
};

console.log(binarySearch([1, 2, 3, 4], 3));
