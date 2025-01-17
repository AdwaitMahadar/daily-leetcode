class Solution:
    def longestPalindrome(self, s: str) -> str:
        # n = len(s)
        # if n == 0:
        #     return ""
        
        # # DP table to store palindrome information
        # dp = [[False] * n for _ in range(n)]
        # start = 0  # To store the start index of the longest palindrome
        # max_len = 1  # The length of the longest palindrome

        # # All substrings of length 1 are palindromes
        # for i in range(n):
        #     dp[i][i] = True
        
        # # Check substrings of length 2
        # for i in range(n - 1):
        #     if s[i] == s[i + 1]:
        #         dp[i][i + 1] = True
        #         start = i
        #         max_len = 2
        
        # # Check substrings of length 3 and greater
        # for length in range(3, n + 1):
        #     for i in range(n - length + 1):
        #         j = i + length - 1  # End index of the current substring
        #         if s[i] == s[j] and dp[i + 1][j - 1]:
        #             dp[i][j] = True
        #             start = i
        #             max_len = length
        
        # return s[start:start + max_len]

        # Function to expand around the center
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome found by expanding
            return s[left + 1:right]

        if not s:
            return ""

        # Initialize the result variable to hold the longest palindrome
        longest_palindrome = ""

        for i in range(len(s)):
            # Odd length palindrome (single character center)
            odd_palindrome = expand_around_center(i, i)
            # Even length palindrome (two consecutive characters center)
            even_palindrome = expand_around_center(i, i + 1)

            # Update longest_palindrome if a longer one is found
            longest_palindrome = max(longest_palindrome, odd_palindrome, even_palindrome, key=len)

        return longest_palindrome