from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit, QListWidget, QCheckBox, QGridLayout, QListWidgetItem, QLabel

class Task(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window
        self.list_widget = main_window.list_widget
        self.list_task = QListWidgetItem()

        self.is_editing: bool = True

        self.layout = QGridLayout(self)

        self.checkbox = QCheckBox()
        self.checkbox.toggled.connect(self.checkbox_on_toggle)

        self.field = QLineEdit()

        self.label = QLabel()
        self.label.hide()

        self.button_del = QPushButton("Del")
        self.button_del.clicked.connect(self.button_del_on_click)

        self.button_edit = QPushButton("Edit")
        self.button_edit.clicked.connect(self.button_edit_on_click)

        self.layout.addWidget(self.checkbox, 0, 0)
        self.layout.addWidget(self.field, 0, 1, 1, 7)
        self.layout.addWidget(self.label, 0, 1, 1, 7)
        self.layout.addWidget(self.button_del, 0, 9)
        self.layout.addWidget(self.button_edit, 0, 8)

        self.list_task.setSizeHint(self.sizeHint())

        self.list_widget.addItem(self.list_task)
        self.list_widget.setItemWidget(self.list_task, self)


    def button_del_on_click(self):
        row = self.list_widget.row(self.list_task)
        self.list_widget.takeItem(row)
        self.main_window.tasks.remove(self)

    def button_edit_on_click(self):
        if self.is_editing:
            self.field.hide()
            self.label.setText(self.field.text())
            self.label.show()
            self.is_editing = False

        else:
            self.label.hide()
            self.field.show()
            self.is_editing = True


    def checkbox_on_toggle(self, checked):
        font = self.label.font()
        font.setStrikeOut(checked)
        self.label.setFont(font)

        if checked:
            self.label.setStyleSheet("color: gray")
        else:
            self.label.setStyleSheet("color: white")


    @classmethod
    def create_from_data(cls, main_window, checked: bool, content: str) -> Task:
        task = Task(main_window)
        task.field.setText(content)
        task.button_edit.click()
        if checked:
            task.checkbox.toggle()

        return task