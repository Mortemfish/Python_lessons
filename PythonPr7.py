import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, QFileDialog, QMessageBox
from PyQt5.QtCore import QFileInfo

class NoteApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Устанавливаем заголовок окна
        self.setWindowTitle("Приложение для заметок")
        self.setGeometry(100, 100, 600, 400)

        # Создаем текстовый редактор
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)

        # Создаем меню
        self.create_menu()

        # Флаг для отслеживания сохранения файла
        self.current_file = None

    def create_menu(self):
        # Создаем меню
        menubar = self.menuBar()

        # Меню "Файл"
        file_menu = menubar.addMenu("Файл")

        # Добавляем действие для создания новой заметки
        new_action = QAction("Новая заметка", self)
        new_action.triggered.connect(self.new_note)
        file_menu.addAction(new_action)

        # Добавляем действие для сохранения заметки
        save_action = QAction("Сохранить", self)
        save_action.triggered.connect(self.save_note)
        file_menu.addAction(save_action)

    def new_note(self):
        # Очищаем текстовый редактор для новой заметки
        self.textEdit.clear()
        self.current_file = None

    def save_note(self):
        # Если файл уже существует, сохраняем в него
        if self.current_file:
            with open(self.current_file, 'w', encoding='utf-8') as file:
                file.write(self.textEdit.toPlainText())
            QMessageBox.information(self, "Сохранение", "Заметка успешно сохранена!")
        else:
            # Если файла нет, открываем диалоговое окно для выбора имени файла
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить заметку", "", "Text Files (*.txt);;All Files (*)", options=options)
            if file_name:
                self.current_file = file_name
                with open(self.current_file, 'w', encoding='utf-8') as file:
                    file.write(self.textEdit.toPlainText())
                QMessageBox.information(self, "Сохранение", "Заметка успешно сохранена!")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Создаем и показываем главное окно приложения
    window = NoteApp()
    window.show()

    sys.exit(app.exec_())
