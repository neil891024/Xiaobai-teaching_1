#檔案的讀取、寫入
#open("檔案路徑", mode="開啟模式")
#絕對路徑 ex:D:/python/123.txt
#相對路徑 以程式的位置做延伸 ex:123.txt

# mode="r" 讀取
# mode="w" 複寫
# mode="a" 在原先的資料後寫東西

# file = open("123.txt",mode="r") #讀取
file = open("123.txt",mode="a",encoding="utf-8") #encoding:寫入資料的格式
# for line in file:
#     print(line) #將資料一行一行讀取出來

# print(file.read()) #讀取全部資料
# print(file.readline()) #讀取一行資料
#print(file.readlines()) #將每行資料放到列表中，\n_換行
# file.write(" 你好")
# file.close() #將檔案關掉避免佔用電腦資源

with open("123.txt",mode="a",encoding="utf-8") as file: #可省略將檔案關掉這個步驟
    file.write("\n 你好")