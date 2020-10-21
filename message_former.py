import db_actions


class ListItem:
    def __init__(self, message, priority='P2', deprecated=0):
        self.text = message.text  # TBD
        self.priority = priority
        self.message_id = message.message_id  # Get id from message
        self.deprecated = deprecated

    def add_item_to_list(self):
        print(self.message_id, self.text, self.priority, self.deprecated)
        db_actions.add_item(self.message_id, self.text, self.priority, self.deprecated)

    def deprecate_item(self):
        self.deprecated = True

    def update_priority(self, new_priority):
        self.priority = new_priority


def get_message_active_items() -> str:
    lst1 = db_actions.get_all_items_to_display()
    lst2 = [str(x[0]) + " " + str(x[1]) + " " + "(" + str(x[2]) + ")" for x in lst1]
    formed_msg = "Here is your To-Do list:\n" + "\n".join(lst2)
    return formed_msg


def get_all_message_items() -> str:
    lst1 = db_actions.get_all_items()
    lst2 = [str(x[0]) + " " + str(x[1]) + " " + "(" + str(x[2]) + ")" + str(x[3]) for x in lst1]
    formed_msg = "Here is the full list:\n" + "\n".join(lst2)
    return formed_msg
