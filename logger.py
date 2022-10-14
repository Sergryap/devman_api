import logging
from api_methods import send_message


class MyLogsHandler(logging.Handler):

    def __init__(self, token, chat_id):
        super().__init__()
        self.token = token
        self.chat_id = chat_id

    def emit(self, record: logging.LogRecord) -> None:
        log_entry = self.format(record)
        send_message(token=self.token, chat_id=self.chat_id, msg=log_entry)
