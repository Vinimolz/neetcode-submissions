class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_s = {}
        dict_t = {}

        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1

        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        if len(dict_s) != len(dict_t):
            return False

        for k in dict_s.keys():
            if dict_s[k] != dict_t.get(k):
                return False

        return True