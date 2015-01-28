__author__ = 'vmac'
import networkx as nx
import json
import pprint
import matplotlib.pyplot as plt
import matplotlib

ab = open("/Users/vmac/PycharmProjects/WikiParse/sampleOutput.json","r")

data = json.load(ab)

G = nx.Graph()

lbls={}

sum=0
for stuff in data.keys():
    for stuff2 in data[stuff]:
        G.add_edge(unicode(stuff),unicode(stuff2),weight=sum)
        sum+=1
print G.node
for node in G.nodes():
    lbls[node]= node
pos=nx.spring_layout(G)
nx.draw(G, pos=pos)
for node in lbls:
    plt.annotate(lbls[node],xy=pos[node])
nx.draw_networkx_labels(G, pos=pos, labels=lbls,fontsize=14)
plt.show(unicode)