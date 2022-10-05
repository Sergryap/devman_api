<h2>Описание</h2>
В программе реализован бот для Telegram.
Цель бота - информирование пользователя о проверке его работ в devman.
Программа состоит из двух модулей: api_methods.py и main.py

В модуле api_methods реализованы функции взаимодействие с api telegram и devman.

В модуле main реализована основная функция main (точка входа), содержащая в себе бесконечный цикл для получения 
данных из api devman и отправки их в chat_id пользователя telegram.

<h2>Установка</h2>
<br> У вас должен быть установлен Python последней версии
<br>1. В заранее созданной папке проекта создать файл .env, содержащий:
<br>TOKEN_DEV=<токен от сервиса Devman>
<br>TOKEN_TG=<токен от бота telegram>
<br>CHAT_ID=<идентификатор чата в telegram для отправки сообщений от бота>

<br>2. Создать виртуальное окружение:
    <br>python -m venv venv
    
<br>3. Активировать виртуальное окружение:
    <br>Для Unix-систем:
    <br>source venv\bin\activate
    <br>Для Windows:
    <br>venv\Scripts\activate
    
<br>4. Установить необходимые зависимости:
    <br>pip install -r requirements txt
    
<br>5. Запустить скрипт:
    <br>python main.py
    
<br>Для unix систем использовать команду python3 вместо python

<br>Быстрый способ выложить бота на виртуальном удаленном сервере.
<br>Выполнить те же шаги по установке.
<br>Но, если требуется постоянная работа бота, то на последнем шаге использовать команду:
<br>nohup python3 main.py

<h2>Пример установки</h2>

![Screenshot from 2022-10-05 21-23-20](https://user-images.githubusercontent.com/99894266/194118086-0df5736e-f6f0-42f5-9413-1552cd62e592.png)
