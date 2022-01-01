#Matplotlib
#Plotting

#matplotlib is a 2d plotting library for python
#matplotlib.pyplot is a collection of command-style
#functions that make matplotlib work like MATLAB

#As convention import pyplot as follows:
import matplotlib.pyplot as plt

#Simple example
import numpy as np
xs=np.linspace(0.0,10.0,100)
ys=np.sin(xs)
plt.plot(xs,ys,'r-')  #Red line
plt.savefig('sin.png')
#plt.show()

#Note I am commenting all show files because plots get deleted
#after show command

#Axis labels
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Plot for MAS212")
#plt.show()

#Thicker lines and points
plt.plot(xs,ys,'r-',linewidth=2.0)
plt.plot(xs[::2],ys[::2],'bo') #plot every 2 point as ablue filled circle
#warning: it is o not zero(0)
plt.show()

#Adding legend
plt.plot(xs,np.sin(xs),'r-',label='sin(x)')
plt.plot(xs,np.cos(xs),'b-',label='cos(x)')
plt.ylabel("Trigonometric functions")
plt.legend()
#plt.show()

plt.axis([0,2.0*np.pi,-1.2,1.2])
#now set ticks and labels on the x-axis
xtics=[0,np.pi/2.0,np.pi,3*np.pi/2.0,2*np.pi]
xlabels=['$0$','$\pi/2$','$\pi$','$3\pi/2$','$2\pi$']
plt.xticks(xtics,xlabels)
plt.yticks([-2,0,1])
plt.show()
