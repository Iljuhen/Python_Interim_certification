import Function as func  

def hello():
    print("\nЭто программа 'Заметки'. Есть следующие функции:\n\n1 - вывод всех заметок из файла\n2 - добавление заметки\n3 - удаление заметки\n4 - редактирование заметки\n5 - сортировка заметок по дате\n6 - вывод заметки по id\n7 - выход\n\nВведите номер функции: ")
    
def goodbuy():
    print("До скорых встреч!")

def run():
    input_from_user = ''
    while input_from_user != '7':
        hello()
        input_from_user = input().strip()
        if input_from_user == '1':
            func.show('all')            
        if input_from_user == '2':
            func.add()
        if input_from_user == '3':
            func.show('all')
            func.id_edit_del_show('del')
        if input_from_user == '4':
            func.show('all')
            func.id_edit_del_show('edit')
        if input_from_user == '5':
            func.show('date')
        if input_from_user == '6':
            func.show('id')
            func.id_edit_del_show('show')
        if input_from_user == '7':
            goodbuy()
            break
