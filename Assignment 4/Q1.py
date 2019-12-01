person_dict={'first_name':'Muhammad','last_name':'Hashim',
            'age':28,'city':'Karachi'}

for key, value in person_dict.items():
    print(key,":",value)
print("\nAdd Qualification \n")
person_dict["qualification"]="Graduate"
print('qualification :',person_dict["qualification"])

print("\nUpdate Qualification \n")
person_dict["qualification"]="High Academic"
for key, value in person_dict.items():
    print(key,":",value)

print("\nDelete Qualification \n")
del person_dict["qualification"]
print(person_dict)
