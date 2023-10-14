class Solution:
    def makeFancyString(self, s: str) -> str:
        result = [s[0]] 
        count = 1   
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
                if count < 3:
                    result.append(s[i])
            else:
                count = 1
                result.append(s[i])  
        return ''.join(result)

# link to question, https://leetcode.com/problems/delete-characters-to-make-fancy-string/