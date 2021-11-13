class Solution(object):
    def get_morse_message(self, original_message):
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_message = ""
        for c in original_message:
            c = c.lower()
            position = ord(c) - ord('a')
            try:
                morse_message+=morse_codes[position]
            except:
                pass
        return morse_message
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        messages = {}
        for word in words:
            morse_message = self.get_morse_message(word)
            messages[morse_message] = 1
        return len(messages.keys())
