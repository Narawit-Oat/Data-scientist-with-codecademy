# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,"B": 1000000000}

# write your update damages function here:
def updated_damages(damages,conversion):
    updated_damages = []
    for i in damages:
        if i == 'Damages not recorded':
            updated_damages.append('Damages not recorded')
        elif i[-1] == "M":
            a = float(i[:-1])*conversion["M"]
            updated_damages.append(a)
        elif i[-1] == "B":
            a = float(i[:-1]) * conversion["B"]
            updated_damages.append(a)
        else:
            print("Error function updated_damages")
    return updated_damages

updated_damages = updated_damages(damages,conversion)

# write your construct hurricane dictionary function here:
def hurricane_dictionary_name (names,months,years,max_sustained_winds,areas_affected,updated_damages,deaths):
    hurricane_dictionary = {}
    for i in range(0,len(names)):
        hurricane_dictionary[names[i]] =  {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': updated_damages[i], 'Deaths': deaths[i]}
    return hurricane_dictionary

hurricane_dictionary_names = hurricane_dictionary_name (names,months,years,max_sustained_winds,areas_affected,updated_damages,deaths)

# write your construct hurricane by year dictionary function here:
def hurricane_dictionary_year (names,months,years,max_sustained_winds,areas_affected,updated_damages,deaths):
    hurricane_dictionary = {}
    for i in range(0,len(years)):
        if not years[i] in hurricane_dictionary:
            hurricane_dictionary[years[i]] = [{'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': updated_damages[i], 'Deaths': deaths[i]}]
        elif years[i] in hurricane_dictionary:
            hurricane_dictionary[years[i]].append({'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': updated_damages[i], 'Deaths': deaths[i]})
        else:
            print("Error function hurricane_dictionary_year")
    return hurricane_dictionary

hurricane_dictionary_years = hurricane_dictionary_year (names,months,years,max_sustained_winds,areas_affected,updated_damages,deaths)

# write your count affected areas function here:
def affected_areas_function (areas_affected):
    areas_affected_dictionary = {}
    for i in areas_affected:
        if len(i) > 1 :
            for j in i:
                if j in areas_affected_dictionary:
                    areas_affected_dictionary[j] += 1
                else:
                    areas_affected_dictionary[j] = 1
        else:
            if i[0] in areas_affected_dictionary:
                areas_affected_dictionary[i[0]] += 1
            else:
                areas_affected_dictionary[i[0]] = 1
    return areas_affected_dictionary

affected_areas_dictionary = affected_areas_function (areas_affected)

# write your find most affected area function here:
def most_affected_area_function (affected_areas_dictionary):
    area_list = []
    area_count_list =[]
    for i in affected_areas_dictionary:
        area_list.append(i)
        area_count_list.append(affected_areas_dictionary[i])
    for j in range(0,len(area_count_list)):
        if max(area_count_list) == area_count_list[j]:
            max_area_count = area_count_list[j]
            max_area = area_list[j]
    return max_area,max_area_count

max_area,max_area_count = most_affected_area_function (affected_areas_dictionary)

# write your greatest number of deaths function here:
def max_number_of_deaths (hurricane_dictionary_names):
    max_mortality = 0
    for i in hurricane_dictionary_names:
        if hurricane_dictionary_names[i]['Deaths'] > max_mortality:
            max_mortality = hurricane_dictionary_names[i]['Deaths']
            max_mortality_cane = i
    return max_mortality_cane, max_mortality

max_mortality_cane, max_mortality = max_number_of_deaths (hurricane_dictionary_names)

# write your catgeorize by mortality function here:
#mortality_scale = {0: 0,1: 100,2: 500,3: 1000,4: 10000}
def mortality_function (hurricane_dictionary_names):
    hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: []}
    for i in hurricane_dictionary_names:
        if (hurricane_dictionary_names[i]['Deaths'] > 0) and (hurricane_dictionary_names[i]['Deaths'] <= 100) :
            hurricanes_by_mortality[0].append(hurricane_dictionary_names[i])
        elif (hurricane_dictionary_names[i]['Deaths'] > 100) and (hurricane_dictionary_names[i]['Deaths'] <= 500) :
            hurricanes_by_mortality[1].append(hurricane_dictionary_names[i])
        elif (hurricane_dictionary_names[i]['Deaths'] > 500) and (hurricane_dictionary_names[i]['Deaths'] <= 1000) :
            hurricanes_by_mortality[2].append(hurricane_dictionary_names[i])
        elif (hurricane_dictionary_names[i]['Deaths'] > 1000) and (hurricane_dictionary_names[i]['Deaths'] <= 10000):
            hurricanes_by_mortality[3].append(hurricane_dictionary_names[i])
        elif (hurricane_dictionary_names[i]['Deaths'] > 10000) :
            hurricanes_by_mortality[4].append(hurricane_dictionary_names[i])
        else:
            print("Error function mortality_function")
    return hurricanes_by_mortality

hurricanes_by_mortality = mortality_function (hurricane_dictionary_names)

# write your greatest damage function here:
def greatest_damage_function (hurricane_dictionary_names):
    max_damage = 0
    for i in hurricane_dictionary_names:
        if hurricane_dictionary_names[i]['Damage'] != "Damages not recorded":
            if int(hurricane_dictionary_names[i]['Damage']) > max_damage :
                max_damage = hurricane_dictionary_names[i]['Damage']
                max_damage_cane = i
    return max_damage_cane, max_damage

max_damage_cane, max_damage = greatest_damage_function (hurricane_dictionary_names)

# write your catgeorize by damage function here:

def damage_function (hurricane_dictionary_names):
    hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[]}
    for i in hurricane_dictionary_names:
        if hurricane_dictionary_names[i]['Damage'] != "Damages not recorded":
            if (hurricane_dictionary_names[i]['Damage'] > 0) and (hurricane_dictionary_names[i]['Damage'] <= 100000000) :
                hurricanes_by_damage[0].append(hurricane_dictionary_names[i])
            elif (hurricane_dictionary_names[i]['Damage'] > 100000000) and (hurricane_dictionary_names[i]['Damage'] <= 1000000000) :
                hurricanes_by_damage[1].append(hurricane_dictionary_names[i])
            elif (hurricane_dictionary_names[i]['Damage'] > 1000000000) and (hurricane_dictionary_names[i]['Damage'] <= 10000000000) :
                hurricanes_by_damage[2].append(hurricane_dictionary_names[i])
            elif (hurricane_dictionary_names[i]['Damage'] > 10000000000) and (hurricane_dictionary_names[i]['Damage'] <= 50000000000):
                hurricanes_by_damage[3].append(hurricane_dictionary_names[i])
            elif (hurricane_dictionary_names[i]['Damage'] > 50000000000) :
                hurricanes_by_damage[4].append(hurricane_dictionary_names[i])
            else:
                print("Error function damage_function")
    return hurricanes_by_damage

hurricanes_by_damage = damage_function (hurricane_dictionary_names)
