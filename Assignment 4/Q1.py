person_dict={'first_name':'Hamza','last_name':'Khan',
            'age':20,'city':'Karachi'}

for key, value in person_dict.items():
    print(key,":",value)
print("\nAdd Qualification \n")
person_dict["qualification"]="Intermediate"
print('qualification :',person_dict["qualification"])

print("\nUpdate Qualification \n")
person_dict["qualification"]="High Academic"
for key, value in person_dict.items():
    print(key,":",value)

print("\nDelete Qualification \n")
del person_dict["qualification"]
print(person_dict)
