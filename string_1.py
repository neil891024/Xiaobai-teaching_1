#如何使用字串、字串的用法
print("Hello \nMr.White")
#字串換行

print("Hello\"Mr.White") #Hello" Mr.White

print("Hello"+"Mr.White") #字串相連

#函式 function
phrase = "Hello Mr.White"
print(phrase.lower()) #將字串變為小寫
print(phrase.upper()) #將字串變為大寫
print(phrase.islower()) #判斷字串內是否都為小寫
print(phrase.isupper()) #判斷字串內是否都為大寫
print(phrase.lower().islower())

print (phrase[6]) #取得字串內第n個字
print (phrase.index("M")) #從字串中找到M在哪個位置
print (phrase.replace("H","h")) #替換字串內文字
