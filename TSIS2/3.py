#1512. Number of Good Pairs
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a=dict()
        for x in nums:
            if x not in a:
                a[x]=0
            a[x]+=1
        s=0
        for x in a:
            s+=(x*(x-1))//2
        return s