# -*- coding: utf-8 -*-
"""
Created on Sat Mar 01 09:05:40 2014

@author: t08-32
"""

from numpy import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt

N=100
l=1
K=100

x=linspace(0,l,num=K)
y=linspace(0,l,num=K)
x,y=meshgrid(x,y)
u=zeros((K,K))
for i in range(1,N,2):
    u=400*sin(pi*i*x/l)*sinh(pi*i*y/l)/(pi*i*sinh(pi*i))+u
fig = plt.figure()
ax = fig.gca(projection='3d')

surf = ax.plot_surface(x,y,u, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
#ax.set_zlim(-1.01, 1.01)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

