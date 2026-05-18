import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow


def main() -> None:
    app = QApplication(sys.argv)

    main_window = MainWindow(app)
    main_window.show()

    app.exec()


if __name__ == '__main__':
    main()