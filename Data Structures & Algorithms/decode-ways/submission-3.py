class Solution:
    def numDecodings(self, s: str) -> int:
        # Base case: an empty string or a string starting with '0' cannot be decoded
        if not s or s[0] == "0":
            return 0
        
        # prev2 represents dp[i-2], prev1 represents dp[i-1]
        prev2 = 1  # Ways to decode a string of length 0
        prev1 = 1  # Ways to decode a string of length 1
        
        for i in range(1, len(s)):
            current_ways = 0
            
            # 1. Check if the single digit s[i] is valid (1-9)
            if s[i] != "0":
                current_ways += prev1
                
            # 2. Check if the two-digit combination s[i-1:i+1] is valid (10-26)
            two_digit = int(s[i-1 : i+1])
            if 10 <= two_digit <= 26:
                current_ways += prev2
                
            # If at any point it's impossible to decode further, fail early
            if current_ways == 0:
                return 0
                
            # Move our sliding window forward
            prev2 = prev1
            prev1 = current_ways
            
        return prev1