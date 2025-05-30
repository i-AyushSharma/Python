letter = "Hey my name is {1} and I am from {0}"
name = "Ayush"
country = "India"
print(letter.format(country, name))

print(f"Hey my name is {name} and I am from {country}")

txt = "For only{price:.2f} dollars"
print(txt.format(price = 49.999))

print(f"{2*30}")
print(type(f"{2*30}"))
print(f"Hey my name is {{name}} and I am from {{country}}")
