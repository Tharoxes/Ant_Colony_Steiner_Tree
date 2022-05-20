import numpy as np

thisdict = {
    1: {'hallo': 'John'}
}

print(thisdict[1]['hallo'])

arr = np.array([[0,1, 324], [1, 2, 2143], [3, 4, 135]])

a = np.where([0,1, 324] == arr)
b = np.where([0,1, 324] == arr)[0][0]
c = a[0]
d = a[1]
print(c)
print(d)
print(b)