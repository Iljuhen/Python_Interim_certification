import Notte


def create_note():
    title = input('Введите заголовок заметки: ')
    body = input('Введите заметку: ')
    return Notte.Notte(title=title, body=body)





# def check_len_text_input(text, n):
#     if len(text) <= n:
#         print(f'Количество вводимых символов должено быть больше {n} \n')
#         text = input('Повторите ввод: ')
#     else:
#         return text



