class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:

        # Input: list of numbers (positive and negative allowed), sorted. target integer
        # Output: list of indices that add up to target
        # [1, 2 ,3, 4] target =6

        # Bruce Force
        l, r = 0, len(n)-1

        while l<r:
            # move l if  
            if (n[l]+n[r] == target):
                return [l+1,r+1]
            while n[l]+n[r] < target:
                l+=1
            while n[l]+n[r] > target:
                r-=1
        return []
            