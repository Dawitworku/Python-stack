# 1 Update Values in Dictionaries and Lists
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# # A. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# x[1] [0] = 15
# print(x)

# # B. Change the last_name of the first student from 'Jordan' to 'Bryant'
# students[0] ['last_name'] = 'Bryant'
# print(students)

# # C. In the sports_directory, change 'Messi' to 'Andres'
# sports_directory['soccer'] [0] = 'Andres'
# print(sports_directory)

# # D. Change the value 20 in z to 30
# z[0] ['y']= 30  # z is a list that has a dictionary inside of it.
# print(z)
#2 Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# def iterateDictionary(list):
#     # First method
#     for i in list:                                   # iterates through the array
#         for key,val in i.items():                    # iterates within the dictionary
#             print(f"{key} - {val}")
#     print("**********************")    
#     # Another way of doing this
#     for i in list:                                   # iterates through the array
#         str = ''
#         for key,val in i.items():                    #  iterates within the dictionary
#             str += f"{key} - {val}, "
#         print(str)
#     print("**********************")    
#     # Another way of doing this
#     for i in list:                                   # iterates through the array
#         str = '' 
#         for j in i.keys(): 
#             str += f"{j} - {i[j]}, "                 #grabs and concatnates key: value in each "i" iteration
#         print(str)
# # To be able to print the key & values same way on the list, we have to store the value of each iteration inside of a varable.            
# iterateDictionary(students)

# 3 Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])   # This will go through each iteration and grab the first name or last name
# Or could be done using the in range for loop
    # for i in range(len(some_list)):
    #     print(some_list[i][key_name])


iterateDictionary2('first_name', students) 
print("**********************")
iterateDictionary2('last_name', students) 
# 4 Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
# first way of doing this    
    # arr = []
    # for key,val in some_dict.items():   # prints the length of the list in the dictionary
    #     print(f"{len(val)} {key.upper()}")
    #     arr=val
    #     for i in arr:
    #         print(i)
#second way of doing this   
    # for key,val in some_dict.items():   # prints the length of the list thats inside the dictionary
    #     print(f"{len(val)} {key.upper()}")
    #     for i in val:
    #         print(i)   
# printInfo(dojo)

    for i in some_dict.keys():   # .keys method will help me wit grabing the keys of the dictionary
        print(f"{len(some_dict[i])} {i.upper()}")
        for i in some_dict[i]:
            print(i)
        print("\n")
        
printInfo(dojo)




