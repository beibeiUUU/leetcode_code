class Solution(object):
    def maxProduct(self, root):
        pass
        

    def calculate_sum(self, node):
        
        current_totaL = 0

        if not node :
            return 0 
        
        if node :
        
            
            
            current_totaL = current_totaL + node.val + node.left + node.right
            return current_totaL


    
