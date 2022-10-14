import requests
from time import sleep
import logging
logger = logging.getLogger('telegram')


def send_message(token, chat_id, msg: str):
    """Отправка сообщения через api TG"""
    url = f"https://api.telegram.org/bot{token}/sendmessage"
    payload = {'chat_id': chat_id, 'text': msg}
    while True:
        try:
            response = requests.get(url, params=payload)
            response.raise_for_status()
            return
        except (requests.exceptions.ReadTimeout, ConnectionError) as er:
            sleep(5)
            logger.warning(f'Ошибка на стороне Tg: {er}', stack_info=True)
            continue
