class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        s = s + s
        return goal in s

# link to question, https://leetcode.com/problems/rotate-string/