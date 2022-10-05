import os
from api_methods import long_polling_timeout, send_message
from textwrap import dedent


def main():
    """Функция получения результата проверок в ожидании в бексконечном цикле. Точка входа"""

    chat_id = os.getenv('CHAT_ID')
    token = os.getenv('TOKEN_TG')
    headers = {'Authorization': f'Token {os.getenv("TOKEN_DEV")}'}

    send_message(token, chat_id, "Вы подключены к получению уведомлений о проверке заданий на Devman")
    while True:
        response = long_polling_timeout(headers)
        head = response['new_attempts'][0]
        msg = f"""\
        Ваша работа проверена:
        Результат: {'РАБОТА ПРИНЯТА' if head['is_negative'] == False else 'ТРЕБУЕТСЯ ДОРАБОТКА'}
        lesson_title: {head['lesson_title']}
        lesson_url: {head['lesson_url']}
        """
        send_message(token, chat_id, dedent(msg))


if __name__ == '__main__':
    main()
