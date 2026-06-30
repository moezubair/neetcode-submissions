class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Input = list of ints representing heights - no negatives. Output is max area
        # Can we sort?

        # [1, 2, 3, 4, 5, 6, 7, 7]
        
        # Brute Force:
        # we can't sort, because the position of index represents the width
        # we need to optimize for l*w
        # what we if we find all the l*w:
        # areas = [1*2, 1*3, 1* 4]

        # Formula is: min(heights[l], heights[r]) * (l - r)
        # What can we do to optimize this? 
        # Two pointers to make it O(n), start from l=0, r=len-1
        # we want the Max of min(heights[l], heights[r]) and (l-r)
        # as we move, l-r will always decrease. so we have to check to optimize heights
        # we can move inwards from left if  
        largest_area = 0
        l, r = 0, len(heights) -1

        while l<r:
            min_h = min(heights[l], heights[r])
            width = r-l
            largest_area = max(min_h * width, largest_area)
            if heights[l] < heights[r]:
                #at this point, the width will only decrease, so lets move away from smallest height
                l+=1
            else:
                r-=1
        
        return largest_area