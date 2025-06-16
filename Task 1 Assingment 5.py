dictionary = {'Arif':71,'Aman':89,'Ayesha':95,'Rani':98}
Name = input("Enter the Student's Name:")
if (Name in dictionary):
    print(Name,"'s","marks is:" , dictionary[Name])
else:
    print("Student not found")

