class Solution:
    def extend(self, s,left,right):
        while left >= 0 and right < len(s) and s[left] == s[right]: #當左右指針未超出邊界且字符相等時繼續擴展
            left = left -1
            right = right +1

        start = left +1
        # end = right -1
        length = (right -1) - (left +1) +1

        return start, length #回傳最後一次相等的長度差距
    
    def longestPalindrome(self, s):
        max_length = 0 #最大回文子串長度
        start_index = 0 #最大回文子串起始索引

        for i in range(len(s)):
            #處理奇數長度回文子串
            left1, length1 = self.extend(s, i, i)
            #處理偶數長度回文子串
            left2, length2 = self.extend(s, i, i + 1)

            #更新最大回文子串資訊
            if length1 > max_length:
                max_length = length1
                start_index = left1

            if length2 > max_length:
                max_length = length2
                start_index = left2

        result = s[start_index: start_index + max_length]
        return result
    
# 測試程式碼
solution_instance = Solution()
test_string = "babad"
result = solution_instance.longestPalindrome(test_string)
print(result)
    

