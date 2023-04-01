#函式 function
def hello(name,age):
    print("hello"+name+"你今年"+str(age)+"歲")

hello("小白",87)

def add(num1,num2): 
    print(num1+num2)
    return 10 #沒有return時，會自動定義

value = add(3,4)
print(value)