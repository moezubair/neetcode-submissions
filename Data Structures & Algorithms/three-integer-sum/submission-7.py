class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Input is not sorted
        ## Can we sort this list and make it a two pointer problem.
        ## Sorted list: [-4,-1,0,1,2]

        nums.sort()
        results = set()
        for i in range(0, len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            if nums[i] > 0:
                break
            
            if i> 0 and nums[i] == nums[i-1]:
                continue


            while l < r:
                sum_n = nums[i] + nums [l] + nums [r]
                if sum_n == 0:
                    results.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
                    r -= 1
                elif sum_n < 0:
                    l += 1
                else:
                    r -= 1

        return [list (t) for t in results]


                    
