#if判斷句
#1.如果我肚子餓，我就去吃飯
# hungry=True
# if hungry:
    # print("我就去吃飯")

#2.如果今天下雨，我就開車，我就開車去上班
#否則我就走路去上班
# rainy=True 
# if rainy:
    # print("我就開車去上班")
# else:
    # print("我就走路去上班")

#3.如果 你考100分，我給你1000元
#或是如果你考80分以上，我給你500元
#否則你給我30元
score=90
# if score==100:
    # print("我給你1000元")
# elif score >=80:
    # print("我給你500元")
# else:
    # print("你給我300元")

# #4.如果 你考100分 且今天下雨
# #我給你1000元
# #否則你給我100元
# score_1=80
# rainy_1 = False
# if score==100 and rainy_1:
#     print("我給你1000元")
# else:
#     print("你給我100元")

# #5.如果 你考100分或今天下雨
# #我給你100元
# #否則你給我100元
# score_1=80
# rainy_1 = True
# if score==100 or rainy_1:
#     print("我給你1000元")
# else:
#     print("你給我100元")

#6.如果 你沒有考100分 或沒有下雨
#   我給你1000元
#否則你給我100元
# score_1=80
# rainy_1 = True
# if score!=100 or not(rainy_1):
#     print("我給你1000元")
# else:
#     print("你給我100元")

def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3

print(max_num(10,3,5))