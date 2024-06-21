import csv


file = open('/Users/tjwkd/Documents/projects/galsan/test/land_info.csv', "r", encoding='UTF8')
data = list(csv.reader(file, delimiter=","))
file.close()

del data[-1]
for item in data:
    name = item[3].replace(" ", "")
    if len(name) > 3:
        if name[3] == '외':
            name = name[0:3]
    item[3] = name
    del item[-1]

#make list of dictionary with name and land(as dictionary in land_template)
def land_and_owner(data):
    result = []
    for item in data:
        temp = {
                    'name':'',
                    'land':{
                            'str_adr':'',
                            'category':'',
                            'area':''
                            }
                }
        temp_land = {
            'str_adr':'',
            'category':'',
            'area':''
        }
        temp['name'] = item[3]
        temp_land['str_adr'] = item[2]
        temp_land['category'] = item[6]
        temp_land['area'] = item[7]
        temp['land'] = temp_land
        result.append(temp)
    return result

# get all lands owned by one person into a dictionary (owner_template)
# data: land_and_owner result
# name: name of owner
def fill_owner(lao, name):
    temp = {
    'name':'',
    'dob':'',
    'adr':'',
    'loland':[]
    }   
    i = 0
    for count, item in enumerate(lao):
        if item['name'] == name:
            temp['loland'].append(item['land'])
            i = count
    temp['name'] = name
    temp['dob'] = data[i][4]
    temp['adr'] = data[i][5]
    return temp

def fill_final_list(data):
    result = []
    lao = land_and_owner(data)
    for item in lao:
        result.append(fill_owner(lao, item['name']))
    result = [i for n, i in enumerate(result) if i not in result[n + 1:]]
    return result


    


