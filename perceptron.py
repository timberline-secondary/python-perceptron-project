import matplotlib.pyplot as plt

x = [0,1,2,3,4]
y = [x**x for x in x]

plt.plot(x, y)

plt.show()