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

qq=vector(12.,-12.,5.)
q=vector(1.,-2.,5.)
vv=vector(0.,2.,5.)
v=vector(2.,0.,5.)
g=vector(0.,0.,-10.)
print v.z
ball = sphere(pos=qq, radius=0.5, color=color.magenta)
bal = sphere(pos=q, radius=0.5, color=color.magenta)
rod = cylinder(pos=ball.pos,axis=-ball.pos+bal.pos, radius=0.1, color=color.magenta)
wallR = box(pos=(0.,0.,-10), size=(20,20,0.2), color=color.cyan)
ball.velocity = v
bal.velocity = v
deltat = 0.005
t = 0
tau= 0
flag=false

#print ball.pos.z, ball.velocity.z, wallR.pos.z
while t < 10:
    rate(100)       
    if ball.pos.z < wallR.pos.z+wallR.size.z-ball.radius:
        ball.velocity.z = -ball.velocity.z
    ball.pos = ball.pos + ball.velocity*deltat+(g*(deltat*deltat))/2.
    ball.velocity=ball.velocity+g*deltat
    if bal.pos.z < wallR.pos.z-bal.radius+wallR.size.z:
        bal.velocity.z = -bal.velocity.z
    bal.pos = bal.pos + bal.velocity*deltat+(g*(deltat*deltat))/2.
    bal.velocity=bal.velocity+g*deltat
    rod.pos=ball.pos
    rod.axis=-ball.pos+bal.pos
    #print ball.pos.z, wallR.pos.z, ball.velocity.z
    t=t+deltat