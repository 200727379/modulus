#Author: Mothapo Rampedi Lesley
#Email: rampedilesley@gmail.com
#28 April 2021
"""Write a program that reads in two integers and determines and prints whether the first is a
multiple of the second. (Hint: Use the modulus operator.)
"""

integer1 = int(input("Enter the first integer:  ")) #read the first integer
integer2 = int(input("Enter the second integer:  ")) #read the second integer

if (integer1 % integer2) == 0: #test statement
    print(f"{integer1} is a multiple of {integer2}") #print the results