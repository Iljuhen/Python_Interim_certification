import Notte


def write_file(array, mode):
    _file = open("notte.csv", mode='w', encoding='utf-8')
    _file.seek(0)
    _file.close()
    _file = open("notte.csv", mode=mode, encoding='utf-8')
    for notes in array:
        _file.write(Notte.Notte.to_string(notes))
        _file.write('\n')
        _file.close


def read_file():
    try:

        array = []
        fille = open("notte.csv", "r", encoding='utf-8')
        notes = fille.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Notte.Notte(id=split_n[0],
                               title=split_n[1],
                               body=split_n[2],
                               date=split_n[3])
            array.append(note)

    except Exception:
        print('Нет сохраненных заметок...')

    finally:
        return array
