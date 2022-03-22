#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


G = nx.Graph()
nodes_to_add = ['A','B', 'C', 'D','E','F','G']
G.add_nodes_from(nodes_to_add)
edges_to_add = [('A', 'B'), ('B', 'C'), ('C', 'D'),('D', 'E'), ('E', 'F'), ('F', 'G')]
G.add_edges_from(edges_to_add)
nx.draw(G,
        with_labels=True,
        node_color='blue',
        node_size=1600,
        font_color='white',
        font_size=16,
        )


# In[3]:


G.nodes()


# In[4]:


G.edges()


# In[5]:


for node in G.nodes:
    print(node)


# In[6]:


for edge in G.edges:
    print(edge)


# In[7]:


G.number_of_nodes()


# In[8]:


G.number_of_edges()


# In[9]:


for neighbor in G.neighbors('E'):
    print(neighbor)


# In[10]:


list(G.neighbors('E'))


# In[11]:


nx.is_tree(G)


# In[12]:


nx.is_connected(G)


# In[13]:


G.has_node('F')


# In[14]:


G.has_node('U')


# In[15]:


G.degree('A')


# In[17]:


items = ['spider', 'y', 'banana']
[item.upper() for item in items]


# In[18]:


print(G.nodes())
print([G.degree(n) for n in G.nodes()])


# In[22]:


G = nx.Graph()
G.add_nodes_from(['A','Mohammed','Alfyad',1911])
G.add_edge('Mohammed','Alfyad')
nx.draw(G,
        with_labels=True,
        node_color='blue',
        node_size=500,
        font_color='white',
        font_size=16,
        )


# In[23]:


print(open('friends.adjlist').read())


# In[25]:


SG = nx.read_adjlist('friends.adjlist')
nx.draw(SG, node_size=2000, node_color='lightblue', with_labels=True)


# In[26]:


SG.degree('Alice')


# In[27]:


D = nx.DiGraph()

D.add_edges_from([(1,2),(2,3),(3,2),(3,4),(3,5),(4,5),(4,6),(5,6),(6,4),(4,2),(1,6),(1,4)])

nx.draw(D, with_labels=True)


# In[28]:


D.has_edge(1,2)


# In[29]:


D.has_edge(2,1)


# In[30]:


print('Successors of 2:', list(D.successors(2)))

print('Predecessors of 2:', list(D.predecessors(2)))


# In[31]:


D.in_degree(2)


# In[32]:


D.out_degree(2)


# In[33]:


print('Successors of 2:', list(D.successors(2)))
print('"Neighbors" of 2:', list(D.neighbors(2)))


# In[ ]:




