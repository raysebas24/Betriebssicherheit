#-----------------------------------------------------------
#Program    :Ray_Sebastian_91044_Aufgabe_2_Programmcode.py
#Written by :Sebastian Ray
#Date       :26.04.2022
#Description:Fehlerbaum.
#-----------------------------------------------------------

#Further Information:
"""

"""

# In[1] --------------------------------------------------------------------------------------
import graphviz as gv


class ANDNODE:
    def __init__(self, name):
        self.name = name
        self.nodes = []
    def add(self, node):
        self.nodes.append(node)
        return
    def availability(self):
        ui = 1
        for element in self.nodes:
              ui = ui * (1 - element.availability())  #ui = Non-Availability (Multiply the individual non-availabilities)
        return 1 - ui
    def __repr__(self):
        return self.name + "(&)"


class ORNODE:
    def __init__(self, name):
        self.name = name
        self.nodes = []
        self.avail = 0
    def add(self, node):
        self.nodes.append(node)
        return
    def availability(self):
        vi = 1
        for element in self.nodes:
            vi = vi * element.availability()    #vi = Availability (Multiply the individual availabilities)
        return vi
    def __repr__(self):
        return self.name + "(>=1)"


class NOTNODE:
    def __init__(self, name):
        self.name = name
        self.nodes = []
        self.avail = 0
    def add(self, node):
        if len(self.nodes)==1:
            return
        else:
            self.nodes.append(node)
        return
    def availability(self):
        self.avail = 1 - self.nodes[0].availability()
        return self.avail
    def __repr__(self):
        return self.name + "(NOT)"


class EVENT:  # Standardeingang
    def __init__(self, name, la, mu):
        self.name = name
        self.nodes = []
        self.la = la
        self.mu = mu
        self.avail = 0
    #def add(self, node):                               Not necessary. Because afte an Event, it's over
    def availability(self):
        self.avail = 1 - (self.la / (self.la+self.mu))  #1 - Unavailibility = Availability
        return self.avail
    def __repr__(self):
        return self.name


#Aufgabe a) Kontollfrage:
# TOP = ANDNODE('TOP')
# A = ORNODE('A')
# E1 = EVENT('1', 1/1000, 1/4)
# TOP.add(A)
# TOP.add(E1)


#Aufgabe a) Beispiel-Baum
TOP = ANDNODE('TOP')
A = ORNODE('A')
B = ORNODE('B')
C = NOTNODE('C')
E1 = EVENT('1', 1/1000, 1/4)
E2 = EVENT('2', 1/1000, 1/4)
E3 = EVENT('3', 1/1000, 1/4)
E4 = EVENT('4', 1/1000, 1/4)
TOP.add(A)
TOP.add(B)
A.add(C)
A.add(E2)
C.add(E1)
B.add(E3)
B.add(E4)

#Aus Uebung 7.5
# TOP = ORNODE('TOP')
# A = EVENT('A',1/365,1/365)
# B = ANDNODE('B')
# C = EVENT('C',1/7300,2/365)
# D = EVENT('D',1/7300,1/365)
# TOP.add(A)
# TOP.add(B)
# B.add(C)
# B.add(D)


graph = gv.Graph(format='png', graph_attr={'splines':'ortho'})


def draw(TOP,graph):
    if not hasattr(TOP, 'nodes'):                                       #return TRUE if the specified object has the attribute, else FALSE
        return graph
    for element in TOP.nodes:                                           #passes through all nodes of TOP
        if type(element).__name__ == "EVENT":                           #checks for the Object class name              
            graph.node(str(element),shape='circle',label=str(element))  #Adds a new node
        else:
            graph.node(str(element),shape='rectangle',label=str(element))
        graph.edge(str(TOP),str(element))                               #Adds a new edge
        graph = draw(element,graph)                                     #recursive call
    return graph


graph.node(str(TOP),shape='rectangle',label=str(TOP))                   #First Node!
draw(TOP,graph)


graph.view("MyGraph", cleanup=True)                                     #Output of the Graph without header-file
print("The Graph as been output.")


#Aufgabe b) Verfügbarkeit
print("Availability = ", TOP.availability())


# %%
