class Solution(object):
    def isPalindrome(self, s):
        a = "".join(s.split())
        temp = ""
        for i in a:
            if i.isalnum():
                temp+=i.lower()

        return temp == temp[::-1]
        
