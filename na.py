import networkx as nx
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np

G=[[]*1000]*1000
cnt=[[]*1000]*1000
cor=[[]*1000]*1000


G[1] = nx.petersen_graph()
G[2] = nx.davis_southern_women_graph()
G[3] = nx.florentine_families_graph()
G[4] = nx.les_miserables_graph()

cnt[1]=nx.degree_centrality(G[1])
cnt[2]=nx.degree_centrality(G[2])
cnt[3]=nx.degree_centrality(G[3])
cnt[4]=nx.degree_centrality(G[4])

nx.draw(G[1])
plt.show()
nx.draw(G[2])
plt.show()
nx.draw(G[3])
plt.show()
nx.draw(G[4])
plt.show()

x=np.arange(1,len(cnt[1])+1,1)
y=np.arange(1,len(cnt[1])+1,1)

#len(cnt[1])
for i in range(0,len(cnt[1])):
  y[i]=cnt[1][i]
plt.scatter(x=x,y=y)

x=np.arange(1,len(cnt[2])+1,1)
y=np.arange(1,len(cnt[2])+1,1)
v=cnt[2].values()
v=list(v)
plt.scatter(x=x,y=v)

x=np.arange(1,len(cnt[3])+1,1)
y=np.arange(1,len(cnt[3])+1,1)
v=cnt[3].values()
v=list(v)
plt.scatter(x=x,y=v)

x=np.arange(1,len(cnt[4])+1,1)
y=np.arange(1,len(cnt[4])+1,1)
v=cnt[4].values()
v=list(v)
plt.scatter(x=x,y=v)
