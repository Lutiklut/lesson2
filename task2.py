#ввести 10 цифр, найти количество  5
b=0
for i in range(1,11,1):
    print("число",i)
    a=input()
    a=int(a)
    if a==5:
        b=b+1
    print(b)



