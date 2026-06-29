class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Input is not sorted
        ## Can we sort this list and make it a two pointer problem.
        ## Sorted list: [-4,-1,0,1,2]
        

        results = set()
        nums.sort()

        for i in range(len(nums) -2):
            j = i+1
            k = len(nums) - 1
            # From here, we need to find two numbers in array nums[i+1:] where they sum to x+y=-nums[i]
            while j < k:
                sum = nums[i]+nums[j]+nums[k]
                if sum == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    results.add(triplet)
                    j += 1
                    k -= 1
                elif sum < 0: #If we need a bigger number move right
                    j +=1
                else:
                    k -=1
        # Convert set of tuples back to a list of lists
        return [list(t) for t in results]