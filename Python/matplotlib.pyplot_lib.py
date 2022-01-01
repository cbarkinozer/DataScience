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


#Figures and subplots
#Plots are contained within a Figureobject

#Create a new figure with
fig=plt.figure()
#To add a new subplot to a figure:
ax1=fig.add_subplot(2,2,1) #Add first subplot to 2x2 subplots 1. index
#plot function belongs to AxesSubplot object rather than Figure
fig.show()

#Useful figure functions
#plt.gcf() #get current figure
#plt.gca() #get current axes
#plt.clf() #clear figure
#plt.cla() #clear axes
#plt.close() #close plotting window



#Multiple Plots
#There are 2 methods

#1. method
xs=np.linspace(0,10,100)
f=plt.figure() #Define figure
ax=f.add_subplot(2,2,1) #create 1. element of 2x2 figure array
ax.plot(xs,np.sin(xs))  #plot 1. element according to our value
ax=f.add_subplot(2,2,2)
ax.plot(xs,np.sin(xs+np.pi/2.0))
ax=f.add_subplot(2,2,3)
ax.plot(xs,np.sin(xs+np.pi))
ax=f.add_subplot(2,2,4)
ax.plot(xs,np.sin(xs+3.0*np.pi/4.0))
f.show()


#2.method
fig,axes=plt.subplots(2,3) #Create 2x3 array of subplots
axs=axes.flatten() #Convert it to 1d array
for i in range(len(axes)):
    axs[i].plot(xs,np.sin(xs+2.0*np.pi/len(axes)))

plt.show()


#Histograms
sample_size=100
Npts=1000
data=[sum(np.random.rand(sample_size)) for k in range(Npts)]
plt.hist(np.array(data),bins=20,range=(40,60))
plt.show()

#Barplot
n=10
X=np.arange(n)
Y=np.random.rand(n)
plt.bar(X,Y,facecolor='blue')
plt.show()

#Image
#img=plt.imread('pororo.png') #You need to have pororo.png on your path
#print(img.shape,.mg.dtype)
#plt.imshow(img)
#plt.show()

#Scatter plots
N=100
xs=np.random.rand(N)
ys=-np.log(np.random.rand(N)) #Exponential distribution
plt.axis([0,1,0,max(ys)])
plt.scatter(xs,ys)
plt.show()

#Pie Charts

a=np.array([35,25,25,15])
mylabels=["apples","bananas","cherries","dates"]
plt.pie(a,labels=mylabels,startangle=90)
plt.show()
