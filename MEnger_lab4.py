#Max Enger
#Lab 4
#IDCE 302
#September 13, 2019
#Time 25 mins
#Creating a temperature gathering function that accepts user inputs(int) and returns a category(str).

print('Happy Friday the 13th! Welcome to my temperature function!')

def feelTemp():
#Gathering user input
    t = int(input('Hi there! Please enter the temperature:'))
    print(t)
#Running the function
    if t >= 100:
        return("Wow! It is hot.")
    elif t >= 70 and t <100:
        return("Perfect. It is warm.")
    elif t >= 32 and t <70:
        return("Brrr. It is cool.")
    else:
        return("I need a jacket! It is cold.")
    
#Calling the Function
print(feelTemp())
