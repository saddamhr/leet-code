class Solution:

    def encode(self, strs):
        res = ''
        for i in range(len(strs)):
            res += str(len(strs[i])) + '#' + strs[i]
        return res

    def decode(self, str): # "4#lint4#code4#love3#you"
        res, i = [], 0
        while i < len(str):
            j  = i
            while str[j] != '#':
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res


print(Solution().encode(["lint","code","love","you"]))
print(Solution().decode("4#lint4#code4#love3#you"))