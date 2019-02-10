from item import Item
# Print all of the to-do items in the list.
# Add a new item to the list.
# Mark an item as completed.

class Manager(Item):

    def start(self):
        todos = open('todos.txt', 'r+')
        print("Welcome! Choose a day you will like to make a plan.")
        global choice, date
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
        print("Particular Date?")
        date = input("")


    def print_item(self):


        print()
        todo = open('todos.txt', 'a+')
        print("Type in your new plan! ")
        #Getting What To Write To File
        self.task = input("")

        #Actually Writing It
        todo.write(f"""\n On {choice}:
         Task: {self.task}
         Task Dated For: {date}
         Task done?: {self.completed}
         Task Created on: {self.timestamp}
         \n""")
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

        todos = open('todos.txt', 'r+')
        check_tasks = todos.readlines()
