# Convert the user's input of temperature in celsius to fahrenheit, and display output

# User's input in celsius
temp_in_c = int(input('Temperature in C? '))


# Convert to fahrenhit
temp_in_f = (temp_in_c * (5/9)) + 32

message = f'{temp_in_f} F'

# Output in fahrenheit
print(message)