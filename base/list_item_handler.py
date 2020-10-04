class ListItem:
    def __init__(self, message, priority='P2', deprecated=False):
        self.text = message.text  # TBD
        self.priority = priority
        self.message_id = message.message_id  # Get id from message
        self.deprecated = deprecated

    def deprecate_item(self):
        self.deprecated = True

    def update_priority(self, new_priority):
        self.priority = new_priority
