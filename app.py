import data as d

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
    print(combined_data)

combine_data(d.names, d.months, d.years, d.max_sustained_winds, d.areas_affected, updated_damages(d.damages), d.deaths)