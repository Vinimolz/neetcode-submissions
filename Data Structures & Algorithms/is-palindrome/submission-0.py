class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(filter(str.isalnum, s)).lower()

        i = 0
        j = len(new_s) - 1

        while i < j: # What if len(s) == 1 ?
            if new_s[i] != new_s[j]: # How to check for non alphanumeric ?
                return False
            i += 1
            j -= 1

        return True