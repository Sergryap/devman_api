import os
from api_methods import long_polling_timeout, send_message


def main():
    """Функция получения результата проверок в ожидании в бексконечном цикле. Точка входа"""
    chat_id = os.getenv('CHAT_ID')
    token = os.getenv('TOKEN_TG')
    headers = {'Authorization': f'Token {os.getenv("TOKEN_DEV")}'}
    send_message(token, chat_id, "Вы подключены к получению уведомлений о проверке заданий на Devman")
    while True:
        response = long_polling_timeout(headers)
        head = response['new_attempts'][0]
        msg = f"Ваша работа проверена:\n" \
              f"Результат: {'РАБОТА ПРИНЯТА' if head['is_negative'] == False else 'ТРЕБУЕТСЯ ДОРАБОТКА'}\n" \
              f"lesson_title: {head['lesson_title']}\n" \
              f"lesson_url: {head['lesson_url']}"
        send_message(token, chat_id, msg)


if __name__ == '__main__':
    main()
