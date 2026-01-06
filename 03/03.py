# 3. Longest Substring Without Repeating Characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_length = 0
        my_list = []

        for char in s:

            while char in my_list:
                my_list.pop(0)

            my_list.append(char)

            if len(my_list) > max_length:
                max_length = len(my_list)

        return max_length
    
# 測試程式碼
solution_instance = Solution()
test_string = "abcabcbb"
result = solution_instance.lengthOfLongestSubstring(test_string)
print(result)