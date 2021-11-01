import csv 

# csv importer function
def get_csv_data(filepath):
    # load csv data
    f = open(filepath, "r")

    # read csv data
    csv_reader = csv.DictReader(f)

    # convert DictReader object into list
    csv_list = []
    for line in csv_reader:
        csv_list.append(line)
    
    # return list
    return csv_list

# loading csv file
data = get_csv_data("practice_data.csv")


# Saving list of dictionaries as a csv file

# Trial 1
modified_data = [] # placeholder for a list of strings, containing field values separated by comma
# loop through each row
for row in data:
    headers = list(row.keys()) # store field names as list
    headers = ','.join(headers) # store field names as single string, where each field is separated by a comma
    field_list = list(row.values()) # storing dictionary values (field values) as list
    #print(field_list)
    field_vals = "'".join(str(a) for a in field_list) # create string, where each field value is separated by comma
    modified_data.append(field_vals)

# saving file
csv_file = open("trial1.csv","w")

#Write the Headers to the file
csv_file.write(headers + "\n")

#Write the data to the file
for line in practice:
    csv_file.write(line + '\n')

#Close CSV File so the code writing of the file will work
csv_file.close()


# trial 2

practice = []
for a in data:
    new_row = ""
    headers = list(a.keys()) # store field names as list
    headers = ','.join(headers)
    # loop through each value
    for key, val in a.items():

        # if remarks
        if a[key] == 'remarks':
            new_row += "'" + val + "'" + ","
        
        else:
            new_row += val + ","
    practice.append(new_row)


csv_file = open("trial2.csv","w")

#Write the Headers to the file
csv_file.write(headers + "\n")

#Write the data to the file
for line in practice:
    csv_file.write(line + '\n')

#Close CSV File so the code writing of the file will work
csv_file.close()
