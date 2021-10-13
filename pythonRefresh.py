'''age = 19
name = "Nick"

todayIsCold = True

# This is a refresh file

if name == "Nick": 
    print('You are older than 18')
else: 
    print('You are younger than 18')


#Function

def hello(name="sean", age= 0):
    return 'Hello {} you are {} years old'.format(name, age)

sentence = hello()

print(sentence)

def tripleprint(string):
    print(string*3)

tripleprint("hello")

# Lists

dognames = ['fido', 'Sean', 'sally', 'mark']

print(dognames)

dognames.insert(0, "mike")

print(dognames[3])
print(dognames)

del(dognames[0])

print(len(dognames))

dognames[3] = 'john'
print(dognames)

#Lists challenge
shoes = ['Spizikes', 'Aire Force 1', 'Curry 2','Melo 5']
print(shoes)

# Loops

dognames = ['fido', 'Sean', 'sally', 'mark']

for dog in dognames:
    print(dog)

for x in range(0,9):
    print(x)

age = 0

while age < 6:
    print(age)
    age += 1

# Loop exercise

numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 45, 33, 38, 10, 40, 44, 70, 81, 79, 28, 83, 41, 14, 16, 27, 38, 20, 84, 24, 50, 59, 71, 1, 13, 56, 91, 29, 54, 65, 23, 60, 57, 13, 39, 58, 94, 94, 42, 46, 58, 59, 29, 69, 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18, 98, 72, 96, 26, 13, 7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]

for num in numbers:
    if num > 90:
        print(num)'''

# Dictionary

dogs = {'fido':8, 'Sally':17, 'Sean':2}

del(dogs['Sean'])

print(dogs)
print(dogs['Sally'])

dogs['sarah'] = 19
print(dogs)

# Dictionary Exercise

words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]
cooldictionary = {}

for i in range(0,3):
        cooldictionary[words[i]] = definitions[i] 

print(cooldictionary)        
















