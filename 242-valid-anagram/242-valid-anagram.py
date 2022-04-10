class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        #First solution
        # return sorted(s) == sorted(t)
        
        #Second solution o(n)
        return Counter(s) == Counter(t)
        
#         #Third solution o(s+t)
#         if len(s) != len(t):
#             return False
        
#         countS, countT = {}, {}
        
#         for i in range(len(s)):
#             # following code counts each occurence of letter in string s and t
#             countS[s[i]] = countS.get(s[i], 0)
#             countT[t[i]] = countS.get(t[i], 0)
        
#         for c in countS:
#             if countS[c] != countT.get(c, 0):
#                 return False
        
#         return True

            
        