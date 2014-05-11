# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 00:50:18 2014

@author: Cobzak
"""

from numpy import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
#1100
N=100
l=1

u = zeros((N,N))
print u
u[0,:] =100
print u
eps=0.15
z=0
k=0
while (trace(u)-z)>eps: 
    print(trace(u)-z)
    z=trace(u)
    u[1:-1,1:-1]=(u[2:,1:-1]+u[:-2,1:-1]+u[1:-1,:-2]+u[1:-1,2:])/4.
    k=k+1
print 'uu',k
x=[float(j)/N for j in range(N)]
y=[float(j)/N for j in range(N)]
print u
#write(u,N)
x,y=meshgrid(x,y)

fig = plt.figure()
ax = fig.gca(projection='3d')

surf = ax.plot_surface(u,x,y, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
#ax.set_zlim(-1.01, 1.01)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

        

