import db_actions as db_actions


class ListItem:
    def __init__(self, message, priority='P2', deprecated=False):
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

