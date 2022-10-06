import requests
from time import sleep


def send_message(token, chat_id, msg: str):
    """Отправка сообщения через api TG"""
    url = f"https://api.telegram.org/bot{token}/sendmessage"
    payload = {'chat_id': chat_id, 'text': msg}
    while True:
        try:
            response = requests.get(url, params=payload)
            response.raise_for_status()
            break
        except (requests.exceptions.ReadTimeout, ConnectionError):
            sleep(2)
            continue
