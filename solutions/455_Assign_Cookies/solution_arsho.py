class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        count = 0
        for gi in g: 
            for i,v in enumerate(s):
                if gi<=v:
                    del s[i] 
                    count+=1
                    break
        return count
    
