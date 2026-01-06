# LeetCode 4: Median of Two Sorted Arrays

## 題目描述
給定兩個已排序的陣列 `nums1` 和 `nums2`,長度分別為 `m` 和 `n`,回傳這兩個陣列合併後的中位數。

---

## 解題思路

### 什麼是中位數?
- **奇數個元素**: 中位數是正中間的那個數
- **偶數個元素**: 中位數是中間兩個數的平均值

### 解法步驟
1. **合併兩個陣列**: 使用 `+` 運算符合併
2. **排序合併後的陣列**: 使用 `sorted()` 函數
3. **計算陣列長度**: 使用 `len()` 函數
4. **判斷奇偶並計算中位數**:
   - 奇數: 回傳中間位置的元素
   - 偶數: 回傳中間兩個元素的平均值

---

## 程式碼架構

```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        # 步驟1: 合併並排序兩個陣列
        fit_array = sorted(nums1 + nums2)
        
        # 步驟2: 計算陣列長度
        array_length = len(fit_array)
        
        # 步驟3: 判斷奇數情況
        if array_length % 2 == 1:
            med_num = array_length // 2 
            return fit_array[med_num]
        
        # 步驟4: 判斷偶數情況
        elif array_length % 2 == 0:
            left_num = array_length // 2 - 1
            right_num = array_length // 2
            return (fit_array[left_num] + fit_array[right_num]) / 2.0
```

---

## 關鍵知識點

### 1. 列表合併
```python
# 使用 + 運算符
merged = list1 + list2
```

### 2. 排序
```python
# sorted() 函數: 回傳新的排序列表
sorted_list = sorted(original_list)

# sort() 方法: 直接修改原列表,不回傳值
original_list.sort()
```

### 3. 判斷奇偶
```python
# 使用 % (取餘數運算符)
if number % 2 == 1:  # 奇數
    pass
elif number % 2 == 0:  # 偶數
    pass
```

### 4. 整數除法
```python
# // 是整數除法,會捨去小數部分
5 // 2  # 結果: 2
4 // 2  # 結果: 2
```

### 5. 陣列索引
- Python 陣列索引從 0 開始
- `array[0]` 是第一個元素
- `array[len(array)//2]` 是中間位置(奇數長度時)

---

## 範例測試

### Example 1
```
輸入: nums1 = [1,3], nums2 = [2]
合併: [1, 2, 3]
長度: 3 (奇數)
中間索引: 3 // 2 = 1
輸出: fit_array[1] = 2
```

### Example 2
```
輸入: nums1 = [1,2], nums2 = [3,4]
合併: [1, 2, 3, 4]
長度: 4 (偶數)
左索引: 4 // 2 - 1 = 1
右索引: 4 // 2 = 2
輸出: (2 + 3) / 2.0 = 2.5
```

---

## 時間與空間複雜度

- **時間複雜度**: O((m+n)log(m+n))
  - 合併: O(m+n)
  - 排序: O((m+n)log(m+n))
  
- **空間複雜度**: O(m+n)
  - 需要額外空間存放合併後的陣列

> **注意**: 題目要求 O(log(m+n)),此解法為簡化版本。進階解法需使用二分搜尋。

---

## Python 基礎語法複習

### Class 類別
```python
class ClassName(object):
    def method_name(self, parameter1, parameter2):
        # 方法內容
        pass
```

### 函數定義
```python
def function_name(parameter):
    # 函數內容
    return result
```

### 條件判斷
```python
if condition:
    # 執行程式碼
elif another_condition:
    # 執行程式碼
else:
    # 執行程式碼
```

---

## 除錯技巧

如果程式有問題,可以加入 print 來檢查:
```python
print("合併後的陣列:", fit_array)
print("陣列長度:", array_length)
print("中位數索引:", med_num)
```

---

## 重點提醒

1. ✅ `sorted()` 回傳新列表,`sort()` 修改原列表且不回傳值
2. ✅ 使用 `//` 整數除法來計算索引
3. ✅ 偶數情況要除以 `2.0` 確保得到浮點數
4. ✅ 陣列索引從 0 開始
5. ✅ `%` 運算符用來取餘數,判斷奇偶

---

## 學習心得

這題練習到的技能:
- ✅ Python 類別和方法的定義
- ✅ 列表的操作(合併、排序、索引)
- ✅ 條件判斷 (if-elif-else)
- ✅ 數學運算(整數除法、取餘數)
- ✅ 理解中位數的概念

繼續加油!💪
