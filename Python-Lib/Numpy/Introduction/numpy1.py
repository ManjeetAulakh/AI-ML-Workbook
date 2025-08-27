import numpy as np

x = np.array([1,2,3,4])
print(x)
print(type(x))

y = [1,2,3,4]
print(y)
print(type(y))

'''

range(1,9) give number from 1 to 8 and  for each j has power 4 means [1**4, 2**4.... 8**4]  = [1,16....]

%timeit give exuation time of single line
%%timeit give excution time for whole program

The error occurs because %timeit is not valid Python syntax in a standard Python script. 
It is an IPython magic command, which is specific to IPython or Jupyter Notebook environments. 


%timeit [j**4 for j in range(1,9)]

%timeit np.arange(1,9)**4



'''




