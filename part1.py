f'''
______
PART 1
______
The code below prompts the user to enter two numbers, and then prints out the smaller of the numbers entered. Modify so that it prompts the user to enter THREE numbers, and then prints the smallest of the three numbers entered in a sentence.

(Hint: You'll need to be careful for the cases when the user enters the same number twice or all three times.)

An example of what should appear on the console when the code is run:

Enter a number: 11
Enter another number: 2
Enter another number: 5

The smallest number is 2
'''

one = int(input("Enter a number: "))

two = int(input("Enter another number: "))

three = int(input("Enter another number: "))

if one < two and one < three: 
  print("The smallest number is ", one)
if two < one and two < three:
  print("The smallest number is ", two)
if three < one and three < two:
  print("The smallest number is ", three)

if one == two and one < three: 
  print("The smallest number is ", one)
if one == three and one < two:
  print("The smallest number is ", one)
if two == three and two < one: 
  print("The smallest number is ", two)

if one == two == three:
  print("The smallest number is ", one)

#this is not what the instructions intend for me to write but I'm exceedingly confused and have spent too many hours on this assignment already so in case these assignments are actually looked over by someone, sorry 