# 7. Reverse Integer

class Solution(object):
    def reverse(self, x):
        result = 0 
        num = x
        needabs = 0

        #處理負數
        if num < 0 : 
            num = abs(num)
            needabs = 1 

        #反轉數字
        while num :
            
            remainder = num % 10
            
            result = result * 10 + remainder
            
            num = num // 10

        #把拿起來的負數放回去
        if needabs :
            result = result * -1

        #處理32位元溢位
        if not -2147483648 <= result <= 2147483647 :
            return 0

        return result


# print(-123 % 10)
# print(-123 // 10)