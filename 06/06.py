# rows = []
# numrows = 3
# for i in range(numrows):
#     rows.append([])

# current_row = 0 
# direction = 1


# letters = "PAYPALISHIRING"
# for letter in letters:
#     rows[current_row].append(letter)

#     if current_row == 0:  # 頂端往下走
#         direction = 1 

#     if current_row == numrows - 1 : #頂端往上走
#         direction = -1

#     current_row = current_row + direction

    
# print(rows)
    
# result = "" 
# for row in rows:
#     result = result + "".join(row)
# print(result)

# letters = "PAYPALISHIRING"

def convert(letters ,numRows):

    if numRows == 1:
        return letters
    
    rows = []
    for i in range(numRows):
        rows.append([])

    # Initialize variables
    current_row = 0 
    direction = 1

    #處理每個字母
    for letter in letters:
        rows[current_row].append(letter)

        if current_row == 0:  # 頂端往下走
            direction = 1 

        if current_row == numRows - 1 : #頂端往上走
            direction = -1
            
        current_row = current_row + direction

    #合併結果
    result = "" 
    for row in rows:
        result = result + "".join(row)
    return result

print(convert("PAYPALISHIRING", 3))
print(convert("PAYPALISHIRING", 4))
print(convert("A", 1))