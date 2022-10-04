import requests
import os

from dotenv import load_dotenv
load_dotenv()


class ApiMethod:
    """Класс для взаимодействия с api telegram и devman"""

    URL_USER = "https://dvmn.org/api/user_reviews/"
    URL_LONG = "https://dvmn.org/api/long_polling/"
    URL_TG = "https://api.telegram.org/bot"
    TOKEN_TG = os.getenv('TOKEN_TG')
    HEADERS = {'Authorization': f'Token {os.getenv("TOKEN_DEV")}'}

    def __init__(self, chat_id: int):
        self.chat_id = chat_id

    def long_polling(self, timestamp=None):
        """Метод long_polling api devman. Метод разовой проверки"""
        url = self.URL_LONG
        if timestamp:
            url += f"?timestamp={round(timestamp, 0)}"
        try:
            return requests.get(self.URL_LONG, headers=self.HEADERS).json()
        except (requests.exceptions.ReadTimeout, ConnectionError):
            return self.long_polling(timestamp)

    def long_polling_timeout(self):
        """
        Метод получения результата проверки в режиме ожидания в цикле
        До появления статуса о проверке работы
        """
        response = self.long_polling()
        while response['status'] == 'timeout':
            response = self.long_polling(timestamp=response['timestamp_to_request'])
        return response

    def send_message(self, msg: str):
        """Отправка сообщения через api TG"""
        requests.get(rf"{self.URL_TG}{self.TOKEN_TG}/sendmessage?chat_id={self.chat_id}&text={msg}")
