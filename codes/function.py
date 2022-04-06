import numpy as np
import matplotlib.pyplot as plt

mylist=[]
x = np.linspace(-100,100)
y = (8*x+3)/(5*x-8)

mylist.append(y)
count=0

'''This for loops checks for any repeatation of element
    if duplicate elements are found then the function is not one-one
'''
for i in range(len(mylist)):
    for j in range(len(mylist)-1):
        if(mylist[i]==mylist[j+1]):
            count = count+1

if(count != 0):
    print("The function is not one-one\n")
else:
    print("The function is one-one\n")

'''
If we plug in inverse function then domain becomes codomain
if for every element in codomain there exist an image then the function is onto
even we can have multiple images in this case
'''
#The only case it fails to prove onto is if for any element if there doesnot exist image then it is not onto

newlist=[]
a=np.linspace(-100,100)
b=(8*a+3)/(5*a-8)

print("The function is onto")
plt.grid()
plt.plot(a,b)
plt.title("Plotting of $f(x)$ = $\dfrac{(8x+3)}{(5x-8)}$ inverse funtion")
plt.show()