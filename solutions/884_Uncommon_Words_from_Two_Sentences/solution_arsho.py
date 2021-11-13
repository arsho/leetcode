class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        data = {}
        for word in A.split(" "):
            data[word] = data.get(word, 0)+1
        for word in B.split(" "):
            data[word] = data.get(word, 0) + 1
        return [word for word in data if data[word]==1]
