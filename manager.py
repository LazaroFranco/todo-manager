# Print all of the to-do items in the list.
# Add a new item to the list.
# Mark an item as completed.

class Manager(object):

    def start(self):
        todos = open('todos.txt', 'r')
        print("Welcome! Choose a day you will like to make a plan.")
        self.choice = input("")
        if self.choice == "Monday":
            todos.read()
        elif self.choice == "Tuesday":
            todos.read()
        elif self.choice == "Wednesday":
            todos.read()
        elif self.choice == "Thursday":
            todos.read()
        elif self.choice == "Friday":
            todos.read()
        elif self.choice == "Saturday":
            todos.read()
        elif self.choice == "Sunday":
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
        todo.write(f"{self.choice}: {text} \n")
        todo.close()

    def read(self):
        print()
        print("These are your plans for the week: ")
        todos = ('todos.txt')
        if (todos):
            todos = open('todos.txt', 'r')
            print(todos.read())
        else:
            print("Error")
            start()

    def complete(self):
        print("mark an item as done")
