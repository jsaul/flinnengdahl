# This script uses SeisComP or ObsPy to get the region numbers for the lat-lon grid.

import sys
from contextlib import redirect_stdout

try:
    import seiscomp.seismology
    have_seiscomp = True
except ImportError:
    have_seiscomp = False


try:
    import obspy.geodetics.flinnengdahl
    fe = obspy.geodetics.flinnengdahl.FlinnEngdahl()
    have_obspy = True
except ImportError:
    have_obspy = False


def number_obspy(lat, lon):
    return fe.get_number(lon, lat)


def number_seiscomp(lat, lon):
    name, number = seiscomp.seismology.Regions.getFlinnEngdahlRegion(lat, lon)
    return number


if have_seiscomp:
    number = number_seiscomp
    print("using seiscomp", file=sys.stderr)
elif have_obspy:
    number = number_obspy
    print("using obspy", file=sys.stderr)
else:
    raise RuntimeError("Neither ObsPy nor SeisComP found")


with open("src/flinnengdahl/fe-numbers.cpp", 'w') as f:
    with redirect_stdout(f):

        print("static short int _numbers[180][360] = {")

        for lat in range(-90, 90):
            print("{\t\t// lat: %+3d ... %+3d" % (lat, lat+1))
            for lon in range(-180, 180):
                num = number(lat+0.5, lon+0.5)

                print("\t%d,\t// lat: %+3d ... %+3d   lon: %+4d ... %+4d" % (num, lat, lat+1, lon, lon+1))
            print("},\t\t// lat: %+3d ... %+3d" % (lat, lat+1))
        print("};")
