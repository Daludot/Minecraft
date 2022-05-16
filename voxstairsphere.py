#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 18:59:27 2022

@author: danieldotson
"""
import matplotlib.pyplot as plt
import numpy as np

bc=True
R=8

blocks=np.array([[1,1,1,1,1,1,1,1],
                 [0,0,0,0,0,0,0,0],
                 [1,0,1,0,1,0,1,0],
                 [0,1,0,1,0,1,0,1],
                 [0,1,0,1,1,1,1,1],
                 [0,1,1,1,0,1,1,1],
                 [1,1,1,1,0,1,0,1],
                 [1,1,0,1,1,1,0,1],
                 [1,0,1,0,1,1,1,1],
                 [1,0,1,1,1,0,1,1],
                 [1,1,1,1,1,0,1,0],
                 [1,1,1,0,1,1,1,0]])

if (bc and int(3*R)%2==0) or (bc==False and int(3*R)%2==1):
    N=int(3*R)+1
else:
    N=int(3*R)
Ns=2*N

xcent=np.linspace(-N/2+0.25,N/2-0.25,Ns)
ycent=np.linspace(-N/2+0.25,N/2-0.25,Ns)
zcent=np.linspace(-N/2+0.25,N/2-0.25,Ns)
Xcent,Ycent,Zcent=np.meshgrid(xcent,ycent,zcent)

xcorn=np.linspace(-N/2,N/2,Ns+1)
ycorn=np.linspace(-N/2,N/2,Ns+1)
zcorn=np.linspace(-N/2,N/2,Ns+1)
Xcorn,Ycorn,Zcorn=np.meshgrid(xcorn,ycorn,zcorn)

sphere=np.sqrt(Xcent**2+Ycent**2+Zcent**2)<=R

colors=np.zeros([np.shape(Xcent)[0],np.shape(Xcent)[1],np.shape(Xcent)[2],3])
for i in range(0,np.shape(colors)[0]-1,2):
    for j in range(0,np.shape(colors)[1]-1,2):
        for k in range(0,np.shape(colors)[2]-1,2):
            colors[i:(i+2),j:(j+2),k:(k+2),:]=np.random.rand(3)

for i in range(0,np.shape(colors)[0]-1,2):
    for j in range(0,np.shape(colors)[1]-1,2):
        for k in range(0,np.shape(colors)[2]-1,2):
            test=sphere[i:(i+2),j:(j+2),k:(k+2)].flatten()
            score=np.zeros(np.shape(blocks)[0])
            for bi in range(np.shape(blocks)[0]):
                score[bi]=np.sum(np.abs(blocks[bi,:]-test))
            bwin=np.argmin(score)
            sphere[i:(i+2),j:(j+2),k:(k+2)]=np.array(np.reshape(blocks[bwin,:],(2,2,2)),dtype=bool)
                

ax = plt.axes(projection='3d')
ax.voxels(Xcorn,Ycorn,Zcorn,filled=sphere,facecolors=colors)
plt.xlim([-N/2,N/2])
plt.ylim([-N/2,N/2])
ax.set_zlim([-N/2,N/2])
ax.set_axis_off()
ax.set_box_aspect(aspect = (1,1,1))
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.tight_layout()