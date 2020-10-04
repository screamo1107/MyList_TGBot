import db_actions


def get_all_list_items():
    lst1 = db_actions.get_all_items()
    lst2 = [x[0] for x in lst1]
    formed_msg = "\n".join(lst2)
    return formed_msg


class List:
    def __init__(self):
        pass

    def add_list_item(self):
        pass  # DB action

    def delete_list_item(self):
        pass  # DB action
