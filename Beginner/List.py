#List
justice_league=["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]
#count number of members in justice laegue
print(len(justice_league))
#Append Batgirl and Nightwing as new memebers
justice_league.extend(['Batgirl','Nightwing'])
print(justice_league)
#Move wonder woman to the beginning of  a list
old_index=2
new_index=0
item=justice_league.pop(old_index)
justice_league.insert(new_index,item)
print(justice_league)
#move green lantern or superman in between aquaman and flash
item2=justice_league.pop(1)
justice_league.insert(3,item2)
print(justice_league)
#replace the items with new members
justice_league=['Cyborg','Shazam','Hawkgirl','Martian Manhunter','Green Arrow']
print(justice_league)
#sort the items in alphabetical order
print(sorted(justice_league))
#Cyborg will be the new leader! WooHoo!!