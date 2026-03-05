from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, QListWidget, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout
import os

app = QApplication([])
notes = []

STYLE ="""
font-weight: bold;
    }
    QPushButton:hover {
        background-color: #D10000;
        color: #fQWidget {
        background-color: #470303;
        color: #A13737;
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 13px;
    }


    QTextEdit {
        background-color: #853282;
        color: #570A54;
        border: 2px solid #D5E4EB;
        border-radius: 10px;
        font-size: 14px;
        selection-background-color: #755074;
    }
   
    QLineEdit {
        background-color: #853282;
        color: #570A54;
        border: 2px solid #D5E4EB;
        border-radius: 6px;
        selection-background-color: #755074;
    }
   
    QLineEdit:focus {
        border: 2px solid #4183A6;
    }


    QListWidget {
        background-color: #853282;
        color: #570A54;
        border: 2px solid #D5E4EB;
        border-radius: 6px;
        selection-background-color: #755074;
    }
   
    QListWidget:item {
        padding: 6px 8px;
        border-raidus: 4px;
    }
   
    QListWidget:item:selected {
        background-color: #5C8796;
        color: #570A54;
    }
   
    QListWidget:item:hover:!selected {
        background-color: #570A54;
    }


    QLabel {
        font-weight: bold;
        font-size: 15px;
        color: #ffffff;
        padding: 4px 0px 2px 2px;
    }


    QPushButton {
        background-color: #ffffff;
        color: #000000;
        border: 2px solid #004933;
        border-radius: 6px;
        padding: 7px 12px;fffff;
    }
    QPushButton:pressed {
        background-color: #082925;
        color: #EAFBF9
    }


"""

'''

|Вікно |
'''

notes_win = QWidget()
notes_win.setWindowTitle("Smatr Notes")
notes_win.resize(900,600)
notes_win.setStyleSheet(STYLE)

'''
|Віджеи вікна|
'''

field_text = QTextEdit()

list_notes = QListWidget()
list_notes_label = QLabel("Список нотаток")

button_notes_create = QPushButton("Створити Нотатку")
button_notes_delete = QPushButton("Видалити Нотатку")
button_notes_save = QPushButton("Зберегти Нотатку")

list_tags_labe = QLabel("список тегів")
list_tags = QListWidget()
field_tag = QLineEdit('')
field_tag.setPlaceholderText("Введіть тег...")
button_tag_create = QPushButton("Додати Тег")
button_tag_delete = QPushButton("Видалити Тег")
button_tag_search = QPushButton("Шукати нотатку за тегом")

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)

col_2 = QVBoxLayout()
col_2. addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget(button_notes_create)
row_1.addWidget(button_notes_delete)

col_2.addLayout(row_1)
col_2.addWidget(button_notes_save)

row_2 = QHBoxLayout()
row_2.addWidget(button_tag_create)
row_2.addWidget(button_tag_delete)

col_2.addLayout(row_2)
col_2.addWidget(button_tag_search)

layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)

'''
Робота з нотатками
'''

def load_notes():
    index = 0
    while True:
        filename = f"{index}.txt"
        if not os.path.exists(filename):
            break
        with open(filename, "r", encoding = "utf-8") as file:
            lines = file.read().split('\n')
            name = lines[0]
            text = lines[1]
            tags= lines[2].split() if len(lines) > 2 else []
            notes.append([name, text ,tags])
            list_notes.addItem(name)
        index += 1

def save_all_notes():
    for i, note in enumerate(notes):
        with open(f"{i}.txt", "w", encoding= "utf-8") as file:
            file.write(note[0] + '\n')
            file.write(note[1] + '\n')
            file.write(''.join(note[2]) + '\n')

def show_note():
    key = list_notes.selectedItems()[0].text()
    for note in note:
        if note[0] == key:
            field_text.setText(note[1])
            list_tags.clear()
            list_tags.addItems(note[2])

list_notes.itemClicked.connect(show_note)

def add_note():
    note_name, ok = QInputDialog.getText(notes_win, "Додати замітки", "Назва замітки:")
    if ok and note_name !="":
        note = [note_name, '', []]
        notes.append(note)
        list_notes.addItems(note_name)
        save_all_notes()


button_notes_create.clicked.connect(add_note)

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        for note in notes:
            if note[0] == key:
                note[1] = field_text.toPlainText()
                break
        save_all_notes()

button_notes_save.clicked.connect(save_note)

def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        for i, note in enumerate(notes):
            if note[0] == key:
                notes.pop(i)
                break
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        for i in range(1000):
            try:
                os.remove(f"{i}.txt")
            except:
                break
                for note in notes:
                    list_notes.addItems(note[0])
        save_all_notes()

button_notes_delete.clicked.connect(del_note)

'''
Робота з тегами
'''

def add_tag():
    if list_notes. selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        for note in notes:
            if note[0] == key and tag not in note[2]:
                note[2].append(tag)
                list_tags.addItem(tag)
                list_tags.addItem(tag)
                field_tag.clear()
        save_all_notes() 

button_tag_create.clicked.connect(add_tag)


def del_tag():
    if list_tags.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        for note in notes:
            if note[0] == key and tag in note[2]:
                note[2].remove(tag)
                list_tags.clear()
                for note in notes:
                    if note[0] == key:
                        list_tags.addItems(note[2])
                save_all_notes()
        
button_tag_delete.clicked.connect(del_tag)

def search_tag():
    tag = field_tag.text()
    if button_tag_search.text() == "Шукати нотатку за Тегом" and tag:
        list_notes.clear()
        for note in notes:
            if tag in note[2]:
                list_notes.addItem(note[0])
        button_tag_search.setText("Скинути пошук")
    else:
        list_notes.clear
        for note in notes:
            list_notes.addItem(note[0])
        button_tag_search.setText("Шукати нотатку за Тегом")
        field_tag.clear()

button_tag_search.clicked.connect(search_tag)


load_notes()
notes_win.show()
app.exec_()









