import numpy as np
a= np.random.randint(20, size=15)
print("Array is", a)
b= a.reshape((3,5))
print("Reshaped array is", b)
c= np.where(b == np.max(b,axis=1).reshape(-1,1),0*b, b)
print("Modified array is",c)

