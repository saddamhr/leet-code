from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash_map = {}
        res = []
        if len(list1) <= len(list2):
            max_l, min_l = list2, list1
        else:
             max_l, min_l = list1, list2
        for i in range(len(max_l)):
            if max_l[i] in min_l:
                print('----->',type( max_l[i]))
                hash_map[i] = max_l[i] + min_l.index(max_l[i])
            else:
                continue
        print(hash_map)
        key_arr = list(hash_map.keys())
        value_arr = list(hash_map.values())
        min_val = min(key_arr) # key_arr.min()
        print(min_val)
        for i in range(len(key_arr)):
            if key_arr[i] == min_val:
                res.append(hash_map[i])
            else:
                return value_arr[0]
        return res
        
list1 =["happy","sad","good"]
list2 = ["sad","happy","good"]
s = Solution()
print(s.findRestaurant(list1, list2))



