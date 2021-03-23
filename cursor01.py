import arcpy

wsp = r'..\..\data\Canada'
Maj_City_fc = r'..\..\data\Canada\Can_Mjr_Cities.shp'
arcpy.env.workspace = wsp

fclist = arcpy.ListFeatureClasses()

print(fclist)

#with arcpy.da.SearchCursor(fc, 'NAME', 'PROV')as cursor:
cursor = arcpy.SearchCursor(Maj_City_fc)
count = 0
print('Name, Prov')
for row in cursor:
    print(row.getValue('NAME')+ ',' + row.getValue('PROV'))
    count += 1

print(count)

