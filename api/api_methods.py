import requests
from pprint import pprint

from api.oauth import TOKEN_DEV, TOKEN_TG


class ApiMethod:

    URL_USER = "https://dvmn.org/api/user_reviews/"
    URL_LONG = "https://dvmn.org/api/long_polling/"
    URL_TG = "https://api.telegram.org/bot"
    TOKEN_TG = TOKEN_TG
    HEADERS = {'Authorization': f'Token {TOKEN_DEV}'}

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
        """Метод получения результата проверки в режиме ожидания в цикле"""
        response = self.long_polling()
        while response['status'] == 'timeout':
            response = self.long_polling(timestamp=response['timestamp_to_request'])
        return response

    def send_message(self, msg: str):
        """Отправка сообщения через api TG"""
        requests.get(rf"{self.URL_TG}{self.TOKEN_TG}/sendmessage?chat_id={self.chat_id}&text={msg}")


def input_chat_id():
    """Ввод chat_id"""
    chat_id = ''
    while not chat_id.isdigit():
        chat_id = input('Введите ваш chat_id в telegram: ')
        if chat_id.isdigit():
            return int(chat_id)
        else:
            print('Неверный формат chat_id')


def main():
    """Функция получения результата проверок в ожидании в бексконечном цикле"""
    # user = ApiMethod(1642719191)
    chat_id = input_chat_id()
    user = ApiMethod(chat_id)
    user.send_message("Вы подключены к получению уведомлений о проверке заданий на Devmane")
    while True:
        response = user.long_polling_timeout()
        head = response['new_attempts'][0]
        msg = f"Ваша работа проверена:\n" \
              f"Результат: {'РАБОТА ПРИНЯТА' if head['is_negative'] == False else 'ТРЕБУЕТСЯ ДОРАБОТКА'}\n" \
              f"lesson_title: {head['lesson_title']}\n" \
              f"lesson_url: {head['lesson_url']}"
        user.send_message(msg)
        pprint(response)


if __name__ == '__main__':
    main()
