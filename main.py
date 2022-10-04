from api_methods import ApiMethod
from pprint import pprint


def input_chat_id():
    """Ввод chat_id для отправки сообщений"""
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