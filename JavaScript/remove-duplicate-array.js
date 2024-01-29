// const removeDuplicate = (nums) => {
//   let uniqueArr = [];

//   for (let n of nums) {
//     const alreadyHas = uniqueArr.find((unique) => unique === n);
//     if (!alreadyHas) {
//       uniqueArr.push(n);
//     }
//   }

//   return uniqueArr;
// };
// const removeDuplicate = (nums) => {
//   let uniqueArr = [];

//   for (let n of nums) {
//     if (uniqueArr.indexOf(n) === -1) {
//       uniqueArr.push(n);
//     }
//   }

//   return uniqueArr;
// };
const removeDuplicate = (nums) => {

    return [...new Set(nums)]
};

console.log(removeDuplicate([1, 2, 2, 3, 3, 4,4]));
