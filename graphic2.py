import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
final="end"
color=['red','blue','yellow','magenta','cyan','burlywood','black', 'chartreuse', 'navy']
x_label="X"
y_label="Y"
num_line=2
data_label=[""]
xdata,ydata=[[]],[[]]


while final!="end":
    i=raw_input("command: ")
    i=i.split(";")
    final=i[0]
    if(final=="xlabel"):
        x_label=i[1]
    if(final=="ylabel"):
        y_label=i[1]
    if(final=="num_line"):
        num_line=int(i[1])
        for k in range(num_line):
            data_label.append("");
            xdata.append([])
            ydata.append([])
    if(final=="label"):
        data_label[int(i[1])-1]=i[2]
    
for k in range(num_line):
            data_label.append("");
            xdata.append([])
            ydata.append([])        


fig = plt.figure()
ax = fig.add_subplot(111)
line=[]
for i in range(num_line):
    for k in range(10):
        xdata[i].append(0)
        ydata[i].append(0)
for i in range(num_line):
    print i
    line.append(Line2D(xdata[i],ydata[i],color=color[i]))
plt.legend(line,data_label)
for i in range(num_line):
    ax.add_line(line[i])
ax.set_ylim(-10, 10)
ax.set_xlim(-10, 10)
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
#ax.grid()



#xdata,ydata,ydata1=[],[],[]
#xdata1=[]

def data_gen2():
    t = data_gen.t
    cnt = 0
    while cnt < 1000:
        cnt+=1
        t += 0.05
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
data_gen2.t = 0


def data_gen():
    i=raw_input("DATA(A;X;Y):")
    i=i.split(";")
    l=int(i[1])-1
    yield l, float(i[2]),float(i[3])

data_gen.t = 0




def run(lixo):
    i=raw_input("DATA(A;X;Y):")
    i=i.split(";")
    l=int(i[1])-1
    j=l
    x=float(i[2])
    y=float(i[3])
    print j,x,y
    xdata[j].append(x)
    ydata[j].append(y)
#    xmin, xmax = ax.get_xlim()
#    print xmin, xmax
#    ymin, ymax = ax.get_ylim()
#    print ymin, ymax
#    if xdata[j][len(xdata[j])-1] >= xmax:
#        ax.set_xlim(xmin, 1.3*xmax)
#        ax.figure.canvas.draw()
#    if ydata[j][len(ydata[j])-1] >= ymax:
#        ax.set_ylim(ymin, 1.1*ymax)
#        ax.figure.canvas.draw()
##    print line
#    for k in range(num_line):
#        line[k].set_data(xdata[k], ydata[k])
#        ax.add_line(line[k])
#        #ax.add_line(line[1])
    line[0].set_data(xdata[0], ydata[0])
    line[1].set_data(xdata[1], ydata[1])
    ax.add_line(line[0])
    ax.add_line(line[1])
    return line[0],

def run2(data):
    # update the data
    t,y = data
    print data
    xdata.append(t)
    ydata.append(y)
    ydata1.append(1)
    xmin, xmax = ax.get_xlim()
    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line[0].set_data(xdata, ydata)
    line[1].set_data(xdata, ydata1)
    ax.add_line(line[0])
    ax.add_line(line[1])
    return line

#print run()


ani = animation.FuncAnimation(fig, run, 1, blit=True, interval=10,repeat=False)
plt.show()
