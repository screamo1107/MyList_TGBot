import telebot
import os


TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)


todo_list = []  # Re-work to Store in DB


@bot.message_handler(commands=['add'])
def add_todo_item(message):
    item = message.text[5:]
    todo_list.append(item)
    bot.send_message(message.chat.id, f'{item} item was added to your list!')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIWV194sVRFrEXJh08_qKC4gW9tZZpnAAJGAANSiZEj-P7l5ArVCh0bBA')
    # TBD: Add item handling


@bot.message_handler(commands=['list'])
def get_todo_list(message):
    todo_list_print = str('n/'.join(todo_list))
    bot.send_message(message.chat.id, 'Here is your TODO list:')
    bot.send_message(message.chat.id, todo_list_print)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIWWV94sYnO0qGG3RGL1_ANXOOlB-TRAAJQAwACtXHaBsOq9o3QxaLKGwQ')
    # TBD: Add list handling


@bot.message_handler(commands=['delete'])
def delete_list_item(message):
    pass


@bot.message_handler(commands=['help'])
def show_help_message(message):
    pass


@bot.message_handler(commands=['reorder'])
def swap_list_items(message):
    pass


bot.polling()
