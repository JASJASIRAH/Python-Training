def add(x,y,*nos):
    print(type(nos))
    sum =0
    for e in nos:
        sum = sum+e
    return sum

def largest(*nos):
    r=0
    for r in nos:
        if(a>b) and (a>c):
            r=a
        elif(b>a)and(b>c):
            r=b
        else:
            r=c
            return r
a=int(input("enter no a:"))
b=int(input("enter no b:"))
c=int(input("enter no c:"))
print(a)
print(b)
print(c)
print("the largest number is:",(largest(a,b,c)))


