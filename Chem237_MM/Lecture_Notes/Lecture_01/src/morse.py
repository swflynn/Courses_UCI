#=============================================================================80
#                       Python 2 Morse Potential Figure		               #
#=============================================================================80
#    Discussion:
#       Python 2 Figure, Representing a Morse Potential in arbitrary units.
#    Modified:
#       4 April 2018
#    Author:
#       Shane Flynn
#==============================================================================#
import numpy as np
import matplotlib.pyplot as plt
#==============================================================================#
# 	   The Morse Potential is given by V(r) = D [1-e^{-ax})]^2             #
#           D ===> The Well Depth 
#           a ===> The Well Width
#==============================================================================#
D=1
a=1
def Morse(x):
    v = D * (1 - np.exp(-a*x))**2 
    return v
#==============================================================================#
# 	   		Set Range and evaluate the Morse                       #
#==============================================================================#
x = np.arange(-1, 3, 0.1)
y = []
for i in x:
    V = Morse(i)
    y.append(V)
#==============================================================================#
# 	   		Plot Figure and Save as png			       #
#==============================================================================#
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('V(x)')
plt.savefig('morse.png') 
plt.close()
