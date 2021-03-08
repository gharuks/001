#1678. Goal Parser Interpretation
# a=str(input())
# a=a.replace("()", "o")
# a=a.replace("(al)", "al")
# print(a)
class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        command=command.replace("()", "o")
        command=command.replace("(al)", "al")
        return(command)