import networkx as nx
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
G=nx.powerlaw_cluster_graph(50,2,1)
cen1=nx.degree_centrality(G)
v=cen1.values()
cen1=list(v)
cen2=nx.closeness_centrality(G)
v=cen2.values()
cen2=list(v)
cen3=nx.betweenness_centrality(G)
v=cen3.values()
cen3=list(v)
nx.draw(G)
plt.show()
plt.scatter(x=cen1,y=cen3)
