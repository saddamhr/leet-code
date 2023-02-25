#User function Template for python3

class Solution:
    def sumOfDigits (self, N):
        if N == 0:
            return 0
        else:
            return int(N % 10) + self.sumOfDigits(int(N//10))


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.sumOfDigits(N))
# } Driver Code Ends