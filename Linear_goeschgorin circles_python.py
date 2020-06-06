#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#program to plot goeshgorin circles(method of estimating eigen vectors in case of large matrices)
#when the dimensions of the matrix are too large,it becomes really difficult to calculate the eigen values as the polynomial is 
#of nth order.Here it is estimated that the eigen values lie inside the area swept by the goeschgorin circles.
# test case -2
# 2
# 3
# 2
# 1
# -6
# -1
# -2
# 0
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'notebook')
fig, ax = plt.subplots()
n=int(input("enter the dimensions of nXn matrix"))#takes the size of the transformation matrix
coef=[]
de=[]
print("enter the elements of the transformation matrix")#takes elements as the input
for i in range(0,n*n):
    ele=coef.append(int(input("")))
b=np.reshape(coef,(n,n))
de=np.diag(b)#stores the elements of the digonal of the nXn matrix
print(de)
s1=b.sum(axis=1)
print(s1)
s2=[]
for j in range(len(s1)):#used for calculating the radius of the goeschgorin circle 
    p=s1[j]-de[j]
    s2.append(p)
print(s2)
for k in range(len(s1)):
    ax.add_patch(plt.Circle((de[k],0),s2[k], color='pink', alpha=0.5))#draws a circle with centre at the the diagonal element 
    #and radius equal to the sum of elements in a row excluding the diagonal element.
    ax.set_aspect('equal', adjustable='datalim')
    plt.scatter(de[k],0, s=50,edgecolors='black',c='black')
    ax.plot()  
plt.show()
#now in the graph,it can inferred that the eigen values the matrix lie anywhere inside the union of these circles.
#If the circles are non-intersecting,then the circles are considered independently.


# In[ ]:




