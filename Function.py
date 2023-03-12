import File_options
import Notte
import Ui

number = 0  # Минимум необходимых знаков в заметке


def add():
    note = Ui.create_note()
    array = File_options.read_file()
    for notes in array:
        if Notte.Notte.get_id(note) == Notte.Notte.get_id(notes):
            Notte.Notte.set_id(note)
    array.append(note)
    File_options.write_file(array, 'a')
    print('Заметка добавлена...')
    input('Нажмите "Enter" для продолжения...')


def show(text):
    logic = True
    array = File_options.read_file()
    if text== 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Notte.Notte.map_note(notes))
                        
        if text == 'id':
            logic = False
            print('ID: ' + Notte.Notte.get_id(notes))
        if text == 'date':
            logic = False
            if date in Notte.Notte.get_date(notes):
                print(Notte.Notte.map_note(notes))
    input('Нажмите "Enter" для продолжения...')
        
    if logic == True:
        print('Нет ни одной заметки...')
        input('Нажмите "Enter" для продолжения...')


def id_edit_del_show(text):
    idd = input('Введите id необходимой заметки: ')
    array = File_options.read_file()
    logic = True
    for notes in array:
        if idd == Notte.Notte.get_id(notes):
            logic = False
            if text == 'edit':
                note = Ui.create_note()
                Notte.Notte.set_title(notes, note.get_title())
                Notte.Notte.set_body(notes, note.get_body())
                Notte.Notte.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'show':
                print(Notte.Notte.map_note(notes))
    input('Нажмите "Enter" для продолжения...')
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    File_options.write_file(array, 'a')
