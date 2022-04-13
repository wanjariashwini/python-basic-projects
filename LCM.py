n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))

if n1>n2:
   s = n2
   b = n1
else:
    s = n1
    b = n2

if n1 == n2:
    print("LCM IS ",n1)
else:
    i = 1
    while(i):
        f = b*i
        i+=1
        if f%s == 0:
          print("LCM is : ",f)
          break
        else:
          continue
