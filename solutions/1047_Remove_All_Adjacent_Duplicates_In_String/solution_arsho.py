'''
Title     : 1047. Remove All Adjacent Duplicates In String
Category  : Stack
URL       : https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
Author    : arsho
Created   : 01 October 2019
'''


class Solution:
    def remove_adjacent_duplicate(self, s):
        original_str = s
        s_length = len(s)
        new_str = ""
        i = 0
        while i < s_length:
            pos = i + 1
            if pos >= s_length or s[i] != s[pos]:
                new_str += s[i]
                i = pos
            else:
                i = pos + 1
        if original_str == new_str:
            return None
        return new_str

    def removeDuplicates(self, S: str) -> str:
        stack = []
        new_string = self.remove_adjacent_duplicate(S)
        if new_string != None:
            stack.append(new_string)
            while len(stack)>0:
                s = stack.pop()
                new_string = self.remove_adjacent_duplicate(s)
                if new_string != None:
                    stack.append(new_string)
                else:
                    return s
        else:
            return S

if __name__ == "__main__":
    solution = Solution()
    s = solution.removeDuplicates("abbaca")
    expected_solution = "ca"
    assert s == expected_solution, "ca"

    input_str = "aaaaaaaa"
    s = solution.removeDuplicates(input_str)
    expected_solution = ""
    assert s == expected_solution, ""

    input_str = "aaaaaaaaa"
    s = solution.removeDuplicates(input_str)
    expected_solution = "a"
    assert s == expected_solution, "a"
