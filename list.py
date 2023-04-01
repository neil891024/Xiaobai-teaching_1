#列表list、列表的用法
scores = [90,70,60,50,40]
friends = ["小黑","小黃","小綠"]
things = [90,"小黑",True]
#print(things)
#print(scores[0]) #取得第0位資料 負號為倒數
#print(scores[1:4]) #從第1位取到第4筆資料
#print(scores[1:]) #取第1位後的資料
#print(scores[:4]) #取第4位前的資料

#phrase = "Hello Mr.White"
#print(phrase[0:5])

#scores[0] = 30 #修改列表內資料
print(scores)

#函式
#scores.extend(friends) #延伸
#scores.append(30) #加入
#scores.insert(2,30) #插入，位置在數值
#scores.remove(30) #刪除指定數字
#scores.clear() #清除列表內所有資料
#scores.pop() #移除最後一位
#scores.sort() #由小到大排列
scores.reverse()#反轉
print(scores)

#print(scores.index(90)) #回傳指定數字在第幾位
print(scores.count(60)) #列表內有幾個指定數字