from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        while pushed[i] != popped[0]:
            stack.append(pushed[i])
            i += 1
        stack.append(pushed[i])
        j = 0
        i += 1
        while j <= len(popped) - 1:
            if stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                if i <= len(pushed) - 1:
                    stack.append(pushed[i])
                    i += 1
        # return len(stack) == 0
        return False
# Solution().validateStackSequences([1,2,3,4,5], [4,5,3,2,1])
Solution().validateStackSequences([1,2,3,4,5], [4,3,5,1,2])