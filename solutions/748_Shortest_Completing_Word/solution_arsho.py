class Solution:
    def shortestCompletingWord(self, license, words):
        """
        :type license: str
        :type words: List[str]
        :rtype: str
        """
        d = {}
        for c in license.lower():
            if c.islower():
                d[c] = d.get(c, 0) + 1
        minimum_length = 10 ** 9
        shortest_word = None
        for word in words:
            word = word.lower()
            e = {}
            for c in word:
                if c.islower():
                    e[c] = e.get(c, 0) + 1
            is_valid = True
            for c in d:
                if e.get(c, 0) < d[c]:
                    is_valid = False
                    break
            word_length = len(word)
            if is_valid and word_length < minimum_length:
                minimum_length = word_length
                shortest_word = word
        return shortest_word


if __name__ == '__main__':
    license = "1s3 456"
    words = ["looks", "pest", "stew", "show"]
    print(Solution().shortestCompletingWord(license, words))
