# Strings are immutable
a = "Apple"
print(a.upper()) #To convert the whole string into Uppercase(WASD)
print(a.lower()) #To convert the whole string into Lowercase(wasd)

b = "Banana !!!"
print(b.rstrip("!")) #To remove any trailing(at the end of the string) charaters from the string

print(b.replace("Banana", "Mango")) #To replace all ocurrences of the string with another one

print(b.split( )) #To convert a string into a list

blogheading = "introduction to pYthon"
print(blogheading.capitalize()) #To convert the letters into uppercase or lowercase as per english grammer

c = "Hello World"
print(len(c))
print(len(c.center(50)))
print(c.center(50))

print(b.count("a")) #To count the occurrence of a letter or a word in a given string

print(c.endswith(" ")) #To check whether the string is ending with a choosen element

str1 = "His name is Dan, he is a honest man"
print(str1.find("is")) #To find the first occurrence of a letter or word in a string. *If there is no occurrence, the output will be "-1"

print(str1.index("is")) #To find the first occurrence of a letter or word in a string. *If there is no occurrence, the output will be an error

print(str1.isalnum()) #To check the entire string contains only A-Z, a-z, 0-9

print(str1.lower()) #To check the entire string is in lowercase

print(str1.isprintable()) #To check whether all the charaters present in the string are printable. eg. /n is not a printable character

str2 = "       "
print(str2.isspace()) #To check whether the string contains wide space

print(str1.istitle()) #To check whether all the word's first letter is in capital

print(str1.isupper()) #To check whether all the words are in capital

str3 = "!!!Ayush"
print(str3.startswith("!")) #To check whether the srting starts with choosen element

print(str1.swapcase()) #To swap the lowercase letter into uppercase letter and vice versa

print(str1.title()) #To convert first letter of all the words in a string into capital letter