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

        areas = List[int]
        area_seen = {}
        largest_area = 0
        for i in range(0, len(heights)):
            # calculate max are between l, and right
            for j in range(i+1, len(heights)):
                max_n = min(heights[i], heights[j])
                area = max_n*(j-i)
                #print(f"{max_n} * {i}, {j} = {area}")
                #print (f" {heights[i]}, {heights[j]}")
                largest_area = max(area, largest_area)
        
        return largest_area