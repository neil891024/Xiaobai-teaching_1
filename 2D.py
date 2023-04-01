# 2維列表、巢狀迴圈
# row = 行
# column = 列

nums = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [9]
]
print(nums[1][2]) #[]第幾行、[]第幾列，ex 3維列表 [][][]
for row in nums: #將每行放入row裡面
    for col in row: #將每行的值拆成每一列
        print(col)