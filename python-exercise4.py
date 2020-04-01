# Get the user to input a number that will be turned into the day of the week represented by that number.
# Add user input to a variable and convert to integer
day = int(input('Day (0-6)? '))

# Output the users input as string for dayo of week represented by that number
# # Convert integer into string output
if day == 0:
    print('Sunday')
elif day == 1:
    print('Monday')
elif day == 2:
    print('Tuesday')
elif day == 3:
    print('Wedensday')
elif day == 4:
    print('Thursday')
elif day == 5: 
    print('Friday')
else:
    print('Saturday')
