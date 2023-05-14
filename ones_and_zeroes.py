class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
      dp = [[[float('-inf')]* (n+1) for i in range(m+1)] for k in range(len(strs))]

      def solve(index, curr_m, curr_n):

        # base cases 
        if index >= len(strs):
          # terminate, base case 
          return 0
        if curr_m > m or curr_n > n:
          return 0 # we want something like..that kills off the base case 


        # cache check
        if dp[index][curr_m][curr_n] != float('-inf'):
          return dp[index][curr_m][curr_n] 

        # choice, not take 

        pick = solve(index+1, curr_m, curr_n)

        # condition check 
        new_m = curr_m + strs[index].count("0")
        new_n = curr_n + strs[index].count("1")
        

        # choice, take
        notpick = 0
        if new_m <= m and new_n <= n:
          notpick = solve(index+1, new_m, new_n) + 1


        # not found cached, so calculate max of both recursive
        # calls, and return
        # store the max at this position.
        dp[index][curr_m][curr_n] = max(pick,notpick)

        return dp[index][curr_m][curr_n]

      return solve(0, 0, 0)   
