# Alec Malenfant amalenf@pnw.edu
# Assignment 01
# Problem 02
# This program will find the sum of the even values of the fibonacci sequence < 100000

# Initial Values
limit = 100000 #100,000
sequence = [0, 1] #Initialize an array with the first two values of the fibonacci sequence
newElement = 0

# Creat an sequence with the Fibonnaci Sequence
while 1 != 0 : #infinite loop condition
    newElement = sequence[-1] + sequence[-2] #add the 2 most previous terms together
    if newElement > limit: #end loop condition
        break
    else:
        sequence.append(newElement)

# Iterate through the sequence and find the sum of the even values
sum = 0
for i in sequence:
    if i % 2 == 0:
        sum += i
    else:
        continue

#print results
print("Fibonnaci Sequence : " + str(sequence))
print("Sum of even numbers : " + str(sum))

# Wait for user input to kill the running program
input("Press enter to quit ")
quit()
