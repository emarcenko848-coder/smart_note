from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, QListWidget, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout
import os

import json

app = QApplication([])
notes = []

'''

|Вікно |
'''

notes_win = QWidget()
notes_win.setWindowTitle("Smatr Notes")
notes_win.resize(900,600)

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
            lines = lines[0]
            lines = lines[1]
            lines = lines[2].split() if len(lines) > 2 else []




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
        safe_all_notes()


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
        safe_all_notes() 

button_tag_create.clicked.connect(add_tag)

def safe_all_notes():
    for i, note in enumerate(notes):
        with open(f"{i}.txt", "w", encoding="utf-8") as file:
            file.write(note[0] + '\n')
            file.write(note[1] + '\n')
            file.write(''.join(note[2]) + '\n')

def add_tag():  
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0]. text()
        tag = field_tag.text()
        if not tag in note[key]["теги"]:
            note[key]["теги"].append(tag)
            list_tags.addItems(tag)
            field_tag.clear()
        with open("notes data.json", "w", encoding = "utf-8") as file:
            json.dump(note, file, sort_keys = True, ensure_ascii = True, indent = 2)
    else:
        print("Замітка для додавання тегу не обрана!")

button_tag_create.clicked.connect(add_tag)

def del_tag():
    if list_tags.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        note[key]["теги"].remove(tag)
        list_tags.clear()
        list_tags.addItems(note[key]["теги"])
        with open("notes data.json", "w", encoding = "utf-8") as file:
            json.dump(note, file, sort_kes = True, ensure_ascii = True, indent = 2)
    else:
        print("Тег не обрано!")
        
button_tag_delete.clicked.connect(del_tag)

def search_tag():
    print(button_tag_search.text())
    tag = field_tag.text()
    if button_tag_search.text() == "Шукати нотатку за Тегом" and tag:
        print(tag)
        notes_filtered = {}
        for i in note:
            if tag in note[i]  ["теги"]:
                notes_filtered [i] = note[i]
        button_tag_search.setText("Скинути пошук")
        list_notes.clear
        list_tags.clear
        list_notes.addItem(notes_filtered)
        print(button_tag_search.text())
    elif button_tag_search.text() + "Синути пошук":
        field_tag.clear()
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(note)
        button_tag_search.setText("Шукати нотатку за Тегом")
        print(button_tag_search.text())
    else:
        pass

button_tag_search.clicked.connect(search_tag)

with open("notes_data.json", "r") as file:
    note = json.load(file)
list_notes.addItems(note)

app.exec_()









