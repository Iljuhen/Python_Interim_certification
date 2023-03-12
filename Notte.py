import uuid
from datetime import datetime



class Notte:
    def __init__(self, id = str(uuid.uuid1())[0:3],  title = "Заголовок заметки", body = "Текст заметки", date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date 

    def get_id(notte):
        return notte.id
    
    def get_title(notte):
        return notte.title
    
    def get_body(notte):
        return notte.body
    
    def get_date(notte):
        return notte.date

    def set_id(notte):
        notte.id = str(uuid.uuid1())[0:3]

    def set_title(notte, title):
        notte.title = title

    def set_body(notte, body):
        notte.body = body

    def set_date(notte):
        notte.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(notte):
        return notte.id + ';' + notte.title + ';' + notte.body + ';' + notte.date

    def map_note(notte):
        return '\nID: ' + notte.id + '\n' + 'Заголовок: ' + notte.title + '\n' + 'Содержание: ' + notte.body + '\n' + 'Дата публикации: ' + notte.date



