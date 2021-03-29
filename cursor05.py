import arcpy

def main():

    wsp = r'..\..\data\Canada\Canada.gdb'
    Maj_City_fc = r'..\..\data\Canada\Canada.gdb\MajorCities'
    arcpy.env.workspace = wsp

    field_names = ["NAME", "PROV", "SHAPE@X", "SHAPE@Y", "UTM_MAP"]

    cities = []

    with arcpy.da.SearchCursor(Maj_City_fc, field_names) as cursor:
        for row in cursor:
            cities.append(row)
    
    with open('..\\output\\cities.kml', mode = 'w')as cf:
        cf.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        cf.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
        cf.write('<Document>\n')
        for row in cities:
            cf.write('  <Placemark\n>')
            cf.write(f'    <name>{row[0]}, {row[1]}</name>\n')
            cf.write(f'    <description>http://www.canmaps.com/topo/nts50/map/{row[4].lower()}.htm</description>\n')
            cf.write('    <Point>\n')
            cf.write(f'      <coordinates>{row[2]},{row[3]},0</coordinates>\n')
            cf.write('    </Point>\n')
            cf.write('  </Placemark\n>')

        cf.write('</Document>\n')
        cf.write('</kml>')
        

if __name__ == '__main__':
    main()