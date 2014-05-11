# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 10:25:54 2014

@author: t08-32
"""


from visual import *

def norma(r):
    return (r[0])**2+(r[1])**2+(r[2])**2
    
scene.background=(1,1,1)
scene.width=1280
scene.height=1024
k=(0,0,1)
k = color.rgb_to_hsv(k)
#s=(raw_input("Enter position of your b(x,y,z)"))
#q=map(float, s.split(','))
#print q
#s=(raw_input("Enter velocity of your b(Vx,Vy,Vz)"))
#v=map(float, s.split(','))
#print v

q1=vector(0.,-5.,4.)
q2=vector(0.,0.,3.)
v1=vector(0.,0.,0.)
v2=vector(-0.,-0.,0.)
g=vector(0.,0.,-2.)
m1=1
m2=2

b1 = sphere(pos=q1, radius=1, color=color.magenta)
b2 = sphere(pos=q2, radius=1, color=color.magenta)
rod = cylinder(pos=b1.pos,axis=-b1.pos+b2.pos, radius=0.1, color=color.magenta)
wallR = box(pos=(0.,0.,-10), size=(20,20,0.2), color=color.cyan)
b1.velocity = v1
b2.velocity = v2
deltat = 0.0001
l=norma(-b1.pos+b2.pos)
t = 0
tau= 0
flag=false
M=m1+m2
c=(m1*b1.pos+m2*b2.pos)/M
vc=(m1*b1.velocity+m2*b2.velocity)/M
R1=l*m2/M
R2=l*m1/M
#print b.pos.z, b.velocity.z, wallR.pos.z
while t < 10:
    rate(1000000000)       
    if b1.pos.z < wallR.pos.z+b1.radius:
        b2.velocity=(M*vc-m1*b1.velocity)/m2
        b1.velocity.z = -b1.velocity.z
        vc=(m1*b1.velocity+m2*b2.velocity)/M
    if b2.pos.z < wallR.pos.z+b2.radius:
        b1.velocity=(M*vc-m2*b2.velocity)/m1
        b2.velocity.z = -b2.velocity.z
        vc=(m1*b1.velocity+m2*b2.velocity)/M
        
    #print b.pos.z, wallR.pos.z, b.velocity.z
    r=b2.pos-b1.pos
    
    b1.pos = b1.pos + b1.velocity*deltat+((g+((r/norma(r))*(norma(b1.velocity))**2)/R1)*(deltat*deltat))/2
    b2.pos = b2.pos + b2.velocity*deltat+((g-((r/norma(r))*(norma(b2.velocity))**2)/R2)*(deltat*deltat))/2
    b1.velocity=b1.velocity+(g+((r/norma(r))*(norma(b1.velocity))**2)/R1)*deltat
    b2.velocity=b2.velocity+(g-((r/norma(r))*(norma(b2.velocity))**2)/R2)*deltat
    c=(m1*b1.pos+m2*b2.pos)/M
    c=c+vc*deltat+g*deltat*deltat/2.
    vc=(m1*b1.velocity+m2*b2.velocity)/M+g*deltat
#    vc=vc+g*deltat
    r=(b2.pos-b1.pos)
    
    b1.pos=c-l*r*m2/(norma(r)*M)
    b2.pos=c+l*r*m1/(norma(r)*M)
    t=t+deltat