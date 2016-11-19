from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')
#z = how many he assists he passed
z = [2, 4, 5, 6, 7, 6, 6, 6, 5, 6, 6, 6, ]
# y = how many points he scored
y = [8, 15, 16, 18, 21, 19, 22, 21, 19, 20, 19, 14]
# x = what year
x = [1987, 1988, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]


# can plot specifically, after just showing the defaults:
plt.title('Scottie Pippen')
plt.ylabel('Y axis')
plt.xlabel('Year')

plt.show()

plt.plot(x,y,'g',label='Points', linewidth=5)
plt.plot(x,z,'c',label='Assists',linewidth=5)

plt.title('Scottie Pippen')
plt.ylabel('Numbers')
plt.xlabel('Year')

plt.legend()

plt.grid(True,color='k')

plt.show()