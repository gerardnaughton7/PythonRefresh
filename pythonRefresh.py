age = 19
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
