#user_text = input('Enter some text: ') #prompts, you can actually type into the terminal to input something

#print(user_text.upper())

#user_number = input("what do you want to double? ")

#print(user_number * 2) #only works with strings. to treat as an int, you have to wrape it in int()

#user_number2 = input("what do you want to double? ")

#print(int(user_number2)*2)

# 1st ask for some text, then prompt to enter 1 to uppercase and 2 to lowercase, then do that for them

chall_text = input('Enter some text: ') 
print(chall_text)

chall_case = input('Enter 1 for upper and 2 for lower: ')
if chall_case == '1': #remeber it's treated as a string!
  print(chall_text.upper())
if chall_case == '2':
  print(chall_text.lower())

