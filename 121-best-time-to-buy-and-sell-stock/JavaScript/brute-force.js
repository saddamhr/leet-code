/**
 * @param {number[]} prices
 * @return {number}
 */
const maxProfit = function(prices) {
  let maxProfit = 0
  for (let i = 0; i < prices.length; i++){
      let localMax = 0
      for(let j = i + 1; j < prices.length; j ++){
          localMax = Math.max(localMax, prices[j]) 
      }
      maxProfit = Math.max(maxProfit, localMax - prices[i])
  }
  return maxProfit
  
};