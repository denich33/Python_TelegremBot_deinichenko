import os
from datetime import datetime
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import psycopg2

# Инициализация базы данных и таблиц
def initialize_database():
    conn = psycopg2.connect(
        dbname="your_database_name",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            event_date TIMESTAMP NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Класс для работы с событиями
class EventManager:
    def __init__(self, user_id):
        self.user_id = user_id

    def add_event(self, title, event_date):
        conn = psycopg2.connect(
            dbname="your_database_name",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        )
        cursor = conn.cursor()
        cursor.execute('INSERT INTO events (user_id, title, event_date) VALUES (%s, %s, %s)',
                       (self.user_id, title, datetime.strptime(event_date, '%Y-%m-%d %H:%M:%S')))
        conn.commit()
        conn.close()

    def get_all_events(self):
        conn = psycopg2.connect(
            dbname="your_database_name",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        )
        cursor = conn.cursor()
        cursor.execute('SELECT title, event_date FROM events WHERE user_id = %s', (self.user_id,))
        events = cursor.fetchall()
        conn.close()
        return [f"{event[0]} ({event[1].strftime('%Y-%m-%d %H:%M:%S')})" for event in events]

# Обработчики команд для Telegram бота
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет Я бот для работы с календарем.')

def add_event(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    event_manager = EventManager(user_id)
    event_title = ' '.join(context.args[:-1])
    event_date = context.args[-1]
    event_manager.add_event(event_title, event_date)
    update.message.reply_text('Событие добавлено!')

def list_events(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    event_manager = EventManager(user_id)
    events = event_manager.get_all_events()
    if events:
        update.message.reply_text('Ваши события:\n' + '\n'.join(events))
    else:
        update.message.reply_text('У вас нет событий.')

# Точка входа в приложение
def main():
    initialize_database()

    updater = Updater('YOUR_TELEGRAM_BOT_TOKEN_HERE', use_context=True)

    # Получить диспетчера для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрация обработчиков команд
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("add_event", add_event))
    dp.add_handler(CommandHandler("list_events", list_events))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()