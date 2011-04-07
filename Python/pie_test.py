from pylab import *
from decimal import *
from matplotlib.pyplot import figure, show
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
from numpy import arange
import datetime
import numpy as N
import matplotlib

## import from csv
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
## find the end of a "day"
## Optimize this later!!!
def end_index(timestamp_array, beginning_index):
    date = timestamp_array[beginning_index][0:10]
    print date
    i = 1
    while timestamp_array[beginning_index+i][0:10] == date:
        i = i + 1
    return beginning_index+i

# ------------------- NEED TO CUSTOMIZE --------------------#
descr = N.dtype([('#id', 'string'), ('user_id', 'string'),
                 ('time_stamp', 'string'), ('epoch_millis', 'string'),
                 ('phone_timezone', 'string'), ('latitude', 'string'),
                 ('longitude', 'string'), ('mode', 'string'),
                 ('speed', 'string')])
myrecarray = read_array('mobility_sample.csv', descr)

# column 8 (index 7) is 'mode'
count = [0, 0, 0, 0]
labels =  ['walk', 'still', 'drive', 'bike']
data_array = myrecarray[2][1:end_index(myrecarray[2], 1)]
# ---------------------------------------------------------- #

for i in range(len(myrecarray[7])):
    temp = str((myrecarray[7])[i])
    if temp == labels[0]:
        count[0] = count[0] + 1
    elif temp == labels[1]:
        count[1] = count[1] + 1
    elif temp == labels[2]:
        count[2] = count[2] + 1
    elif temp == labels[3]:
        count[3] = count[3] + 1 

total = Decimal(len(myrecarray[7]))
for i in range(len(count)):
    count[i] = (Decimal(count[i])/total)*100
    
print count
    

# make a square figure and axes
figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

# Optional - to use different labels on the chart, customize name and use
# labels=names in pie()
names =  ['Walk', 'Still', 'Drive', 'Bike']

explode=(0.03, 0.03, 0.03, 0.03)
pie(count, explode=explode, labels=names, autopct='%1.1f%%', shadow=True)
title('Mobility', bbox={'facecolor':'0.8', 'pad':10})

# -------------------testing
date1 = datetime.datetime( 2000, 3, 2)
date2 = datetime.datetime( 2000, 3, 6)
delta = datetime.timedelta(hours=6)
dates = drange(date1, date2, delta)

y = arange(len(myrecarray[7]))

fig = figure()
ax = fig.add_subplot(111)
ax.plot_date(dates, y)

# this is superfluous, since the autoscaler should get it right, but
# use date2num and num2date to to convert between dates and floats if
# you want; both date2num and num2date convert an instance or sequence
ax.set_xlim( dates[0], dates[-1] )

# The hour locator takes the hour or sequence of hours you want to
# tick, not the base multiple

ax.xaxis.set_major_locator( DayLocator() )
ax.xaxis.set_minor_locator( HourLocator(arange(0,25,6)) )
ax.xaxis.set_major_formatter( DateFormatter('%Y-%m-%d') )

ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
fig.autofmt_xdate()
#--------------------/testing

show()
