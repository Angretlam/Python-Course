#################################################
# Script for the if Python lesson               #
# The goal behind this lesson script is to demo #
# the capabilities of the IF statement. This    #
# program requires that the student understands #
# how different operators work.                 #
#################################################
import os

os.system("clear")

x = 1 
y = 0

print(' \n \
Given the following code what would expect the output to be? \n \
\n \
y = 0 \n \
\n \
 if y: \n \
	print(\'This is a true statement\') \n \
 else: \n \
	print(\'This is a false statement\') \n ')

v = 'NULL'

while v != 0:
	v = int(input('\n Enter 0 for false and 1 for true: '))
	if v == 1:
		print (' That is incorrect. Try again.')

if v == 0:
	print('\n\
 That is correct. In Python Boolean Values are represented \n\
 by 1s and 0s. 0s always reflect a false value where as 1s \n\
 always represent a true value. \n ')

input(' Press any key to continue. ')


os.system("clear")

print(' \n \
Given the following code what would expect the output to be? \n \
\n \
y = \'False\' \n \
\n \
 if y: \n \
        print(\'This is a true statement\') \n \
 else: \n \
        print(\'This is a false statement\') \n ')

v = 'NULL'

while v != 1:
        v = int(input('\n Enter 0 for false and 1 for true: '))
        if v == 0:
                print (' That is incorrect. Try again.')

if v == 1:
        print('\n\
 That is correct. In Python Boolean Values are represented \n\
 by 1s and 0s. This is dissimilar to other languages where \n\
 TRUE and FALSE are taken literally for their values. \n ')


