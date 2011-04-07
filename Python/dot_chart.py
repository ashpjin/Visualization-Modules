from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import numpy as N
import pylab

# define this function to read in values from a csv
def read_array(filename, dtype, separator=','):
    data = [[] for dummy in xrange(len(dtype))]
    f = open(filename, 'r')
    for line in f:
        fields = line.strip().split(separator)
        index = len(fields)
        if index > len(data):
            index = len(data)
        for i in range(index):
            number = fields[i]
            data[i].append(number)
    f.close()
    return data

# ------------ main function ---------------- #
#clf()  ## clear the window

#plot(x, y2, 'r', label="Gallup", color='r', linewidth=2, markerfacecolor='g',
#    markeredgecolor='y', marker='d')

# Add Legend
#legend()

# Read in the csv and translate the modes into ints
y_axis_labels =  ['still', 'drive', 'walk', 'bike']
x_axis_labels = []
x = []      #x values
y = []      #y values
descr = N.dtype([('#id', 'string'), ('user_id', 'string'),
                 ('time_stamp', 'string'), ('epoch_millis', 'string'),
                 ('phone_timezone', 'string'), ('latitude', 'string'),
                 ('longitude', 'string'), ('mode', 'string'),
                 ('speed', 'string')])
myrecarray = read_array('C:/Users/Ashley/Desktop/mobility_sample.csv', descr)
for i in range(len(myrecarray[7])):
    temp = str((myrecarray[7])[i])
    x.append(i)
    x_axis_labels.append(myrecarray[2][i][10:])
    if temp == labels[0]:
        y.append(.5)
    elif temp == labels[1]:
        y.append(1.5)
    elif temp == labels[2]:
        y.append(2.5)
    elif temp == labels[3]:
        y.append(3.5)
    else:
        x.remove(i)
        x_axis_labels.remove(myrecarray[2][i][10:])

# ---------------- Define how graph looks ---------------- #
fig = plt.figure()
ax = plt.subplot(111)

# Graph and axis titles
xlabel(myrecarray[2][1][0:10])
ylabel('Mode')
title('Activity')

# Create the label list for the major x ticks
test_labels = []
for i in range(len(x_axis_labels)):
    if i % 20 == 0:
        test_labels.append(x_axis_labels[i])

# Personalize the Y axis ticks
pos = N.arange(4)+0.5   #Center bars on the Y-axis ticks
pylab.yticks(pos, y_axis_labels)

# Transform the X axis ticks to reflect the time the sample was taken
pos = N.arange(len(test_labels))
pylab.xticks(pos, test_labels)

# Set the graph limits (preferable to leave some space so it looks good)
plt.ylim([0, 4])
plt.xlim([1, 100])
plt.plot(x, y, 'o')

# Set major and minor ticks, here minor ticks are unlabelled
majorLocator   = MultipleLocator(20)
minorLocator   = MultipleLocator(5)
ax.xaxis.set_major_locator(majorLocator)
ax.xaxis.set_minor_locator(minorLocator)

# ------------------ Show graph --------------------- #
print "done"
 
fig.autofmt_xdate() 
plt.show()