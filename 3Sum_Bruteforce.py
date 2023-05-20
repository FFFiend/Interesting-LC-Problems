class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def solve(subset, i):
            if len(subset) == 3:
                if sum(subset) == 0:
                    v.append(subset)
                    return 
                return
            if i >= len(nums):
                return 

            solve(subset+[nums[i]],i+1)
            solve(subset,i+1)

        v = []
        solve([],0)

        ans = []
        d = {}

        for i in range(len(v)):
            v[i].sort()
        
        for i in range(len(v)):
            if "{}".format(v[i]) not in d:
                d["{}".format(v[i])] = 1
                ans.append(v[i])
        return ans
