# ****Write a Python program to display a user-entered name followed by Good Afternoon
# using input() function.******
name = input("Enter your name,")
print("Good Aternoon,",name)


# """Write a program to fill in a letter template given below with name and date."""
# '''letter = ‘’’ Dear <|NAME|>,

#                         You are selected!

#                         <|DATE|>'''
                        
letter = '''letter = ‘’’ Dear <|NAME|>,

                        You are selected!

                        <|DATE|>'''
name = input("Enter your name\n")
date = input("Enter your date\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)


# ****Write a program to detect double spaces in a string.******


Name = "One day I become biggest  person in the world"
doublespace = Name.find("  ")
print(doublespace)

