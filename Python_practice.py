counties_dict={}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
counties_dict

len(counties_dict)

counties_dict.items()

counties_dict.keys()

counties_dict.values()

#create list holds dictionaries
voting_data=[]

voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters":432438})
voting_data

#add ELPaso to the second position in the voting_data list
voting_data.insert(1,{"county":"EL Paso","registered_voters":461149})
voting_data

#remove Arapahoe
voting_data.pop(0)
voting_data

#make denver to 3rd position, keep jefferson in the 2nd position
voting_data[2]={"county":"Denver","registered_voters":463353}
voting_data[1]={"county":"Jefferson","registered_voters":432438}
voting_data

#add arapahoe
voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for votings in voting_data:
    for county, registered_voters in votings.items():
        print(f'{county} county has {registered_voters} registered voters.')

