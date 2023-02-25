class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        Is_pal = False

        if x_str == x_str[::-1]: Is_pal = True
        else: pass

        return Is_pal