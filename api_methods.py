import requests
import os

from dotenv import load_dotenv
load_dotenv()


def long_polling(headers, timestamp=None):
    """Функция long_polling api devman. Метод разовой проверки"""

    url = "https://dvmn.org/api/long_polling/"
    if timestamp:
        url += f"?timestamp={round(timestamp, 0)}"
    try:
        return requests.get(url, headers=headers).json()
    except (requests.exceptions.ReadTimeout, ConnectionError):
        return long_polling(timestamp)


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
    url = "https://api.telegram.org/bot"
    requests.get(rf"{url}{token}/sendmessage?chat_id={chat_id}&text={msg}")
