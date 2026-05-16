import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QListWidget
from item import Item

def start():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("ToDo List")
    window.resize(600, 400)

    layout = QVBoxLayout(window)

    list_widget = QListWidget()

    button_add = QPushButton("Add")

    def on_click() -> None:
        Item(list_widget)

    button_add.clicked.connect(on_click)

    layout.addWidget(list_widget)
    layout.addWidget(button_add)

    window.show()
    app.exec()

start()