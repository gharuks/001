#1732. Find the Highest Altitude
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        a=0
        l=[0]
        for x in gain:
            a+=x
            l.append(a)
        l.sort()
        return(l[-1])