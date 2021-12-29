# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 21:50:50 2019

@author: ASUS
"""
import numpy as np
from PIL import Image
import cv2
import time
import pylab
import matplotlib.pyplot as plt
import math 

# 0,0 80,80 80,80 0,0
#0,0 80,80 40,0 40,80

src = [40,0]
dest = [40,80]

srcx = src[0]
srcy = src[1]
destx = dest[0]
desty = dest[1]

src2 = [40,80]
dest2 = [40,0]

src2x = src2[0]
src2y = src2[1]
dest2x = dest2[0]
dest2y = dest2[1]

newdesx =0 
newdesy = 0

def move(newx,newy,orgx,orgy,destx,desty,obs):
    global newdesx
    global newdesy
    flag1=0
    flag2=0
    global src1,src2,src21,src22
    
    if destx == 0 and destx > orgx:
        errx =  1
        flag1 = 1
        
    if desty == 0 and desty > orgy:
        erry =  1
        flag2 = 1
        
    if destx == 0 and destx < orgx:
        errx = -1
        flag1 = 1
        
    if desty == 0 and desty < orgy:
        erry = -1
        flag2 = 1
        
    if destx == newx or abs(destx - newx) <= 0.5:
        errx = 0
        flag1 = 1
        
    if desty == newy or abs(desty - newy) <= 0.5:
        erry = 0
        flag2 = 1

    if flag1 == 0:
        errx = (destx - newx)/abs(destx)
    if flag2 == 0:
        erry = (desty - newy)/abs(desty)
    

    if  errx > 1:
        errx = 1
    if erry > 1:
        erry = 1
    if errx < -1:
        errx = -1
    if erry < -1:
        erry = -1
        
    if errx > 0 and errx < 1:
        errx = 1
    if erry > 0 and erry < 1:
        erry = 1
    if errx < 0 and errx > -1:
        errx = -1
    if erry < 0 and erry > -1:
        erry = -1
        
    print("errx",errx,"erry",erry)
        

    newdesx =  newx + errx
    newdesy =  newy + erry
    
    if abs(src1 - dest1) == 0.5:
        src1 = src1 + 0.5
        
    if abs(src2 - dest2) == 0.5:
        src2 = src2 + 0.5
        
    if abs(src21 - dest21) == 0.5:
        src21 = src21 + 0.5
        
    if abs(src22 - dest22) == 0.5:
        src22 = src22 + 0.5
    
    print("newdesx",newdesx,"newdesy",newdesy)
    
    return newdesx,newdesy


def GetObstacle(x1,y1,x2,y2):
    dist = 0
    #for car in cars:
    sq1 = x2 - x1
    sq2 = y2 - y1
    sq1*=sq1
    sq2*=sq2
    sq3 = sq1 + sq2
    dist = math.sqrt(sq3)
    print("dist",dist)
    return dist

    
    
src1=srcx
src2=srcy
dest1=destx
dest2=desty

src21=src2x
src22=src2y
dest21=dest2x
dest22=dest2y

src3=srcx
src4=srcy
src23=src2x
src24=src2y
cd1 = []
cd2 = []
cd3 = []
cd4 = []


def difference(x1,y1,x2,y2,x3,y3,x4,y4,dist12,dist21):
    dis1 = 0
    dis2 = 0
    dis3 = 0
    dis4 = 0
    xx1 = x2 - x1
    yy1 = y2 - y1
    
    xx2 = x4 - x3
    yy2 = y4 - y3
    
    if xx1 > 0 and yy1 > 0 and xx2 < 0 and yy2 > 0:  #1
        dis1 = 1
        dis2 = 1
        dis3 = -1
        dis4 = -1
        
    if xx1 > 0 and yy1 > 0 and xx2 < 0 and yy2 < 0:  #2
        dis1 = 0.5
        dis2 = 2
        dis3 = -0.5
        dis4 = -2
        
    if xx1 > 0 and yy1 > 0 and xx2 == 0 and yy2 > 0:  #3
        dis1 = 0.5
        dis2 = -1
        dis3 = 0.5
        dis4 = 1
        
    if xx1 > 0 and yy1 > 0 and xx2 > 0 and yy2 == 0:  #4
        dis1 = 2
        dis2 = 1
        dis3 = 0.5
        dis4 = -1
        
    if xx1 > 0 and yy1 > 0 and xx2 > 0 and yy2 < 0:   #5
        dis1 = 2
        dis2 = 1
        dis3 = -1
        dis4 = -1
        
    if xx1 > 0 and yy1 > 0 and xx2 == 0 and yy2 < 0:  #6
        dis1 = 2
        dis2 = -1
        dis3 = -2
        dis4 = 0
        
    if xx1 > 0 and yy1 > 0 and xx2 < 0 and yy2 == 0:  #7
        dis1 = 2
        dis2 = -0.5
        dis3 = 0.5
        dis4 = 2
        
   #2 ******************************************************************************     
    if xx1 > 0 and yy1 == 0  and xx2 > 0 and yy2 > 0:  #8
        dis1 = 0.5
        dis2 = -2
        dis3 = 2
        dis4 = 0.5
        
    if xx1 > 0 and yy1 == 0 and xx2 > 0 and yy2 < 0:  #9
        dis1 = -0.5
        dis2 = 2
        dis3 = 2
        dis4 = -0.5
        
    if xx1 > 0 and yy1 == 0 and xx2 == 0 and yy2 < 0:  #10
        dis1 = 2
        dis2 = -1
        dis3 = -2
        dis4 = -1
        
    if xx1 > 0 and yy1 == 0 and xx2 < 0 and yy2 < 0:  #11
        dis1 = 2
        dis2 = -0.5
        dis3 = -2
        dis4 = -0.5
        
    if xx1 > 0 and yy1 == 0 and xx2 <0 and yy2 == 0 :  #12
        dis1 = 2
        dis2 = 2
        dis3 = -2
        dis4 = -2
    
    if xx1 > 0 and yy1 == 0 and xx2 < 0 and yy2 > 0:  #13
        dis1 = 1
        dis2 = 2
        dis3 = -1
        dis4 = -2
        
    if xx1 > 0 and yy1 == 0 and xx2 == 0 and yy2 > 0:  #14
        dis1 = 1
        dis2 = 2
        dis3 = -2
        dis4 = 1
        
 #3 ******************************************************************************    
        
    if xx1 > 0 and yy1 < 0 and xx2 > 0 and yy2 > 0:  #1
        dis1 = 2
        dis2 = 1
        dis3 = -1
        dis4 = 1
            
    if xx1 > 0 and yy1 < 0 and xx2 > 0 and yy2 == 0:  #2
        dis1 = 2
        dis2 = 1
        dis3 = -0.5
        dis4 = 1
      
    if xx1 > 0 and yy1 < 0 and xx2 == 0 and yy2 < 0:  #3
        dis1 = 1
        dis2 = 2
        dis3 = -2
        dis4 = 0
    
    if xx1 > 0 and yy1 < 0 and xx2 < 0 and yy2 < 0:  #4
        dis1 = 1
        dis2 = -2
        dis3 = -2
        dis4 = 1
       
    if xx1 > 0 and yy1 < 0 and xx2 < 0 and yy2 == 0: #5  
        dis1 = 1
        dis2 =0.5
        dis3 = -1
        dis4 = -0.5
    
    if xx1 > 0 and yy1 < 0 and xx2 < 0 and yy2 > 0:  #6
        dis1 = 0
        dis2 = -2
        dis3 = 0
        dis4 = 2

    if xx1 > 0 and yy1 < 0 and xx2 == 0 and yy2 > 0:  #7
        dis1 = 2
        dis2 = 0
        dis3 = -2
        dis4 = 1
        
#4*****************************************************************************************
        
    if xx1 == 0 and yy1 < 0 and xx2 > 0 and yy2 > 0:  #1
        dis1 = -2
        dis2 = -1
        dis3 = 2
        dis4 = 0
            
    if xx1 == 0 and yy1 < 0 and xx2 > 0 and yy2 == 0:  #2
        dis1 = -2
        dis2 = -1
        dis3 = 1
        dis4 = -2
    
    if xx1 == 0 and yy1 < 0 and xx2 > 0 and yy2 < 0:  #3
        dis1 = -2
        dis2 = 0
        dis3 =  0
        dis4 = -2
    
    if xx1 == 0 and yy1 < 0 and xx2 < 0 and yy2 < 0:  #4
        dis1 = -1
        dis2 = -2
        dis3 = -1
        dis4 = 2
    
    if xx1 == 0 and yy1 < 0 and xx2 < 0 and yy2 == 0:   #5
        dis1 =  2
        dis2 =  -1
        dis3 =  -1   
        dis4 =  -2
    
    if xx1 == 0 and yy1 < 0 and xx2 < 0 and yy2 > 0:  #6
        dis1 = -2
        dis2 = -1
        dis3 = -1
        dis4 = 2
    
    if xx1 == 0 and yy1 < 0 and xx2 == 0 and yy2 > 0:  #7
        dis1 = -2
        dis2 = -1
        dis3 = 2
        dis4 = 1
         
#5*******************************************************************************        
        
    if xx1 < 0 and yy1 < 0 and xx2 > 0 and yy2 > 0:  #1
        dis1 = 0
        dis2 = -2
        dis3 = 0
        dis4 = 2
            
    if xx1 < 0 and yy1 < 0 and xx2 > 0 and yy2 == 0:  #2
        dis1 = 0
        dis2 = -2
        dis3 = 0
        dis4 = 2
    
    if xx1 < 0 and yy1 < 0 and xx2 > 0 and yy2 < 0:  #3
        dis1 = 0
        dis2 = -2
        dis3 = 2
        dis4 = 1
    
    if xx1 < 0 and yy1 < 0 and xx2 == 0 and yy2 < 0:  #4  wrong
        dis1 = -1
        dis2 = -3
        dis3 = 1
        dis4 = -0.5
    
    if xx1 < 0 and yy1 < 0 and xx2 < 0 and yy2 == 0:   #5 wrong
        dis1 =  1
        dis2 =  -1
        dis3 =  -2   
        dis4 =  0
    
    if xx1 < 0 and yy1 < 0 and xx2 < 0 and yy2 > 0:  #6
        dis1 = 2
        dis2 = 0
        dis3 = -1
        dis4 = -1

    if xx1 < 0 and yy1 < 0 and xx2 == 0 and yy2 > 0:  #7
        dis1 = 0
        dis2 = -2
        dis3 = -2
        dis4 = 1
    
#6******************************************************************************* 
        
    if xx1 < 0 and yy1 == 0 and xx2 > 0 and yy2 > 0:  #1
        dis1 = 0
        dis2 = -2
        dis3 = 0
        dis4 = 2
            
    if xx1 < 0 and yy1 == 0 and xx2 > 0 and yy2 == 0:  #2
        dis1 = 0
        dis2 = -1
        dis3 = 1
        dis4 = 2
    
    if xx1 < 0 and yy1 == 0 and xx2 > 0 and yy2 < 0:  #3
        dis1 = 0
        dis2 = -2
        dis3 = 2
        dis4 = 1
    
    if xx1 < 0 and yy1 == 0 and xx2 == 0 and yy2 < 0:  #4  wrong
        dis1 = 0
        dis2 = 2
        dis3 = -2
        dis4 = 0
    
    if xx1 < 0 and yy1 == 0 and xx2 < 0 and yy2 < 0:   #5 other approach
        dis1 =  -2
        dis2 =  -1
        dis3 =  2   
        dis4 =  -1
    
    if xx1 < 0 and yy1 == 0 and xx2 < 0 and yy2 > 0:  #6
        dis1 = -2
        dis2 = 1
        dis3 = 1
        dis4 =  1

    if xx1 < 0 and yy1 == 0 and xx2 == 0 and yy2 > 0:  #7
        dis1 = -1
        dis2 =  2
        dis3 = 2
        dis4 = 1
        
#7******************************************************************************* 
        
    if xx1 < 0 and yy1 > 0 and xx2 > 0 and yy2 > 0:  #1
        dis1 = -1
        dis2 = -1
        dis3 = 1
        dis4 = 1
            
    if xx1 < 0 and yy1 > 0 and xx2 > 0 and yy2 == 0:  #2
        dis1 = -1
        dis2 = -1
        dis3 = 2
        dis4 = 2
    
    if xx1 < 0 and yy1 > 0 and xx2 > 0 and yy2 < 0:  #3
        dis1 = 0
        dis2 = -2
        dis3 = 0
        dis4 = 2
    
    if xx1 < 0 and yy1 > 0 and xx2 == 0 and yy2 < 0:  #4  
        dis1 = -1
        dis2 = -1
        dis3 = 2
        dis4 = 0
    
    if xx1 < 0 and yy1 > 0 and xx2 < 0 and yy2 < 0:   #5 
        dis1 =  -2
        dis2 =  1
        dis3 =  -2   
        dis4 =  0
    
    if xx1 < 0 and yy1 > 0 and xx2 < 0 and yy2 == 0:  #6
        dis1 = 2
        dis2 = 2
        dis3 = -1
        dis4 =  1

    if xx1 < 0 and yy1 > 0 and xx2 == 0 and yy2 > 0:  #7
        dis1 = -1
        dis2 =  -2
        dis3 = 1
        dis4 = 1
        
#8******************************************************************************* 
        
    if xx1 == 0 and yy1 > 0 and xx2 > 0 and yy2 > 0:  #1
        dis1 = 0.5
        dis2 = 1
        dis3 = 0.5
        dis4 = -1
            
    if xx1 == 0 and yy1 > 0 and xx2 > 0 and yy2 == 0:  #2
        dis1 = -2
        dis2 = 1
        dis3 = 1
        dis4 = 2
    
    if xx1 == 0 and yy1 > 0 and xx2 > 0 and yy2 < 0:  #3
        dis1 = -2
        dis2 = 1
        dis3 = 2
        dis4 = 0
    
    if xx1 == 0 and yy1 > 0 and xx2 == 0 and yy2 < 0:  #4  
        dis1 = 2
        dis2 = 1
        dis3 = -2
        dis4 = -1
    
    if xx1 == 0 and yy1 > 0 and xx2 < 0 and yy2 < 0:   #5 
        dis1 =  -2
        dis2 =  2
        dis3 =  2   
        dis4 =  0
    
    if xx1 == 0 and yy1 > 0 and xx2 < 0 and yy2 == 0:  #6
        dis1 = 2
        dis2 = 1
        dis3 = -2
        dis4 =  1

    if xx1 == 0 and yy1 > 0 and xx2 < 0 and yy2 > 0:  #7
        dis1 = 1
        dis2 = 1
        dis3 = -1
        dis4 = -2
    
    
    
 
        
    return dis1,dis2,dis3,dis4
    
    





time.sleep(5)
while src1 < dest1 or src2 < dest2 or src21 < dest21 or src22 < dest22:
        obsdist = GetObstacle(src1,src2,src21,src22)
        dist1,dist2 = move(src1,src2,src3,src4,dest1,dest2,obsdist)
        if obsdist < 10:
            dis1,dis2,dis3,dis4 = difference(src3,src4,dest1,dest2,src23,src24,dest21,dest22,dist1,dist2)
            dist1 = dist1 + dis1
            dist2 = dist2 + dis2
        print("dist1",dist1,"dist2",dist2)
        src1 = dist1
        src2 = dist2
        cd1.append(src1)
        cd2.append(src2)
        
        obsdist = GetObstacle(src21,src22,src1,src2)
        dist3,dist4 = move(src21,src22,src23,src24,dest21,dest22,obsdist)
        if obsdist < 10:
            print("in here")
            dis1,dis2,dis3,dis4 = difference(src3,src4,dest1,dest2,src23,src24,dest21,dest22,dist3,dist4)
            dist3 = dist3 + dis3
            dist4 = dist4 + dis4
        print("dist3",dist3,"dist4",dist4)
        src21 = dist3
        src22 = dist4
        cd3.append(src21)
        cd4.append(src22)
        
  
    
        env = np.zeros((90, 90, 3), dtype=np.uint8)
        env1 = np.zeros((90, 90, 3), dtype=np.uint8)
        env[int(src1)][int(src2)] = (255, 175, 0)
        env[int(src21)][int(src22)] = (255, 175, 0)
        #env[int(destx)][int(desty)] = (0, 0, 255)
        #env[int(dest2x)][int(dest2y)] = (0, 0, 255)
        img = Image.fromarray(env, 'RGB')  # reading to rgb. Apparently. Even tho color definitions are bgr. ???
        img = img.resize((1000, 1000))  # resizing so we can see our agent in all its glory.
        img1 = Image.fromarray(env1, 'RGB')  # reading to rgb. Apparently. Even tho color definitions are bgr. ???
        img1 = img.resize((1000, 1000))  # resizing so we can see our agent in all its glory.
        cv2.imshow("image", np.array(img))  # show it!
         # cv2.imshow("image1", np.array(img1))  # show it!
        if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        time.sleep(0.1)
            
while src1 > dest1 or src2 > dest2 or src21 < dest21 or src22 < dest22:
        obsdist = GetObstacle(src1,src2,src21,src22)
        dist5,dist6 = move(src1,src2,src3,src4,dest1,dest2,obsdist)
        if obsdist < 10:
            dis1,dis2,dis3,dis4 = difference(src3,src4,dest1,dest2,src21,src22,dest21,dest22,dist5,dist6)
            dist5 = dist5 + dis1
            dist6 = dist6 + dis2
        src1 = dist5
        src2 = dist6
        cd1.append(src1)
        cd2.append(src2)
        
     
        obsdist = GetObstacle(src1,src2,src21,src22)
        dist7,dist8 = move(src21,src22,src23,src24,dest21,dest22,obsdist)
        if obsdist < 10:
            dis1,dis2,dis3,dis4 = difference(src3,src4,dest1,dest2,src21,src22,dest21,dest22,dist7,dist8)
            dist7 = dist7 + dis1
            dist8 = dist8 + dis2
        src21 = dist7
        src22 = dist8
        cd3.append(src21)
        cd4.append(src22)
        
        env = np.zeros((90, 90, 3), dtype=np.uint8)
        env1 = np.zeros((90, 90, 3), dtype=np.uint8)
        env[int(src1)][int(src2)] = (255, 175, 0)
        env[int(src21)][int(src22)] = (255, 175, 0)
       # env[int(destx)][int(desty)] = (0, 0, 255)
       # env[int(destx)][int(desty)] = (0, 255, 0)
        img = Image.fromarray(env, 'RGB')  # reading to rgb. Apparently. Even tho color definitions are bgr. ???
        img = img.resize((1000, 1000))  # resizing so we can see our agent in all its glory.
        img1 = Image.fromarray(env1, 'RGB')  # reading to rgb. Apparently. Even tho color definitions are bgr. ???
        img1 = img.resize((1000, 1000))  # resizing so we can see our agent in all its glory.
        cv2.imshow("image", np.array(img))  # show it!
             # cv2.imshow("image1", np.array(img1))  # show it!
        if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
        time.sleep(0.05)
               
            
            
print("src1",src1)
print("src2",src2)

pylab.clf()
plt.plot(cd1,cd2,'-g',label = 'Car 1')
plt.plot(cd3,cd4,'-y',label = 'Car 2')
pylab.ylim([0,100])
pylab.xlim([0,100])
plt.xlabel('X-co-ordinate')
plt.ylabel('Y-co-ordinate')
plt.show()
    