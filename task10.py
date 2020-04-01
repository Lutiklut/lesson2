#Найти количество цифр 5 в числе
a=input("введите число")
c=0
b=1
n=len(a)
for i in range(len(a)):
    a=int(a)
    b = a % 10

    if b == 5:
        c=c+1
        a = a // 10
    else:
       a = a // 10
print(c)