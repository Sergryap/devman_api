<h2>Описание</h2>
В программе реализован бот для Telegram.
Цель бота - информирование пользователя о проверке его работ в devman.
Программа состоит из трех модулей: api_methods.py, main.py и logger.py

В модуле api_methods реализована функция отправки сообщения через api telegram.

В модуле main реализована основная функция main (точка входа), содержащая в себе бесконечный цикл для получения 
данных из api devman и отправки их в chat_id пользователя telegram.

В модуле logger.py описан класс хэндлера для обработки логов.

## Установка на удаленном сервере (непосредственно на хосте)
<br> У вас должен быть установлен Python последней версии

##### Загрузить необходимые файлы в папку для установки:

`git clone https://github.com/Sergryap/devman_api.git`

##### В корневой папке проекта создать файл .env, содержащий:
TOKEN_DEV=<токен от сервиса Devman>
<br>TOKEN_TG=<токен от основного бота telegram>
<br>TOKEN_TG_LOG=<токен от бота для отправки логов>
<br>CHAT_ID=<идентификатор чата в telegram для отправки сообщений от бота>

##### Создать виртуальное окружение:
`python3 -m venv venv`
    
##### Активировать виртуальное окружение:

`source venv\bin\activate`
    
#####  Установить необходимые зависимости:

`pip install -r requirements.txt`
    
#####  Запустить скрипт:
`python3 main.py`
<br>Для постоянной работы бота, на последнем шаге использовать команду:
<br>`nohup python3 main.py`
<br>Либо запустить скрипт через утилиту screen в отдельном окне

<h2>Пример установки</h2>

![Screenshot from 2022-10-05 21-23-20](https://user-images.githubusercontent.com/99894266/194118086-0df5736e-f6f0-42f5-9413-1552cd62e592.png)

## Установка на удаленном сервере в docker-контейнере
<br> У вас должен быть установлен Docker на сервере
##### Загрузить необходимые файлы в папку для установки:

`git clone https://github.com/Sergryap/devman_api.git`

##### В корневой папке проекта создать файл .env, содержащий:
TOKEN_DEV=<токен от сервиса Devman>
<br>TOKEN_TG=<токен от основного бота telegram>
<br>TOKEN_TG_LOG=<токен от бота для отправки логов>
<br>CHAT_ID=<идентификатор чата в telegram для отправки сообщений от бота>
#### Находясь в корневой папке проекта, соберите образ, выполнив команду:
`sudo docker build --tag devman-bot:1.0 .`
#### Запустите созданный образ:
`sudo docker run -d --name devman-bot devman-bot:1.0`
### Пример установки:
![Screenshot from 2022-10-19 20-52-47](https://user-images.githubusercontent.com/99894266/196751768-7dbaa423-c3b7-47d4-8fd6-dc4fd68d9553.png)
![Screenshot from 2022-10-19 21-24-29](https://user-images.githubusercontent.com/99894266/196752008-ecb08cdf-855b-4fb9-b9a0-be35189e933e.png)
![Screenshot from 2022-10-19 21-26-05](https://user-images.githubusercontent.com/99894266/196751568-3f820cec-e4e0-45b6-9b41-11e609a2cdf4.png)

