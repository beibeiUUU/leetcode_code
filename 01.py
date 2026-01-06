# 01two sum ---------------------------------------

# def two_sum(nums, target):
#     num_map = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in num_map:
#             return (num_map[complement], i)
#         num_map[num] = i
#     return None

# num = [2, 7, 11, 15]
# target = 9

# def two_sum(num, target):
#     for i in range(len(num)):
#         for j in range(i + 1, len(num)):
#             if num[i] + num[j] == target:
#                 return (i, j)
#     return None

# result = two_sum(num, target)
# print(result)



# 02 add two numbers ---------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0 #進位
        dummy_head = ListNode(0) #虛擬頭節點
        current = dummy_head #當前節點

        while l1 or l2 or carry: #當l1或l2或進位不為0時繼續迴圈
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0

            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0

            total = val1 + val2 + carry
            carry = total // 10 #計算進位
            current.next = ListNode(total % 10) #創建新節點
            current = current.next #移動當前節點
        return dummy_head.next #返回結果鏈表的頭節點
    
    
# 測試程式碼
def print_linked_list(node):
    values = []
    while node:
        values.append(str(node.val)) #把節點值轉成字串加入列表
        node = node.next #移動到下一個節點
    print(" -> ".join(values)) #用箭頭連接並打印節點值

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
solution_instance = solution()
result = solution_instance.addTwoNumbers(l1, l2)
print_linked_list(result)  