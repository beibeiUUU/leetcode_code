class Solution(object):
    def myAtoi(self, s):
        s_strip = s.lstrip()

        if not len(s_strip) :
            return 0 
        
        sign  = 1 # 1是正的 -1是負的
        index = 0 #從頭開始看的索引

        #先讓數值變成絕對值
        if s_strip[0] == '-' :
            sign = -1 
            index = index +1
        elif s_strip[0] == '+' :
            sign = 1
            index = index +1

        #計算用
        result = 0

        #把數字一個一個摘出來，直到全部摘出來，或者遇到不是數字
        while index < len(s_strip) and s_strip[index].isdigit():
            result = result * 10 +  int(s_strip[index])
            index = index + 1 

        #把絕對值變回有號數
        result = result * sign
        
        #限制最大最小值
        if result < -2**31:
            return -2**31
        elif result > 2**31-1:
            return 2**31-1
        
        return result
