from collections import deque

class Solution(object):
    def maxLevelSum(self, root):

        if not root: #如果樹是空的 回傳0
            return 0

        queue = deque([root])

        current_lavel = 1   #目前的層數
        max_sum = float('-inf')  #最大和 #負無限大是因為可能有負數
        max_level = 1  #最大和的層數
        
        #開始BFS
        while queue: 
            
            layer_sum = 0 #每一層的和
            layer_nodes = len(queue) #每一層的節點數量

            for i in range(layer_nodes): #處理每一層的節點
                node = queue.popleft()
                # print(node)
                layer_sum =  layer_sum + node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if layer_sum > max_sum :
                max_sum = layer_sum
                max_level = current_lavel   

            current_lavel = current_lavel + 1
        return max_level


                    
                



















# queue.append(1)
# queue.append(2)
# queue.append(3)

# print(queue)

# if queue :
#     a1 = queue.popleft()
    
# print(a1)

    