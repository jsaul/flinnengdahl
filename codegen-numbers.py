import seiscomp.seismology

print("static short int _numbers[180][360] = {")

for lat in range(-90,90):
    print("{\t\t// lat: %+3d ... %+3d" % (lat, lat+1))
    for lon in range(-180,180):
        name, num = seiscomp.seismology.Regions.getFlinnEngdahlRegion(lat+0.5, lon+0.5)
        print("\t%d,\t// lat: %+3d ... %+3d   lon: %+4d ... %+4d " % (num, lat, lat+1, lon, lon+1))
    print("},\t\t// lat: %+3d ... %+3d" % (lat, lat+1))
print("};")
