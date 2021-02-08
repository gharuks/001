#1732. Find the Highest Altitude
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        a=[]
        for x in gain:
            a.append(gain[x])
        a.sort()
        return(a[-1])