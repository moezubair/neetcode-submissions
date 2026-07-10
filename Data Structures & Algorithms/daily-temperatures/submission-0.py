class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0 for t in temperatures]
        stack = []
        # If we go through the array, we have to count how many items before temp > current_temp
        # for each element, we would have to loop one time. so n^n

        # we can build by checking the temperatures from last element to first

        # we know that the last element will be 0 always

        for r in range(len(temperatures)):
            days = 0
            for c in range(r+1, len(temperatures)):
                if temperatures[c] > temperatures[r]:
                    results[r] = days + 1
                    break
                else :
                    days += 1
        
        return results