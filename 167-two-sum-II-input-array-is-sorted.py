from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(numbers)):
            difference = target - numbers[i]
            if dictionary.get(difference) is not None:
                return [dictionary.get(difference) + 1, i+1]
            else:
                difference[numbers[i]] = i