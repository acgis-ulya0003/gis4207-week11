import sys

def main():

    if len(sys.argv) != 2:
        print('Usage: cursor03.py <province name>')
    else:
        import arcpy

        wsp = r'..\..\..\..\data\Canada\Canada.gdb'
        Maj_City_fc = r'..\..\..\..\data\Canada\Canada.gdb\MajorCities'
        arcpy.env.workspace = wsp

        field = ['NAME', 'PROV']

        count = 0

        print('Name')

        prov_code = sys.argv[1].upper()

        search_fields = arcpy.AddFieldDelimiters(wsp, 'PROV')
        where_clause = f"{search_fields} = '{prov_code}'"
        

        cursor = arcpy.da.SearchCursor(Maj_City_fc, field, where_clause)

        print('Name,Prov,Longitude,Latitude')

        for row in cursor:
            
            print(str(row).strip('(\'').strip('\')'))            
            count += 1

        count = str(count)
        print('\n')
        print('There are ' + count + ' cities in the above list.')

if __name__ == '__main__':
    main()

#python cursor03.py on