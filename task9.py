#Найти максимальную цифру в числе
a=input("введите число")
max=int(a)%10
b=1
n=len(a)
for i in range(len(a)):
    a=int(a)
    b = a % 10

    if b > max:
        max=b
        a = a // 10
    else:   a = a // 10

print(max)