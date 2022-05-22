#-----------------------------------------------------------
#Program    :Ray_Sebastian_91044_Aufgabe_3_Programmcode.py
#Written by :Sebastian Ray
#Date       :22.05.2022
#Description:Markov.
#-----------------------------------------------------------

#Further Information:
"""

"""
import graphviz as gv
import numpy as np


class STATE:
    def __init__(self, name, num):
        self.name = name
        self.num = num
        return

class TRANSITION:
    def __init__(self, source, destination, name, rate):
        self.source = source
        self.destination = destination
        self.name = name
        self.rate = rate

class MARKOV:
    def __init__(self, name, dt=1.0):
        self.nodes = []
        self.transitions = []
        self.name = name

    #saves the possible states in a list
    def state(self, stateS):
        self.nodes.append(stateS)

    #saves the possible transitions in a list
    def transition(self, transT):
        self.transitions.append(transT)

    #Calculates the probability that the system will be refurbished (Generalüberholt)
    def probability(self,hours):
        p0=np.zeros(len(self.nodes))                                #array filled with zeros
        p0[0]=1                                                     #set first postition to 1
        P=np.zeros((len(self.nodes),len(self.nodes)))               #Matrix filled with zeros 
        
        for edges in self.transitions:                              #Cycle through all transitions (edges)
            P[edges.source.num][edges.destination.num]=edges.rate   #Matrix Position [source][destination]=Rate

        i=0
        for i in range(hours):
            p0=np.matmul(p0,P)
            i+=1
        return p0

    #Displays the graph
    def draw(self):
        graph.attr(label=str(self.name))                    #Show me the titel 'Fließband' in the graph
        for node in self.nodes:                             #Cycle through all states (nodes)
            graph.node(name=node.name)                      #Stat (node) name
        for edges in self.transitions:                      #Cycle through all transitions (edges)
            graph.edge(edges.source.name, edges.destination.name,dir="forward",label=str(round(edges.rate,5)))  #(start,end,arrow,range)
        graph.render('Markov', view=True)


#Create Graph
graph = gv.Graph(format='png')


# #Parameters
error2=1/(2*365*6)      #Failure of 2 engines
error3=1/(3*365*6)      #Failure of 3 or more engines
serv12=1/12             #Service Guy comes within 12h
serv24=1/24             #Service Guy comes within 24h
repair=1/4              #Repair time 4h
serv3w=1/(24*21)        #Service 3 weeks
serv10=1/(24*365*10)    #Service all 10 years

#Create Markov Modell
M = MARKOV("Fließband")

S1 = STATE("S1_Run",0)
S2 = STATE("S2_War",1)
S3 = STATE("S3_Err",2)
S4 = STATE("S4_Rep",3)
S5 = STATE("S5_Ser",4)

T12 = TRANSITION(S1,S2,"S1,S2",error2)
T13 = TRANSITION(S1,S3,"S1,S3",error3)
T24 = TRANSITION(S2,S4,"S2,S4",serv24)
T34 = TRANSITION(S3,S4,"S3,S4",serv12)
T45 = TRANSITION(S4,S5,"S4,S5",serv10)
T41 = TRANSITION(S4,S1,"S4,S1",repair)
T51 = TRANSITION(S4,S1,"S5,S1",serv3w)
T11 = TRANSITION(S1,S1,"S1,S1",1-(error2+error3))
T22 = TRANSITION(S2,S2,"S2,S2",1-serv24)
T33 = TRANSITION(S3,S3,"S3,S3",1-serv12)
T44 = TRANSITION(S4,S4,"S4,S4",1-repair)
T55 = TRANSITION(S5,S5,"S5,S5",1-serv3w)

#Add STATE
M.state(S1)
M.state(S2)
M.state(S3)
M.state(S4)
M.state(S5)

#Add TRANSITION
M.transition(T12)
M.transition(T13)
M.transition(T24)
M.transition(T34)
M.transition(T45)
M.transition(T41)
M.transition(T51)
M.transition(T11)
M.transition(T22)
M.transition(T33)
M.transition(T44)
M.transition(T55)

# M = MARKOV("Beispiel")
# S1=STATE("S1",0)
# S2=STATE("S2",1)
# M.state(S1)
# M.state(S2)
# T12 = TRANSITION(S1, S2, '112', 1000)
# M.transition(T12)

#Displays the graph 
M.draw()
result = M.probability(87600)
print("Probability over 10 Years = \n", result)
