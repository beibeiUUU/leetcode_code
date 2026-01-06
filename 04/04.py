class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        #因為原本合併的不是排好的陣列 所以用sorted讓合併的陣列排整齊
        fit_array = sorted(nums1 + nums2)

        array_length = len(fit_array)

        #判斷陣列是不是奇數
        if array_length % 2 == 1:
            med_num = array_length // 2 
            
            return fit_array[med_num]
            

        #判斷陣列是不是偶數
        elif array_length % 2 == 0:
            left_num = array_length // 2 -1
            right_num = array_length // 2

            return (fit_array[left_num] + fit_array[right_num]) / 2.0 