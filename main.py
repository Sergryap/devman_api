import os
import requests
from api_methods import send_message
from textwrap import dedent
from math import trunc
from time import sleep

from dotenv import load_dotenv
from logger import MyLogsHandler

import logging
logger = logging.getLogger('telegram')


def main():
    """Функция получения результата проверок в ожидании в бексконечном цикле"""
    chat_id = os.getenv('CHAT_ID')
    token = os.getenv('TOKEN_TG')

    logger.setLevel(logging.WARNING)
    logger.addHandler(MyLogsHandler(token, chat_id))
    logger.warning(f'Бот запущен')

    url = "https://dvmn.org/api/long_polling/"
    headers = {'Authorization': f'Token {os.getenv("TOKEN_DEV")}'}
    timestamp = ""

    while True:
        try:
            response = requests.get(url, params={"timestamp": timestamp}, headers=headers)
            response.raise_for_status()
            reviews = response.json()
        except ConnectionError as er_conn:
            sleep(5)
            logger.warning(f'Соединение было прервано: {er_conn}', stack_info=True)
            continue
        except requests.exceptions.ReadTimeout as er_time:
            logger.warning(f'Ошибка ReadTimeout: {er_time}', stack_info=True)
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
            timestamp = ""
        else:
            logger.error('Не удалось получить данные', stack_info=True)

    logger.critical('Бот вышел из цикла', stack_info=True)


if __name__ == '__main__':
    load_dotenv()
    main()
