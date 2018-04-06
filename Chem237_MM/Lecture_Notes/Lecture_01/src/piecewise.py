#=============================================================================80
#                 Python 2 Piece-Wise Constant Potential Figure		       #
#=============================================================================80
#    Discussion:
#       Python 2 Figure, Representing a Piecewise Potential in arbitrary units.
#    Modified:
#       4 April 2018
#    Author:
#       Shane Flynn
#==============================================================================#
import matplotlib.pyplot as plt
#==============================================================================#
# 	   Define Domain and Range as a decaying step-wise function	       #
#==============================================================================#
x = [0,1,2,3,4, 5, 6, 7, 8]
y = [5, 5,4,4.5,3, 3.5, 2, 2.5, 1]
#==============================================================================#
# 	   		Plot Figure and Save as png			       #
#==============================================================================#
plt.step(x, y)
plt.xlabel('x')
plt.ylabel('V(x)')
plt.ylim(ymin=0) 
plt.ylim(ymax=6) 
plt.savefig('piecewise.png') 
plt.close()
