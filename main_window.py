from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QListWidget
from pathlib import Path
import json
from task import Task

class MainWindow(QWidget):
    def __init__(self, app: QApplication) -> None:
        super().__init__()
        self.tasks: list[Task] = []

        self.app = app

        self.setWindowTitle("ToDo List")
        self.resize(600, 400)

        self.layout = QVBoxLayout(self)

        self.list_widget = QListWidget()

        self.button_add = QPushButton("Add task")

        def on_click() -> None:
            task = Task(self)
            self.tasks.append(task)

        self.button_add.clicked.connect(on_click)

        self.layout.addWidget(self.list_widget)
        self.layout.addWidget(self.button_add)


        # load data if present
        path = Path("data.json")
        if path.exists():
            data: list[dict] = []
            with path.open("r") as file:
                data: list[dict] = json.load(file)

            for d in data:
                task = Task.create_from_data(self, d["checked"], d["content"])
                self.tasks.append(task)


    def closeEvent(self, event) -> None:
        path = Path("data.json")
        data: list[dict] = []
        for task in self.tasks:
            data.append({
                "checked": task.checkbox.isChecked(),
                "content": task.label.text()
            })

        with path.open("w") as file:
            json.dump(data, file)

        event.accept()