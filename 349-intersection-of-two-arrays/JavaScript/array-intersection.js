/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
const intersection = function (nums1, nums2) {
  let d = {};
  let res = [];

  for (let n of nums1) {
    d[n] = 1;
  }

  for (let n of nums2) {
    if (d.hasOwnProperty(n) && d[n]) {
      res.push(n);
      d[n] -= 1;
    }
  }
  return res;
};
