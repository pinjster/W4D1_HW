# You are to write a Python function named nickname_generator. This function should take a single argument, name, which is a string, and return a nickname based on the following rules:

# If the third letter of name is a consonant, the function should return the first three letters as the nickname. For example, 
# nickname_generator("Robert") should return "Rob".

# If the third letter of name is a vowel, the function should return the first four letters as the nickname. For example, 
# nickname_generator("Jeannie") should return "Jean".

# If the string name has fewer than four characters, the function should return the string "Error: Name too short".
# Notes:

# For the purposes of this exercise, consider the vowels to be "aeiou". The letter "y" should be treated as a consonant.

# The input will always be a string, with the first letter capitalized and the rest in lowercase (e.g., "Sam").

def nickname_generator(name):
    if len(name) < 4:
        return "Error: Name too short"
    if name[2] in ['a','e','i','o','u']:
        return name[0] + name[1] + name[2] + name[3]
    else:
        return name[0] + name[1] + name[2]
    
print(nickname_generator('Robert'))
print(nickname_generator('Jeannie'))
print(nickname_generator('Sam'))