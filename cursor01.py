import arcpy

wsp = r'..\..\data\Canada'
Maj_City_fc = r'..\..\data\Canada\Can_Mjr_Cities.shp'
arcpy.env.workspace = wsp



fields = ['NAME', 'PROV']
cursor = arcpy.da.SearchCursor(Maj_City_fc, fields)

count = 0
print('Name, Prov')
for row in cursor:
    
    print(str(row).strip('(\'').strip('\')'))
    count += 1

count = str(count)
print('\n')
print('There are ' + count + ' cities in the above list.')

