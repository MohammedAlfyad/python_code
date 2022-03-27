#!/usr/bin/env python
# coding: utf-8

# In[4]:


import networkx as nx
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


G = nx.Graph()

G.add_nodes_from(['A','B','C','D','E'])

G.add_edges_from([('A','B'),('B','C'),('A','C'),('A','D')])

nx.draw(G,
        with_labels=True,
        node_color='blue',
        node_size=500,
        font_color='white',
        font_size=16,
        )


# In[6]:


nx.has_path(G, 'D', 'C')


# In[7]:


nx.has_path(G, 'A', 'E')


# In[8]:


list(nx.all_simple_paths(G, 'D', 'C'))


# In[9]:


G = nx.Graph()
G.add_nodes_from(['A','B','C','D'])
G.add_edges_from([('A','B'),('B','C'),('A','C'),('A','D')])
nx.draw(G,
        with_labels=True,
        node_color='blue',
        node_size=1600,
        font_color='white',
        font_size=16,
        )


# In[10]:


list(nx.all_simple_paths(G,'D','C'))


# In[11]:


nx.shortest_path(G,'D','C')


# In[12]:


nx.shortest_path_length(G, 'D', 'C')


# In[13]:


nx.is_connected(G)


# In[14]:


G = nx.Graph()

G.add_nodes_from(['A','B','C','D','E'])
G.add_edges_from([('A','B'),('B','C'),('C','A'),('D','E')])

nx.draw(G, with_labels=True)


# In[15]:


nx.is_connected(G)


# In[16]:


nx.has_path(G, 'A', 'C')


# In[17]:


nx.has_path(G, 'A', 'E')


# In[18]:


nx.number_connected_components(G)


# In[21]:


list(nx.connected_components(G))


# In[19]:


components = list(nx.connected_components(G))
len(components[0])


# In[20]:


components = list(nx.connected_components(G))
len(components[1])


# In[21]:


max(nx.connected_components(G), key=len)


# In[22]:


core_nodes = max(nx.connected_components(G), key=len)
core = G.subgraph(core_nodes)

nx.draw(core, with_labels=True)


# In[23]:


D = nx.DiGraph()
D.add_edges_from([
    (1,2),
    (2,3),
    (3,2), (3,4), (3,5),
    (4,2), (4,5), (4,6),
    (5,6),
    (6,4),
])
nx.draw(D, with_labels=True)


# In[24]:


nx.has_path(D, 1, 4)


# In[25]:


nx.has_path(D, 4, 1)


# In[26]:


nx.shortest_path(D, 2, 5)


# In[27]:


nx.shortest_path(D, 1, 4)


# In[28]:


nx.shortest_path(D, 5, 2)


# In[29]:


nx.is_strongly_connected(D)


# In[30]:


nx.is_weakly_connected(D)


# In[31]:


list(nx.weakly_connected_components(D))


# In[32]:


list(nx.strongly_connected_components(D))


# In[33]:


G = nx.read_graphml('openflights_usa.graphml')


# In[34]:


G.nodes['IND']


# In[35]:


G.nodes['IND']['name']


# In[36]:


G.nodes['FAI']


# In[41]:


A = nx.read_edgelist('openflights_usa.edges')


# In[42]:


A.edges()


# In[43]:


A.has_edge('IND', 'FAI')


# In[44]:


nx.has_path(A,'IND', 'FAI')


# In[45]:


nx.shortest_path(A,'IND', 'FAI')


# In[ ]:




