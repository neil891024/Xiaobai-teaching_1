#猜數字遊戲
secert_num = 88
guess = None 
guess_count = 0 #猜測的次數
guess_limit = 3 #最多能猜幾次
out_of_limit = False #布林值，是否猜超過三次

while secert_num != guess and not (out_of_limit):
    #當secert_num不等於guess，且次數未超過3次
    guess_count +=1
    if guess_count <= guess_limit:
        #判斷
        guess = int(input("請輸入數字: "))
        if guess > secert_num:
            print("小一點")
        elif guess < secert_num:
            print("大一點")
    else:
        out_of_limit = True

if out_of_limit:
    print("抱歉 你輸了~")
else:
    print("恭喜贏了")

