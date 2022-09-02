Dog = {}

Dog.update({
    'name' : 'Buddy',
    'color' : 'White',
    'breed' : 'Labrador',
    'legs' : '4',
    'age' : '7'
    })


#student dictionary
Student = {
    'first_name' : 'Sai_Pavana_Niharika',
    'last_name' : 'Kali',
    'gender' : 'Female',
    'age' : '23',
    'marital status' : 'Unmarried',
    'skills' : ["C","Java","Python","Tableau"],
    'country' : 'India',
    'city' : 'Rajahmundry',
    'address' : 'APPM Staff Quarters, Sri Ram Nagar, Rajahmundry, 533106'
}
#length of student dictionary
print("Length of the Student dictionary is", len(Student))

#Get the value of skills and check the data type
print("skills of the student are ", Student['skills'])
print("datatype of the skills is", type(Student['skills']))

#modifying

Student['skills'].extend(["PowerBI", "Microstrategy"])
print("Modified skills in the list are", Student['skills'])

#keys as list

print("Keys in the student dictionary are", list(Student.keys()))
print("values in the student dictionary are", list(Student.values()))