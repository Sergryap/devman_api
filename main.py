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
    """Функция получения результата проверок в ожидании в бесконечном цикле"""
    load_dotenv()

    chat_id = os.getenv('CHAT_ID')
    token = os.getenv('TOKEN_TG')
    token_log = os.getenv('TOKEN_TG_LOG')

    logger.setLevel(logging.WARNING)
    logger.addHandler(MyLogsHandler(token_log, chat_id))
    logger.warning('Бот запущен')

    url = "https://dvmn.org/api/long_polling/"
    headers = {'Authorization': f'Token {os.getenv("TOKEN_DEV")}'}
    timestamp = ""

    while True:
        try:
            response = requests.get(url, params={"timestamp": timestamp}, headers=headers)
            response.raise_for_status()
            reviews = response.json()

            if reviews.get('status') == 'timeout':
                timestamp = trunc(reviews['timestamp_to_request'])
                continue
            elif reviews.get('status') == 'found':
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

        except ConnectionError as err:
            sleep(5)
            logger.warning(f'Соединение было прервано: {err}', stack_info=True)
            continue
        except requests.exceptions.ReadTimeout as err:
            logger.warning(f'Ошибка ReadTimeout: {err}', stack_info=True)
            continue
        except Exception as err:
            logger.exception(err)

    logger.critical('Бот вышел из цикла и упал:', stack_info=True)


if __name__ == '__main__':
    main()
