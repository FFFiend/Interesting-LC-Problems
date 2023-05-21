class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)


        for i in range(len(nums)):

            prev = float('-inf')
            index = 0
            j = 0
            while j < i:

                if nums[j] < nums[i] and prev < nums[j]:
                    index = j
                    prev = nums[j]
                    dp[i] += 1
                
                elif nums[j] < nums[i] and prev >= nums[j]:
                    if dp[j] >= dp[i]:
                        dp[i] = dp[j] + 1
                        prev = nums[j]
                        index = j

                j += 1
        return max(dp)
      
 # This is iterative dp, O(n^2). The recursive solution involves a dp array such as dp[index][prev_index] on the whole, this approach is cleaner.
