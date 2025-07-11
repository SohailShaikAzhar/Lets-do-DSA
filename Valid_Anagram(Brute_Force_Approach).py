class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lst1 = sorted(list(s.lower()))
        lst2 = sorted(list(t.lower()))
        if lst1 == lst2:
            return True
        return False
