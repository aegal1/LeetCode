class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        #First solution o(1)
        return sorted(s) == sorted(t)
        
        #Second solution o(n)
        return Counter(s) == Counter(t)
        
            
        
