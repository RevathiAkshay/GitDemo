#while loop
a= 5
while a > 1:
    print(a)
    a = a-1

print("loop ends")

#if we need to add condition within while loop
a=10
while a >1:
    if a!=3:
        print(a)
    a= a - 1
print("end of While")
print("*******************************")

##break and continue
# break will just comes out of the while loop
#continue will skip all the lines after the continue word and goes to while loop it will go to next iteration
print("*******************************")
p= 10
while p>1:
    if p==9:
        p=p-1
        continue
    if p==3:
        break
    print(p)
    p=p-1
print("*******************************")