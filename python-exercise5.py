# Get user to input a number, then convert the number to a string. 
# Tell the user to go to work or sleep in based on day of week.

# Capture users input into a variable
day = int(input('Day (0-6)? '))

# Output if user should Go to work or sleep in
if day == 0 or day == 6:
    print('Sleep in')
else:
    print('Go to work')



