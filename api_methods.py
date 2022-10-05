import requests
import os

from dotenv import load_dotenv
load_dotenv()


URL_LONG = "https://dvmn.org/api/long_polling/"
URL_TG = "https://api.telegram.org/bot"
TOKEN_TG = os.getenv('TOKEN_TG')
HEADERS = {'Authorization': f'Token {os.getenv("TOKEN_DEV")}'}


def long_polling(timestamp=None):
    """Функция long_polling api devman. Метод разовой проверки"""
    url = URL_LONG
    if timestamp:
        url += f"?timestamp={round(timestamp, 0)}"
    try:
        return requests.get(URL_LONG, headers=HEADERS).json()
    except (requests.exceptions.ReadTimeout, ConnectionError):
        return long_polling(timestamp)


def long_polling_timeout():
    """
    Функция получения результата проверки в режиме ожидания в цикле
    До появления статуса о проверке работы.
    Цикл прерывается и функция завершается, при появлении результата проверки работы
    """
    response = long_polling()
    while response['status'] == 'timeout':
        response = long_polling(timestamp=response['timestamp_to_request'])
    return response


def send_message(chat_id: int, msg: str):
    """Отправка сообщения через api TG"""
    requests.get(rf"{URL_TG}{TOKEN_TG}/sendmessage?chat_id={chat_id}&text={msg}")
