"""
Ian Pope
ICP #1
"""
import statistics
import math

#Question 1
#Uses some of the built in functions to sort and get min/max
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(f"The min age is {min(ages)}, and the max age is {max(ages)}")

#Use pythons libraries to get median
print(f"The median age is {statistics.median(ages)}")

#Gets average age within the list
totalAge = 0
for age in ages:
    totalAge += age
averageAge = totalAge / len(ages)
print(f"The average age is {averageAge}")

#Gets range using min and max functions
print(f"The range of ages is {max(ages) - min(ages)}\n")


#Question 2
#Creates empty dictionary and fills with value, key pairs
dog = {}
dog["name"] = "Sasha"
dog["color"] = "Brown"
dog["breed"] = "German Shepard"
dog["legs"] = "4"
dog["age"] = "5"
print("Dog is", dog)

#Creates student info
student = {"first_name" : "Ian", "last_name" : "Pope", "gender" : "Male", "age" : 20,
           "marital_status" : "single", "skills" : ["java", "python"], "country" : "USA",
           "city" : "Warrensburg", "address" : "123 McGoodwin"}
print(f"The length of student is {len(student)}")

#Gets the value and typing from a dictionary entry
skillsList = student["skills"]
skillsType = type(student["skills"])
print(f"The value of skills is {skillsList} and it is of type {skillsType}")

#Appends skill on dictionary entry
student["skills"].append("C++")
print(f"The value of skills is {skillsList}")

#Gets the dictionary keys and values
print("The dictionary keys are", student.keys())
print("The dictionary values are", student.values())
print()


#Question 3
#Creates new tuples based on my family as tuples
brothers = ("David",)
print("My brothers are", brothers)
sisters = ("Cherish",)
print("My sisters are", sisters)
siblings = brothers + sisters
print("My siblings are", siblings)
print(f"I have {len(siblings)} siblings")
family_members = siblings + ("Jeffrey", "Tamara")
print("My family members are", family_members)
print()

#Question 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("The length of it_companies is", len(it_companies))

#Adds 3 companies and the removes 1
it_companies.add('Twitter')
it_companies.update(['Samsung', 'Dell'])
print(it_companies)
it_companies.remove('Facebook')
print(it_companies)

#The remove function will raise an error if the key is not found in the list
#The discard function will not raise an error if the key is not found
print("The remove() function will raise an error is key is not found while discard() will not")

#Gets the union of A and B
A_b = A | B
print("A union B", A_b)

#Gets the intersection of A and B
A_b = A & B
print("A intersection B", A_b)

#Uses set functions to check if A is a subset of B and if they are disjoint
if A.issubset(B):
    print("A is a subset of B")
else:
    print("A is not a subset of B")

if A.isdisjoint(B):
    print("A and B are disjointed")
else:
    print("A and B are not disjointed")

#Shows that A union B is the same as B union A
A_b = A | B
print(A_b)
A_b = B | A
print(A_b)
print("A|B and B|A are the same")

#Shows what items belong to only one set
print("The symetric difference of A and B is", A.symmetric_difference(B))

#Deletes the sets from memory
del A
del B
del A_b

#The length of ages is longer before being turned into a set because sets do not allow duplicates
ages_set = set(ages)
print(f"The length of ages list is {len(ages)}, of ages set {len(ages_set)}\n")


#Question 5
#Gets the area and circumference of a circle for radius 30 and a user input
radius = 30

_area_of_circle_ = math.pi * radius * radius
print(f"The area of the circle is {_area_of_circle_} square meters")

_circum_of_circle_ = 2 * math.pi * radius
print(f"The circumference of the circle is {_circum_of_circle_} meters")

radius = int(input("Enter the radius of the circle in meters: "))
_area_of_circle_ = math.pi * radius * radius
print(f"The area of the circle is {_area_of_circle_} square meters\n")


#Question 6
#Splits the string and turns it into a set to delete duplicate words
str = "I am a teacher and I love to inspire and teach people"
unique_words = set(str.split(" "))
print("The unique words in the sentence are", unique_words)
print()


#Question 7
#Uses tab
print("\tName\tAge  Country City")
print("\tAsabeneh 250  Finland Helinski\n")


#Question 8
#Uses string format function
radius = 10
area = math.pi * radius ** 2
txt = "The area of a circle with radius {radius:.0f} is {area:.0f} meters square."
print(txt.format(radius = radius, area = area))
print()


#Question 9
#Gets the number of students
N = int(input("How many students: "))
kgList = []
lbsList = []

#Gets the weights from user in lbs
for i in range(N):
    lbsList.append(eval(input("Enter students weight in lbs: ")))

#Converts lbs to kg
for weight in lbsList:
    kgList.append(int(weight * 45.359) / 100)

print("Lbs:", lbsList)
print("Kgs:", kgList)


