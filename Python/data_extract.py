import string
from decimal import *

f = open('C:\Users\Ashley\Documents\CENS\mobility_sample.csv')
list = []
temp = []

lat = []
longi = []
mode = []

#change this variable
r = 1000

for x in range(r + 1):
    temp.append(f.readline())
f.close()

temp.pop(0)

for x in temp:
    list.append(x.split(','))

for x in list:
    lat.append((x[5]))
    longi.append((x[6]))
    mode.append((x[7]))

#for x in range(len(lat)):
#    lat[x] = '%.4f' float(lat[x])
    

lat_array = 'var latitudes = new Array(' + str(lat) + ');'
long_array = 'var longitudes = new Array(' + str(longi) + ');'
mode_array = 'var modes = new Array(' + str(mode) + ');'

lat_array = string.replace(lat_array, '[', '', 1)
long_array = string.replace(long_array, '[', '', 1)
mode_array = string.replace(mode_array, '[', '', 1)

lat_array = string.replace(lat_array, ']', '', 1)
long_array = string.replace(long_array, ']', '', 1)
mode_array = string.replace(mode_array, ']', '', 1)

f = open('C:\Users\Ashley\Desktop\data.txt', 'r+')
f.write(lat_array + '\n')
f.write(long_array + '\n')
f.write(mode_array + '\n')
f.close()
