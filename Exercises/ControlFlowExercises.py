print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:
print(x[0:5])


print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
even = []
for i in x:
    if i % 2 == 0:
        even.append(i)
print(even)

print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
even = []
for i in x[:5]:
    if i % 2 == 0:
        even.append(i)
print(even)

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
first = []
for i in names:
    first.append(i[0])
print(first)

print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
spaces = []

substring = " "

for i in names:
    spaces.append(i.index(substring))

print(spaces)

print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:

initials = []

for i in names:
    name_initials = "" # Initialise a string so we can add to it later
    for j in i.split(): # Split the strings in "names" and loop through the resulting list (for example "Alan Turing" becomes ["Alan", "Turing"])
        name_initials += j[0] # Add to the name_initials string created earlier
    initials.append(name_initials)
print(initials)

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a:

for i in list_of_lists:
    if len(set(i)) == len(i): # Since sets get rid of duplicates, just equate the lengths
        print(i)

# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:

while True:
    number = input("Please input a number greater than 100 ")
    number = int(number)
    if number > 100:
        print("You inputted " + str(number))
        break
    else:
        print("You did not input a number greater than 100, please try again")

print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:

while True:
    number = input("Please input a number greater than 100 ")
    number = int(number)
    if number > 100:
        print("You inputted " + str(number))

        if number > 1:
            for i in range(2, (number // 2)+1):
                if number % i == 0:
                    print(str(number) + " is not prime")
                    break
            else:
                print(str(number) + " is prime")
        break
    else:
        print("You did not input a number greater than 100, please try again")



