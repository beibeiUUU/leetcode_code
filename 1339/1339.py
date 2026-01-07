class Solution(object):
    def maxProduct(self, root):
        # 步驟1: 計算整棵樹的總和
        self.total_sum = self.calculate_sum(root)

        # 步驟2: 記錄最大乘積
        self.max_product = 0

        # 步驟3: 遍歷整棵樹,找最大乘積
        self.find_max_product(root)

        return self.max_product % (10**9 + 7)   

        

    def calculate_sum(self, node):
        #第一步:先檢查是否為空
        if not node :
            return 0 
        
        # 第二步:確定不是空了,才計算
        left_sum = self.calculate_sum(node.left)
        right_sum = self.calculate_sum(node.right)

        # 第三步:回傳總和
        return node.val + left_sum + right_sum
    

    def find_max_product (self,node):
        #第一步:先檢查是否為空
        if not node :
            return 0 
        

        #
        left_sum = self.find_max_product(node.left)
        right_sum = self.find_max_product(node.right)

        # 現在子樹的總和
        current_sum = node.val + left_sum + right_sum

        product = (self.total_sum - current_sum) * current_sum
        
        if product > self.max_product :
            self.max_product = product

        return current_sum


    
