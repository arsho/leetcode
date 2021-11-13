class Solution(object):
    def numberOfLines(self, widths, S):
        line_width = 0
        count_line = 1
        S = list(S)
        while len(S)>0:
            current_position = ord(S[0].lower()) - ord('a')
            current_value = widths[current_position]
            if line_width + current_value<=100:
                line_width += current_value
            else:
                line_width = current_value
                count_line += 1
            del S[0]
        return [count_line, line_width]
