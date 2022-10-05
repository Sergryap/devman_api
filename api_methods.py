import requests
from math import trunc

from dotenv import load_dotenv
load_dotenv()


def long_polling(headers, timestamp=None):
    """Функция long_polling api devman. Метод разовой проверки"""

    url = "https://dvmn.org/api/long_polling/"
    timestamp = trunc(timestamp) if timestamp else ""
    payload = {"timestamp": timestamp}

    try:
        response = requests.get(url, params=payload, headers=headers)
        response.raise_for_status()
        return response.json()

    except (requests.exceptions.ReadTimeout, ConnectionError):
        return long_polling(headers, timestamp)


def long_polling_timeout(headers):
    """
    Функция получения результата проверки в режиме ожидания в цикле
    До появления статуса о проверке работы.
    Цикл прерывается и функция завершается, при появлении результата проверки работы
    """
    response = long_polling(headers)
    while response['status'] == 'timeout':
        response = long_polling(headers, timestamp=response['timestamp_to_request'])
    return response


def send_message(token, chat_id, msg: str):
    """Отправка сообщения через api TG"""
    url = f"https://api.telegram.org/bot{token}/sendmessage"
    payload = {'chat_id': chat_id, 'text': msg}
    try:
        response = requests.get(url, params=payload)
        response.raise_for_status()
    except (requests.exceptions.ReadTimeout, ConnectionError):
        return send_message(token, chat_id, msg)
