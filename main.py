import os
import requests
from api_methods import send_message
from textwrap import dedent
from math import trunc
from time import sleep

from dotenv import load_dotenv
load_dotenv()


def main():
    """Функция получения результата проверок в ожидании в бексконечном цикле"""
    url = "https://dvmn.org/api/long_polling/"
    chat_id = os.getenv('CHAT_ID')
    token = os.getenv('TOKEN_TG')
    headers = {'Authorization': f'Token {os.getenv("TOKEN_DEV")}'}
    send_message(token, chat_id, "Вы подключены к получению уведомлений о проверке заданий на Devman")
    timestamp = ""

    while True:
        try:
            response = requests.get(url, params={"timestamp": timestamp}, headers=headers)
            response.raise_for_status()
            reviews = response.json()
        except (requests.exceptions.ReadTimeout, ConnectionError):
            sleep(2)
            continue

        if reviews['status'] == 'timeout':
            timestamp = trunc(reviews['timestamp_to_request'])
            continue
        elif reviews['status'] == 'found':
            head = reviews['new_attempts'][0]
            msg = f"""\
            Ваша работа проверена:
            Результат: {'РАБОТА ПРИНЯТА' if head['is_negative'] == False else 'ТРЕБУЕТСЯ ДОРАБОТКА'}
            lesson_title: {head['lesson_title']}
            lesson_url: {head['lesson_url']}
            """
            send_message(token, chat_id, dedent(msg))


if __name__ == '__main__':
    main()
