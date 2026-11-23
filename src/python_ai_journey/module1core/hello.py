from datetime import date

name = "Vigani"
print(f"Hello, {name}! Today is {date.today()}")

name = "Vigani"
years = 5
price = 199.5
is_senior = years >= 4

print(f"{name} has {years} years of experience")
print(f"Price: {price:,.2f}")

if years >= 4:
    level = "Senior"
elif years >= 2:
    level = "Mid"
else:
    level = "Junior"

print(f"{name} is a {level} developer")
level = "Senior" if years >= 5 else "Mid" if years >= 2 else "Junior"
print(f"{name} is a {level} developer")
for i in range(3):
    print(i)

text = "Python fo AI"
print(text.lower(), text.split(), text[0:6], text[-2:])
print(text[::-1])
print(text[::2])
print(text[:5:2])
