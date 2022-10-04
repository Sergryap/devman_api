import requests
import json

from api.oauth import TOKEN_DEV, TOKEN_TG


class ApiMethod:

    URL_USER = "https://dvmn.org/api/user_reviews/"
    URL_LONG = "https://dvmn.org/api/long_polling/"
    URL_TG = "https://api.telegram.org/bot"
    TOKEN_DEV = TOKEN_DEV
    TOKEN_TG = TOKEN_TG

    def __init__(self, chat_id: int):
        self.chat_id = chat_id

    def long_polling(self):
        """Метод api devman"""
        response = requests.get(self.URL_USER, headers={'Authorization': f'Token {self.TOKEN_DEV}'}).json()
        return response

    def send_message(self, msg: str):
        """Отправка сообщения через api TG"""
        requests.get(rf"{self.URL_TG}{self.TOKEN_TG}/sendmessage?chat_id={self.chat_id}&text={msg}")


if __name__ == '__main__':
    a = ApiMethod(1642719191)
    res = a.long_polling()
    a.send_message("Привет")
    print(res)
