'''Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"
 
Constraints:
1 <= s.length <= 104
s consists of lowercase English letters.'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        visited = [False]*26
        counts = [0]*26
        stack = []
        for i in s:
            counts[ord(i)-97] += 1
        for i in s:
            counts[ord(i)-97] -= 1
            if visited[ord(i)-97]:
                continue
            while len(stack)!=0 and stack[-1] > i and counts[ord(stack[-1])-97] > 0 :
                visited[ord(stack.pop())-97] = False
            stack.append(i)
            visited[ord(i)-97] = True
        ans = ""
        while len(stack)!=0 :
            ans += stack.pop()
        return ans[::-1]
