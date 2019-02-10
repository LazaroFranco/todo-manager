import sys
import datetime
# A timestamp of when they were created DONE
# A boolean marking the item as completed or not DONE
# Text of the actual to-do item DONE

class Item(object):

    def __init__(self, task):
        self.task = task
        self.timestamp = datetime.datetime.now()
        self.boolean = False
