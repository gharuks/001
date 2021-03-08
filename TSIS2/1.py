#1108. Defanging an IP Address
# address=str(input())
# print(address.replace(".","[.]"))
class Solution:
    def defangIPaddr(self, address):
        x = address.replace(".","[.]")
        return(x)