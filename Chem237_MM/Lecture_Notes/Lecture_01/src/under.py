#=============================================================================80
#                   Python 2 Under-Damped Oscillator Figure		       #
#=============================================================================80
#    Discussion:
#       Python 2 Figure, Under-Damped Oscillator in arbitrary units.
#       This solution assumes that the damping coefficient >> natural frequency 
#    Modified:
#       4 April 2018
#    Author:
#       Shane Flynn
#==============================================================================#
import numpy as np
import matplotlib.pyplot as plt
#==============================================================================#
#   The Solution of the Under-Damped Oscillator is given by:                   #
#               y(t) = A exp{-gamma t} cos(omega t - delta)                    #
#   A       ===> Arbitrary Constant                                            #
#   gamma   ===> The Damping Constant of the Oscillator                        #
#   omega   ===> The Natural Frequency of the Oscillator                       #
#   delta   ===> A generic phase term of the Oscillator                        #
#==============================================================================#
A = 1
gamma = 1
omega = 10
delta = 0
#==============================================================================#
# 	   		       The Full Solution                               #
#==============================================================================#
def Damping(x):
    z = A * np.exp(-gamma*x) * np.cos(omega*x - delta)
    return z
#==============================================================================#
# 	   		   The Expotential Decay Term                          #
#==============================================================================#
def Decay(x):
    z = A * np.exp(-gamma*x)
    return z
#==============================================================================#
# 	   		Set Range and evaluate the  Oscillator                 #
#==============================================================================#
t = np.arange(0, 5, 0.01)
y = []
w = []
for i in t:
    Y = Damping(i)
    W = Decay(i)
    y.append(Y)
    w.append(W)
#==============================================================================#
# 	   		Plot Figure and Save as png			       #
#==============================================================================#
plt.plot(t, y)
plt.plot(t, w, '--')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.savefig('under_damped.png') 
plt.close()
