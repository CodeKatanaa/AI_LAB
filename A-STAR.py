#!/usr/bin/env python
# coding: utf-8

# In[1]:


graph=[['A','B',1,3],
       ['A','C',2,4],
       ['A','H',7,0],
       ['B','D',4,2],
       ['B','E',6,6],
       ['C','F',3,3],
       ['C','G',2,1],
       ['D','E',7,6],
       ['D','H',5,0],
       ['F','H',1,0],
       ['G','H',2, 0]]


# In[2]:


temp=[]
temp1=[]
for i in graph:
    temp.append(i[0])
    temp1.append(i[1])


# In[3]:


print(temp)


# In[4]:


print(temp1)


# In[5]:


nodes = set(temp).union(set(temp1))


# In[6]:


nodes


# In[17]:


def A_star(graph, costs, open, closed, cur_node):
    if cur_node in open:
        open.remove(cur_node)
    closed.add(cur_node)
    for i in graph:
        print(costs)
        if(i[0] == cur_node and costs[i[0]]+i[2]+i[3] < costs[i[1]]):
            open.add(i[1])
            costs[i[1]] =  costs[i[0]]+i[2]+i[3]
            path[i[1]] = path[i[0]] + ' -> ' + i[1]
    costs[cur_node] = 999999
    small = min(costs, key=costs.get)
    if small not in closed:
        A_star(graph, costs, open,closed, small)
costs = dict()
temp_cost = dict()
path = dict()
for i in nodes:
    costs[i] = 999999
    path[i] = ' '


# In[18]:


open = set()
closed = set()
start_node = input("Enter the Start Node: ")
open.add(start_node)


# In[19]:


path[start_node] = start_node
costs[start_node] = 0


# In[20]:


A_star(graph, costs, open, closed, start_node)
goal_node = input("Enter the Goal Node: ")
print("Path with least cost is: ",path[goal_node])


# In[ ]:




