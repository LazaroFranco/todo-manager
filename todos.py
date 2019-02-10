from manager import Manager
from item import Item

app = Manager(Item)
app.start()
app.print_item()
app.read()
app.complete()
