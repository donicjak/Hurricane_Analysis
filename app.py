import data as d
from collections import Counter
import decimal


def updated_damages(damages):
  updated = []
  for item in damages:
    if(item == 'Damages not recorded'):
      updated.append(item)
    else:
      number = item[:-1]
      updated.append(float(number))
  return updated

def combine_data(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    combined_data = {}
    for i in range(len(names)):
        combined_data[names[i]] = {'Month' : months[i], 'Year' : years[i], 'Max Sustained Wind' : max_sustained_winds[i], 'Areas Affected' : areas_affected[i], 'Damage' : damages[i], 'Deaths' : deaths[i]}
    #print(combined_data)
    return combined_data

def year_as_key(dict):
    newDict = {}
    for key, value in dict.items():
        newDict[value['Year']] = {'Name' : key, 'Month' : value['Month'], 'Max Sustained Wind' : value['Max Sustained Wind'], 'Areas Affected' : value['Areas Affected'], 'Damage' : value['Damage'], 'Deaths' : value['Deaths']}
        print(newDict)
    return newDict

def frequency_for_areas(dict):
    new_list = []
    for value in dict.values():
        for item in value['Areas Affected']:
            new_list.append(item)
            new_dict = Counter(new_list)
    return new_dict

def most_frequent(dict):
    tmp_list = list(dict)
    tmp_list2 = list(dict.values())
    result = (tmp_list[0], tmp_list2[0])
    return result

def most_deaths(dict):
    new_list = []
    for value in dict.values():
        new_list.append(value['Deaths'])
    new_list.sort()
    return (new_list[-1])

def rating_deaths(dict):
    new_dict = {}
    over10000 = []
    over1000 = []
    over500 = []
    over100 = []
    over0 = []
    for key, value in dict.items():
        if(value['Deaths'] > 10000):
            over10000.append(value['Deaths'])
        elif(value['Deaths'] > 1000):
            over1000.append(value['Deaths'])
        elif(value['Deaths'] > 500):
            over500.append(value['Deaths'])
        elif(value['Deaths'] > 100):
            over100.append(value['Deaths'])
        else:
            over0.append(value['Deaths'])
    lists_combined = []
    lists_combined.append(over10000)
    lists_combined.append(over1000)
    lists_combined.append(over500)
    lists_combined.append(over100)
    lists_combined.append(over0)
    for i in range(5):
        new_dict[i] = lists_combined[-1-i]
    return (new_dict)

def biggest_damage(dict):
    damage_list = []
    for value in dict.values():
        #print(value['Damage'])
        if(value['Damage'][-1] == 'B'):
         damage_list.append(float(value['Damage'][:-1]))
    damage_list.sort()
    to_decimal = decimal.Decimal(damage_list[-1])
    tmp_damage = str(to_decimal) + 'B'
    result_dict = {}

    for key,value in dict.items():
        if(value['Damage'] == tmp_damage):
            result_dict[key] = value['Damage']
    return (result_dict)

def damage_scale(dict):
    new_dict = {}

    for key, value in dict.items():
        if( value['Damage'] == 'Damages not recorded'):
            pass
        elif( value['Damage'][-1] == 'M'):
            milions_to_float = float(value['Damage'][:-1])
            to_milions = int(milions_to_float*1000000)
            if(to_milions > 50000000000):
                try:
                    new_dict['4'].append(key)
                except:
                    new_dict['4'] = [key]
            elif(to_milions > 10000000000):
                try:
                    new_dict['3'].append(key)
                except:
                    new_dict['3'] = [key]
            elif(to_milions > 1000000000 ):
                try:
                    new_dict['2'].append(key)
                except:
                    new_dict['2'] = [key]
            elif(to_milions > 100000000 ):
                try:
                    new_dict['1'].append(key)
                except:
                    new_dict['1'] = [key]
            else:
                try:
                    new_dict['0'].append(key)
                except KeyError:
                    new_dict['0'] = [key]
        else:
            bilions_to_float = float(value['Damage'][:-1])
            tobilions = int(bilions_to_float*1000000000)
            if(tobilions > 50000000000):
                try:
                    new_dict['4'].append(key)
                except:
                    new_dict['4'] = [key]
            elif(tobilions > 10000000000):
                try:
                    new_dict['3'].append(key)
                except:
                    new_dict['3'] = [key]
            elif(tobilions > 1000000000 ):
                try:
                    new_dict['2'].append(key)
                except:
                    new_dict['2'] = [key]
            elif(tobilions > 100000000 ):
                try:
                    new_dict['1'].append(key)
                except:
                    new_dict['1'] = [key]
            else:
                try:
                    new_dict['0'].append(key)
                except:
                    new_dict['0'] = [key]
    return(new_dict)

my_dict2 = combine_data(d.names, d.months, d.years, d.max_sustained_winds, d.areas_affected, d.damages, d.deaths)
my_dict = combine_data(d.names, d.months, d.years, d.max_sustained_winds, d.areas_affected, updated_damages(d.damages), d.deaths)
frequency_for_areas(my_dict)
rating_deaths(my_dict)
biggest_damage(my_dict2)
damage_scale(my_dict2)