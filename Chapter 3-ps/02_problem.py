letter  = '''Dear <|name|>,
you are selected!
<|Date|>'''

# name = input("Enter your  name :")
# Date = input("Enter the Date :")

print(letter.replace("<|name|>", "Harry").replace("<|Date|>", "30 sep 2030"))             