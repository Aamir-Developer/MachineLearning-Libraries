import numpy as np

a = np.array([1, 2, 3])
print(type(a))
print(a.shape)
print(a[0], a[1], a[2])
a[0] = 5
print(a[0])

b = np.array([[1, 2, 3], [4, 5, 6]])
print(type(b))
print(b.shape)
print(b[0, 0], b[0, 1], b[0, 2], b[1, 0], b[1, 1], b[1, 2])

c = np.zeros((3, 3))
print(c)

d = np.ones((2, 2))
print(d)

e = np.full((2,2), 5)
print(e)

f = np.eye(4, 4)
print(f)

g = np.random.random(5)
print(g)