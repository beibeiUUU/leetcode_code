# 9. Palindrome Number ---------------------------------------
class Solution:
    def isPalindrome(self, x):
        if x < 0 :
            return False
        
        str_x = str(x)
        reversed_str_x = str_x[::-1]
        return str_x == reversed_str_x
    
# 測試程式碼
solution_instance = Solution()
test_number = 12126
result = solution_instance.isPalindrome(test_number)
print(result)