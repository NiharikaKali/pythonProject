
# tuple with names of sisters and brothers
sisters = ("Niha", "Vysh", "Harshi", "Sush", "Sailu")
brothers = ("Srikar", "Venkat", "Krishna")
print("Sisters are",sisters)
print("Brothers are",brothers)

# joining brothers and sisters

siblings= sisters + brothers
print("Updated list of siblings is",siblings)

#count of siblings

count_siblings= len(siblings)
print("Total count of the siblings is",count_siblings)

#appending father and mother

mother = "Sujatha"
father= "Radha_Krishna"

family_members = list(siblings)

family_members.append(father)
family_members.append(mother)
family_members=tuple(family_members)
print("Total family members list is",family_members)
