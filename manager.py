# Print all of the to-do items in the list.
# Add a new item to the list.
# Mark an item as completed.

class Manager(object):
    todos = open('todos.txt', 'r')

    def start():

        print("Choose a day you will like to make a plan.")
        choice = input("")
        if choice == "Monday":
            todos.read()
        elif choice == "Tuesday":
            todos.read()
        elif choice == "Wednesday":
            todos.read()
        elif choice == "Thursday":
            todos.read()
        elif choice == "Friday":
            todos.read()
        elif choice == "Saturday":
            todos.read()
        elif choice == "Sunday":
            todos.read()
        else:
            print("Incorrect spelling")
            start()

        print()
        todo = open('todos.txt', 'a+')
        print("Type in your new plan! ")
        #Getting What To Write To File
        text = input("")
        #Actually Writing It
        todo.write(f"{choice}: {text} \n")
        todo.close()

    def read():
        print()
        print("These are your plans for the week: ")
        todos = ('todos.txt')
        if os.path.isfile(todos):
            todos = open('todos.txt', 'r')
            print(todos.read())
        else:
            print("Error")
            start()
