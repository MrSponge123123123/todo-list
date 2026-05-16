import sys
from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit, QListWidget, QCheckBox, QGridLayout, QListWidgetItem

class Item(QWidget):
    def __init__(self, list_widget: QListWidget, /):
        super().__init__()

        self.list_widget = list_widget
        self.list_item = QListWidgetItem()

        self.layout = QGridLayout(self)

        self.checkbox = QCheckBox()
        self.field = QLineEdit()
        self.button = QPushButton("Del")
        self.button.clicked.connect(self.on_click)

        self.layout.addWidget(self.checkbox, 0, 0)
        self.layout.addWidget(self.field, 0, 1, 1, 2)
        self.layout.addWidget(self.button, 0, 3)

        self.show()

        self.list_item.setSizeHint(self.sizeHint())

        self.list_widget.addItem(self.list_item)
        self.list_widget.setItemWidget(self.list_item, self)

    def on_click(self):
        row = self.list_widget.row(self.list_item)
        self.list_widget.takeItem(row)