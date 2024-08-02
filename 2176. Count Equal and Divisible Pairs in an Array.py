class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        d = dict()
        count = 0
        for i,num in enumerate(nums):
            if num not in d:
                d[num] = [i]
            else:
                d[num].append(i)
        for key in d:
            if len(d[key]) > 1:
                for i in range(len(d[key])):
                    indexI = d[key][i]
                    for j in range(i+1, len(d[key])):
                        indexj = d[key][j]
                        if (indexI*indexj) % k == 0:
                            count += 1
        return count

