#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import heapq as hq
import copy


# In[13]:



#backtracking function, takes parent node from explored nodes and stores the coordinates of the path in a new list
def Backtrack(S,start_node,goal_node,canvas):
    #fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    #out = cv2.VideoWriter('Dijkstra.avi',fourcc,1000,(canvas.shape[1],canvas.shape[0]))
    explored_nodes=S.keys()
    navigation=[]
    navigation.append(goal_node)
    for node in explored_nodes:
        canvas[node[0]][node[1]]=[255,255,255]
        cv2.imshow("Nodes Exploration",canvas)
        cv2.waitKey(1)
       # out.write(canvas)
    parent=S[tuple(goal_node)]
    while(parent!=start_node):
        navigation.append(parent)
        parent=S[tuple(parent)]
    navigation.append(start_node)
    start=copy.deepcopy(start_node)
    goal=copy.deepcopy(goal_node)
    start.reverse()
    goal.reverse()
    cv2.circle(canvas,tuple(start),3,(0,255,0),-1)           #draw green and red circles representing the start & goal
    cv2.circle(canvas,tuple(goal),3,(0,0,255),-1)
    while(len(navigation)>0):
        path_node = navigation.pop()
        canvas[path_node[0]][path_node[1]] = [184,13,218]
        #out.write(canvas)
    
    cv2.imshow("Nodes Exploration",canvas)
    #out.release()
    print(navigation)
    
#move-up     
def Move_up(node,canvas):
    #print(node)
    current_node = copy.deepcopy(node)
    #print(current_node)
    next_node=[current_node[0],current_node[1]-1]
    #print(canvas[current_node[0]][current_node[1]-1] )
    
    #node should not be in obstacle space
    if(current_node[1] > 0) and (canvas[next_node[0]][next_node[1]][0]==0) and  (canvas[next_node[0]][next_node[1]][2]==0):
        return tuple(next_node)
    else:
        return None
    
    
def Move_down(node,canvas):
    
    current_node = copy.deepcopy(node)
    next_node=[current_node[0],current_node[1]+1]
    
    if(next_node[1] < 250) and (canvas[next_node[0]][next_node[1]][0]==0) and  (canvas[next_node[0]][next_node[1]][2]==0):
        return tuple(next_node)
    else:
        return None
    
    
def Move_right(node,canvas):
    
    current_node = copy.deepcopy(node)
    next_node=[current_node[0]+1,current_node[1]]
    
    if(next_node[0] < 600) and (canvas[next_node[0]][next_node[1]][0]==0) and (canvas[next_node[0]][next_node[1]][2]==0):
        return tuple(next_node)
    else:
        return None
    
    
def Move_left(node,canvas):
    
    current_node = copy.deepcopy(node)
    next_node=[current_node[0]-1,current_node[1]]
    
    if(next_node[0] > 0) and (canvas[next_node[0]][next_node[1]][0]==0) and (canvas[next_node[0]][next_node[1]][2]==0):
        return tuple(next_node)
    else:
        return None
    
    
def move_left_up(node,canvas):
    
    current_node = copy.deepcopy(node)
    next_node=[current_node[0]-1,current_node[1]]
    
    if(next_node[1] > 0) and (next_node[0] > 0) and (canvas[next_node[0]][next_node[1]][0]==0) and (canvas[next_node[0]][next_node[1]][2]==0):
        return tuple(next_node)
    else:
        return None

def move_right_up(node,canvas):
    
    current_node = copy.deepcopy(node)
    next_node=[current_node[0]-1,current_node[1]]
    
    if(next_node[1] > 0) and (next_node[0] < 600) and  (canvas[next_node[0]][next_node[1]][0]==0) and (canvas[next_node[0]][next_node[1]][2]==0):
        return tuple(next_node)
    else:
        return None
    
    
def move_right_down(node,canvas):
    
    current_node = copy.deepcopy(node)
    next_node=[current_node[0]-1,current_node[1]]
    
    if(next_node[1] < 250) and (next_node[0] < 600) and  (canvas[next_node[0]][next_node[1]][0]==0) and (canvas[next_node[0]][next_node[1]][2]==0):
        return tuple(next_node)
    else:
        return None
    
    
def move_left_down(node,canvas):
    
    current_node = copy.deepcopy(node)
    next_node=[current_node[0]-1,current_node[1]]
    
    if(next_node[1] < 250) and (next_node[0] > 0) and (canvas[next_node[0]][next_node[1]][0]==0) and (canvas[next_node[0]][next_node[1]][2]==0):
        return tuple(next_node)
    else:
        return None

    
    


# In[14]:


def Dijkstra(start_node, goal_node,canvas):
    S={}
    PQ=[]
    temp=0
    hq.heapify(PQ)
    hq.heappush(PQ,[0,start_node,start_node])   #PQ= priority Queue. Elements: cost,parent,present
    while(len(PQ)!=0):
        node=hq.heappop(PQ)
        S[(node[2][0],node[2][1])]=node[1]
        present_cost=node[0]
        if(list(node[2])==goal_node):
            print("\n------\nGOAL REACHED\n--------\n")
            Backtrack(S,start_node,goal_node,canvas)
            temp=1
            break;
        #actions
        
        
        next_node=Move_up(node[2],canvas)
        #print(next_node)                 
        next_node1=Move_down(node[2],canvas)
        next_node2=Move_left(node[2],canvas)
        next_node3=Move_right(node[2],canvas)
        next_node4=move_right_down(node[2],canvas)
        next_node5=move_right_up(node[2],canvas)
        next_node6=move_left_down(node[2],canvas)
        next_node7=move_left_up(node[2],canvas)
        
        if(next_node):
          
            if(next_node not in S):
                flag=0
                for i in range(len(PQ)):
                    if(PQ[i][2]==[next_node[0],next_node[1]]):
                        flag=1
                        #print(i)
                        if(PQ[i][0]>(present_cost+1)):
                            PQ[i][0]=present_cost+1
                            PQ[i][1]=node[2]
                            hq.heapify(PQ)
                        break; #breaks for- no point in continuing after finding the index
                if(flag==0):
                    hq.heappush(PQ,[present_cost+1,node[2],[next_node[0],next_node[1]]])
                    hq.heapify(PQ)
                    
                    
        if(next_node1):
            
            if(next_node1 not in S):
                flag=0
                for i in range(len(PQ)):
                    if(PQ[i][2]==[next_node1[0],next_node1[1]]):
                        flag=1
                        if(PQ[i][0]>present_cost+1):
                            PQ[i][0]=present_cost+1
                            PQ[i][1]=node[2]
                            hq.heapify(PQ)
                        break;
                if(flag==0):
                    hq.heappush(PQ,[present_cost+1,node[2],[next_node1[0],next_node1[1]]])
                    hq.heapify(PQ)
                    
                    
        
        if(next_node2):
            
            if(next_node2 not in S):
                flag=0
                for i in range(len(PQ)):
                    if(PQ[i][2]==[next_node2[0],next_node2[1]]):
                        flag=1
                        if(PQ[i][0]>present_cost+1):
                            PQ[i][0]=present_cost+1
                            PQ[i][1]=node[2]
                            hq.heapify(PQ)
                        break;
                if(flag==0):
                    hq.heappush(PQ,[present_cost+1,node[2],[next_node2[0],next_node2[1]]])
                    hq.heapify(PQ)
                    
                    
                    
                    
        
        if(next_node3):
            
            if(next_node3 not in S):
                flag=0
                for i in range(len(PQ)):
                    if(PQ[i][2]==[next_node3[0],next_node3[1]]):
                        flag=1
                        if(PQ[i][0]>present_cost+1):
                            PQ[i][0]=present_cost+1
                            PQ[i][1]=node[2]
                            hq.heapify(PQ)
                        break;
                if(flag==0):
                    hq.heappush(PQ,[present_cost+1,node[2],[next_node3[0],next_node3[1]]])
                    hq.heapify(PQ)
                    
                    
        
        
        
        if(next_node4):
            
            if(next_node4 not in S):
                flag=0
                for i in range(len(PQ)):
                    if(PQ[i][2]==[next_node4[0],next_node4[1]]):
                        flag=1
                        if(PQ[i][0]>present_cost+1.4):
                            PQ[i][0]=present_cost+1.4
                            PQ[i][1]=node[2]
                            hq.heapify(PQ)
                        break;
                if(flag==0):
                    hq.heappush(PQ,[present_cost+1.4,node[2],[next_node4[0],next_node4[1]]])
                    hq.heapify(PQ)
                    
                    
                    
        
        if(next_node5):
            
            if(next_node5 not in S):
                flag=0
                for i in range(len(PQ)):
                    if(PQ[i][2]==[next_node5[0],next_node5[1]]):
                        flag=1
                        if(PQ[i][0]>present_cost+1.4):
                            PQ[i][0]=present_cost+1.4
                            PQ[i][1]=node[2]
                            hq.heapify(PQ)
                        break;
                if(flag==0):
                    hq.heappush(PQ,[present_cost+1.4,node[2],[next_node5[0],next_node5[1]]])
                    hq.heapify(PQ)
                    
                    
        
        if(next_node6):
            
            if(next_node6 not in S):
                flag=0
                for i in range(len(PQ)):
                    if(PQ[i][2]==[next_node6[0],next_node6[1]]):
                        flag=1
                        if(PQ[i][0]>present_cost+1.4):
                            PQ[i][0]=present_cost+1.4
                            PQ[i][1]=node[2]
                            hq.heapify(PQ)
                        break;
                if(flag==0):
                    hq.heappush(PQ,[present_cost+1.4,node[2],[next_node6[0],next_node6[1]]])
                    hq.heapify(PQ)
                    
                    
                    
        
        if(next_node7):
            
            if(next_node7 not in S):
                flag=0
                for i in range(len(PQ)):
                    if(PQ[i][2]==[next_node7[0],next_node7[1]]):
                        flag=1
                        if(PQ[i][0]>present_cost+1.4):
                            PQ[i][0]=present_cost+1.4
                            PQ[i][1]=node[2]
                            hq.heapify(PQ)
                        break;
                if(flag==0):
                    hq.heappush(PQ,[present_cost+1.4,node[2],[next_node7[0],next_node7[1]]])
                    hq.heapify(PQ)
                    
                    
                    
                    
                    
   
        
    if temp==0 :
        print("Goal cannot be reached")


# In[19]:


if __name__ == '__main__':
    start=[]
    goal=[]
    canvas = np.zeros((250, 600, 3), dtype='uint8')

    center_x, center_y = canvas.shape[1] // 2, canvas.shape[0] // 2

    
    radius = 75
    radius1=80

# calculate the vertices of the hexagon
    vertices = []
    vertices_bloat=[]
    rect1_bloat=[]
    for i in range(6):
        x = center_x + radius * np.cos(i * np.pi / 3)
        y = center_y + radius * np.sin(i * np.pi / 3)
        vertices.append((int(x), int(y)))
    
    for i in range(6):
        x = center_x + radius1 * np.cos(i * np.pi / 3)
        y = center_y + radius1 * np.sin(i * np.pi / 3)
        vertices_bloat.append((int(x), int(y)))

# draw the hexagon on the canvas
    cv2.fillPoly(canvas,[np.array(vertices_bloat)],(0,0,255))
    cv2.fillPoly(canvas, [np.array(vertices)], (255,0,0))
#canvas[245,595]=(0,0,255)
#cv2.rectangle(canvas, (0,0), (250, 600), (0, 0,255), thickness=5)
#cv2.circle(canvas, (50,50), radius=2, color=(0, 0, 255), thickness=-1)
#cv2.rectangle(canvas, (0, 0), (canvas.shape[1] - 1, canvas.shape[0] - 1), (0, 0, 255), 5)
    print(canvas.shape)

# show the canvas
    M = cv2.getRotationMatrix2D((center_x, center_y), 90, 1.0)
    canvas = cv2.warpAffine(canvas, M, (canvas.shape[1], canvas.shape[0]))

    rectangle1=[[100,0],[150,0],[150,100],[100,100]]
    rect_1_bloat=[[95,0],[95,105],[155,105],[155,0]]

    rectangle2=[[100,150],[150,150],[150,250],[100,250]]
    rect_2_bloat=[[95,145],[155,145],[155,255],[95,255]]

    triangle=[[460,25],[510,125],[460,225]]
    triangle_bloat=[[455,5],[515,125],[455,245]]
    vertices1=np.array(rectangle1,dtype=np.int32)
    vertices2=np.array(rectangle2,dtype=np.int32)
    vertices3=np.array(triangle,dtype=np.int32)

    cv2.rectangle(canvas, (0, 0), (canvas.shape[1] - 1, canvas.shape[0] - 1), (0, 0, 255), 5)

#cv2.polylines(canvas,[vertices_tri_bloat],True,(0,0,255),thickness=5)
#cv2.fillPoly(canvas,[np.array(vertices_tri_bloat)],(0,0,255))
    cv2.fillPoly(canvas, [np.array(rect_1_bloat)], (0, 0, 255))
    cv2.fillPoly(canvas, [np.array(rect_2_bloat)], (0, 0, 255))
    cv2.fillPoly(canvas, [np.array(triangle_bloat)], (0, 0, 255))


    cv2.fillPoly(canvas, [np.array(vertices1)], (255, 0, 0))
    cv2.fillPoly(canvas, [np.array(vertices2)], (255, 0, 0))
    cv2.fillPoly(canvas, [np.array(vertices3)], (255,0,0))


#cv2.fillPoly(new_canvas, [np.array(vertices)], (255,0,0))


# show the rotated canvas
    #cv2.imshow('Canvas', canvas)
    
    print(canvas.shape)
    while(1):
        x1=input( "Enter initial state (x): ")
        y1=input( "Enter initial state (y): ")
        start.append(250-int(y1))
        start.append(int(x1))
        
        x2=input( "Enter goal state (x): ")
        
        y2=input( "Enter goal state (y): ")
        goal.append(250-int(y2))
        goal.append(int(x2))
        
        
        if(int(x1) > 600 or int(y1)>250 or int(x2) > 600 or int(y2)>250):
            print("enter the coordinates within the framework (600,250)")
            
        elif canvas[int(y2)][int(x2)][0]!=0 or canvas[int(y2)][int(x2)][1]!=0 or canvas[int(y2)][int(x2)][2]!=0:
            print("Goal in obstacle space,  try again")
            
        elif canvas[int(y1)][int(x1)][0]!=0 or canvas[int(y1)][int(x1)][1]!=0 or canvas[int(y1)][int(x1)][2]!=0:
            print("Start node in obstacle space, try again")
            
        
            
        else:
            break;
        
    
    Dijkstra(start,goal,canvas) #Compute the path using Dijkstra Algorithm
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# In[ ]:




