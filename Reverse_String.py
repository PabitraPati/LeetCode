"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Hint  - The entire logic for reversing a string is based on using the opposite directional two-pointer approach!

"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # soution 1
        b, e = 0, len(s)-1
        while b < e:
            s[b], s[e] = s[e], s[b]
            b, e = b+1, e-1
        
        #solution 2
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]
        
    
