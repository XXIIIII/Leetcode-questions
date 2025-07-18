class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and symbol_dict[s[i]] < symbol_dict[s[i+1]]:
                total += symbol_dict[s[i+1]] - symbol_dict[s[i]]
                i += 1
            else:
                total += symbol_dict[s[i]]
            i += 1
        return total
        
