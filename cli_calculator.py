num_1 = int(input('Enter your first number: '))
num_2 = int(input('Enter your second number: '))
 
# Addition
print('{} + {} = '.format(num_1, num_2))
print(num_1 + num_2)
 
# Subtraction
print('{} - {} = '.format(num_1, num_2))
print(num_1 - num_2)
 
# Multiplication
print('{} * {} = '.format(num_1, num_2))
print(num_1 * num_2)
 
# Division
print('{} / {} = '.format(num_1, num_2))
print(num_1 / num_2)

#Modulus
print('{} % {} = '.format (num_1, num_2))
print (num_1 % num_2)


import zipfile
my_zip = zipfile.ZipFile('files.Zip', 'w')

my_zip.write ('cli_calculator.py')

my_zip.close()