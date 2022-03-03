from .stock import *

class Alert:

    alerted = False

    def __init__(self, category, itemId, itemColor, itemSize, phoneNumber):
        self.category = category
        self.id = itemId
        self.color = itemColor
        self.size = itemSize
        self.number = phoneNumber

    def check(self):
        if perform_tasks(self.category, self.id, self.color, self.size):
            send_msg(self.id, self.color, self.size, self.number)
            alerted = True

    def to_string(self):
        return f"Alert created for {self.id} in {self.color}, size {self.size} to be sent to {self.number}"

