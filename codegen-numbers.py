# This script uses SeisComP to get the region numbers for the lat-lon grid.
# Could also have used ObsPy for that.

import sys
#import seiscomp.seismology
import obspy.geodetics.flinnengdahl
fe = obspy.geodetics.flinnengdahl.FlinnEngdahl()

print("static short int _numbers[180][360] = {")

for lat in range(-90, 90):
    print("{\t\t// lat: %+3d ... %+3d" % (lat, lat+1))
    for lon in range(-180, 180):
        num = fe.get_number(lon+0.5, lat+0.5)
#       name, num = seiscomp.seismology.Regions.getFlinnEngdahlRegion(lat+0.5, lon+0.5)
        
        print("\t%d,\t// lat: %+3d ... %+3d   lon: %+4d ... %+4d " % (num, lat, lat+1, lon, lon+1))
    print("},\t\t// lat: %+3d ... %+3d" % (lat, lat+1))
print("};")
