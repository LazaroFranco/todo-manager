import sys

print("Choose a day you will like to make a plan.")
answer = input()


if answer == "Monday":
    add = input()
    print("Monday - " + add)

#aList = print("Monday - "), input("")

# Open the file for writing
todoFile = open('todos.txt', 'a+')

# Loop through each item in the list
# and write it to the output file.
for eachitem in answer:
    todoFile.write(str(eachitem))

# Close the output file
todoFile.close()
