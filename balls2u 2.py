# -*- coding: utf-8 -*-
"""
Created on Sat Apr 05 00:32:17 2014

@author: Cobzak
"""

from visual import *

scene.background=(1,1,1)
scene.width=1280
scene.height=1024
k=(0,0,1)
k = color.rgb_to_hsv(k)
#s=(raw_input("Enter position of your ball(x,y,z)"))
#q=map(float, s.split(','))
#print q
#s=(raw_input("Enter velocity of your ball(Vx,Vy,Vz)"))
#v=map(float, s.split(','))
#print v

q=vector(12.,-12.,5.)
v=vector(0.,3.,5.)
g=vector(0.,0.,-10.)
print v.z
ball = sphere(pos=q, radius=0.5, color=color.magenta)
wallR = box(pos=(0.,0.,-10), size=(20,20,0.2), color=color.cyan)
ball.velocity = v
deltat = 0.005
t = 0
tau= 0
flag=false
#print ball.pos.z, ball.velocity.z, wallR.pos.z
while t < 10:
    rate(100)       
    if ball.pos.z < wallR.pos.z+ball.radius:
        ball.velocity.z = -ball.velocity.z
    ball.pos = ball.pos + ball.velocity*deltat+(g*(deltat*deltat))/2.
    ball.velocity=ball.velocity+g*deltat
    #print ball.pos.z, wallR.pos.z, ball.velocity.z
    t=t+deltat