# String Concatenation

first = 'Brian'
last = 'Muthuure'
full_name = first + ' ' + last

name = 'Manchester United'
# print(len(name))

sliced = name[3:6]
# print(sliced)

print(name.capitalize())  # Capitalize

print(name.count('e'))  # Count

print(name.endswith('er'))  # False
print(name.endswith('ted'))  # True

print(name.find('n'))  # Returns the index of n

print(name.isalnum())  # Find if its alphanumeric

string2 = 'Brian6894'
print(string2.isalnum())  # Its alphanumeric

# join(): Returns a concatenated string
languages = ['Python', 'Java', 'PHP', 'Kotlin', 'Ruby']
result = '; '.join(languages)
print(result)

# strip() # Removes both leading and trailing characters

challenge = 'I want to go home'
print(challenge.strip('e'))  # Removes e from the string

# replace()
s1 = 'I love Java'
print(s1.replace('Java', 'Python'))

# splits() Splits a string
s2 = 'Ruby C++ C Java PHP Python Kotlin'
sp = s2.split()  # ['Ruby', 'C++', 'C', 'Java', 'PHP', 'Python', 'Kotlin']
print(sp)
