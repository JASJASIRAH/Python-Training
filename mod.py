def biggest(n1,n2,n3):
    if n1>n2 and n1>n3:
        highest=n1
    elif n2>n1 and n2>n3:
        highest=n2
    else:
        highest=n3
    return highest

print("the biggest number is",biggest(4,9,10))

def add(n1, n2):
     return n1+n2
print(add(8,90))