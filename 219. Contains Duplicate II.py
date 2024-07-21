class Solution:
    # Initial solution, slow becuase needs to intialise array of length k with None
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numSet = set()
        numArr = []
        for i in range(k+1):
            numArr.append(None)

        for num in nums:
            x = numArr.pop(0)
            if (x in numSet):
                numSet.remove(x)
            numArr.append(num)
            if (num not in numSet):
                numSet.add(num)
            else:
                return True

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}
        for i in range(len(nums)):
            if (nums[i] in hm and (i - hm[nums[i]] <= k)):
                return True

            hm[nums[i]] = i
        
        

        