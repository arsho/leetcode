class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        result = ""
        for c in str:
            if "A"<=c<="Z":
                result += chr(ord(c) - ord('A') + ord('a'))
            else:
                result += c
        return result
