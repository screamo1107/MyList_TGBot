import telebot
import os
from message_former import ListItem, get_all_message_items, get_message_active_items


TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['add'])
def add_todo_item(message):
    item = ListItem(message)
    item.add_item_to_list()
    bot.send_message(message.chat.id, "Item was added to your list!")
    # bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIWV194sVRFrEXJh08_qKC4gW9tZZpnAAJGAANSiZEj-P7l5ArVCh0bBA')


@bot.message_handler(commands=['deprecate'])
def deprecate_list_item(message):
    item = ListItem(message)
    item.deprecate_item()
    bot.send_message(message.chat.id, "Item was deprecated!\n"
                                      "To see all items (including deprecated) use /flist command)")


@bot.message_handler(commands=['/flist'])
def get_full_list(message):
    message_to_print = get_all_message_items()
    print(message_to_print)
    bot.send_message(message.chat.id, message_to_print)
    # bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIWWV94sYnO0qGG3RGL1_ANXOOlB-TRAAJQAwACtXHaBsOq9o3QxaLKGwQ')


@bot.message_handler(commands=['list'])
def get_todo_list(message):
    message_to_print = get_message_active_items()
    bot.send_message(message.chat.id, message_to_print)
    # bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIWWV94sYnO0qGG3RGL1_ANXOOlB-TRAAJQAwACtXHaBsOq9o3QxaLKGwQ')


@bot.message_handler(commands=['help'])
def show_help_message(message):
    bot.send_message(message.chat.id, """
    Available commands:
    /list - Return your To-Do list
    /add <item> - Add a new item to your To-Do list
    /delete <item_id> - Remove selected item from the list
    /reorder <item1_id> <item2_id> - Swap the items in the list
    """)


@bot.message_handler(commands=['reorder'])
def swap_list_items(message):
    pass


bot.polling()
