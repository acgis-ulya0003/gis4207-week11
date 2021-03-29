import sys

def main():

    if len(sys.argv) != 2:
        print('Usage: cursor02.py <province name>')
    else:
        import arcpy

        wsp = r'..\..\..\..\data\Canada'
        Maj_City_fc = r'..\..\..\..\data\Canada\Can_Mjr_Cities.shp'
        arcpy.env.workspace = wsp

        field = ['NAME', 'PROV']

        count = 0

        print('Name')

        prov_code = sys.argv[1].upper()

        search_fields = arcpy.AddFieldDelimiters(wsp, 'PROV')
        where_clause = f"{search_fields} = '{prov_code}'"

        cursor = arcpy.da.SearchCursor(Maj_City_fc, field, where_clause)

        for row in cursor:
            #print(row)
            print(str(row).strip('(\'').strip('\')'))
            #print(str(row).strip('(\'').strip('\')'))
            count += 1

        count = str(count)
        print('\n')
        print('There are ' + count + ' cities in the above list.')

if __name__ == '__main__':
    main()

#python cursor02.py on