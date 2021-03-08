#1281. Subtract the Product and Sum of Digits of an Integer
class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum=0
        product=1
        while n>0:
            a=n%10
            sum+=a
            product*=a
            n=n/10
        return(product-sum)