import sys

def main():

    if len(sys.argv) != 2:
        print('Usage: cursor04.py <province name>')
    else:
        import arcpy

        wsp = r'..\..\..\..\data\Canada\Canada.gdb'
        Maj_City_fc = r'..\..\..\..\data\Canada\Canada.gdb\MajorCities'
        arcpy.env.workspace = wsp

        get_text = arcpy.GetParameterAsText(0)

        field = ['NAME', 'PROV']

        count = 0

        print('Name')

        prov_code = sys.argv[1].upper()

        search_fields = arcpy.AddFieldDelimiters(wsp, 'PROV')
        field_names = ["NAME", "PROV", "SHAPE@XY"]
        where_clause = f"{search_fields} = '{prov_code}'"

        count = 0

        with arcpy.da.SearchCursor(Maj_City_fc, field_names, where_clause) as cursor:
            for row in cursor:
                count += 1                
                x, y = row[2]
                print(row[0] + ', ' + row[1] + ', ' "{}, {}".format(x, y))

        count = str(count)
        print('\n')
        print('There are ' + count + ' cities in the above list.')

if __name__ == '__main__':
    main()

#python cursor04.py on