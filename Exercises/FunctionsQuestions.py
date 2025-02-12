print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:

def divisor(number):
    divisors_list = []

    for i in range(1, number+1): # number+1 to include the number itself
        if number % i == 0:
            divisors_list.append(i)
    return divisors_list

print(divisor(12))

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:

def factor(num1, num2):
    if num1 in divisor(num2):
        return True
    elif num2 in divisor(num1):
        return True
    else:
        return False

print(factor(6, 12))
# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:
def alphabet_position(letter):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

    for i in range(len(alphabet)):
        if alphabet[i] == letter:
            return  i


print(alphabet_position("z"))

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

def id_creator(name):
    letters = list(name) # Split up the name into a list of letters
    id = "" # Create ID string
    for i in letters:
        id += str(alphabet_position(i)) # Concatenate id
    return id

print(id_creator("bob"))

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:

def password(name):
    id = id_creator(name)
    id_list = [int(i) for i in id]
    id_sum = sum(id_list)
    return int(id) - id_sum

print(password("bob"))

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def prime(number):
    if number > 1:
        for i in range(2, (number // 2) + 1):
            if number % i == 0:
                return False
        return True
    else:
        return False

print(prime(5))

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:

def prime(number):

    if not isinstance(number, int):
        return "Input must be an integer!"

    if number > 1:
        for i in range(2, (number // 2) + 1):
            if number % i == 0:
                return False
        return True
    else:
        return False

print(prime(5))

# -------------------------------------------------------------------------------------- #






