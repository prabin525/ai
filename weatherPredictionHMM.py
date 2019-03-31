# Weather Prediciton using HMM

from pomegranate import *
import numpy as np 
import matplotlib.pyplot as plt

# #Markov Chain

# d1 = DiscreteDistribution({'S': 0.33, 'R': 0.33, 'F': 0.33})

# d2 = ConditionalProbabilityTable([['S', 'S', 0.8],
#                                 ['S', 'R', 0.05],
#                                 ['S', 'F', 0.15],
#                                 ['R', 'S', 0.2],
#                                 ['R', 'R', 0.6],
#                                 ['R', 'F', 0.2],
#                                 ['F', 'S', 0.2],
#                                 ['F', 'R', 0.3],
#                                 ['F', 'F', 0.5]], [d1])

# model = MarkovChain([d1, d2])

# print(model.log_probability( ['S','S','R'] ))


#HMM


d1 = DiscreteDistribution({'U':0.1,'N':0.9})
d2 = DiscreteDistribution({'U':0.8,'N':0.2})
d3 = DiscreteDistribution({'U':0.3,'N':0.7})


s1 = State(d1, name="Sunny")
s2 = State(d2, name = "Rainy")
s3 = State(d3, name="Foggy")

hmm = HiddenMarkovModel("Weather Predicition")

hmm.add_states(s1,s2,s3)

hmm.add_transition(hmm.start,s1,0.33)
hmm.add_transition(hmm.start,s2,0.33)
hmm.add_transition(hmm.start,s3,0.33)

hmm.add_transition(s1,s1,0.8)
hmm.add_transition(s1,s2,0.05)
hmm.add_transition(s1,s3,0.15)

hmm.add_transition(s2,s1,0.2)
hmm.add_transition(s2,s2,0.6)
hmm.add_transition(s2,s3,0.2)

hmm.add_transition(s3,s1,0.2)
hmm.add_transition(s3,s2,0.3)
hmm.add_transition(s3,s3,0.5)


hmm.bake()

hmm.plot(arrows=True, with_labels=True)

seq = list("NNU")
print('XXXXXXXXXXXXXXXXXXXXXXX')
print(hmm.viterbi( seq ))
print('XXXXXXXXXXXXXXXXXXXXXXX')
print(hmm.log_probability(seq))
print('XXXXXXXXXXXXXXXXXXXXXXX')
print(hmm.forward_backward(seq))
print('XXXXXXXXXXXXXXXXXXXXXXX')
#print(hmm.predict(seq, algorithm ='viterbi'))
print(hmm.predict(seq, algorithm ='map'))
print('XXXXXXXXXXXXXXXXXXXXXXX')
print ("hmm state 0: " + hmm.states[0].name )
print('XXXXXXXXXXXXXXXXXXXXXXX')
print ("hmm state 1: " + hmm.states[1].name )
print('XXXXXXXXXXXXXXXXXXXXXXX')
print ("hmm state 2: " + hmm.states[2].name )
print('XXXXXXXXXXXXXXXXXXXXXXX')
print ("hmm state 3: " + hmm.states[3].name )
print('XXXXXXXXXXXXXXXXXXXXXXX')
print(hmm.dense_transition_matrix())
#print(hmm_predictions)

#print(hmm.forward(seq))


plt.show()
